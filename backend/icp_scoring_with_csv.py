import csv
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk

def normalize_text(text):
    # Tokenize text
    words = nltk.word_tokenize(text)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.lower() not in stop_words]
    
    # Lemmatize words
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    
    # Return normalized text
    return ' '.join(words)

def score_lead(lead, icp):
    score = 0
    max_score = 6
    
    # Normalize and compare keywords
    lead_keywords = normalize_text(lead['keywords'])
    icp_keywords = normalize_text(icp['keywords'])
    common_keywords = set(lead_keywords.split()) & set(icp_keywords.split())
    score += len(common_keywords)
    
    # Compare job function
    if lead['job_function'] == icp['job_function']:
        score += 1
    
    # Compare age category
    if lead['age_category'] == icp['age_category']:
        score += 1
    
    # Compare geography
    if lead['geography'] == icp['geography']:
        score += 1
    
    # Compare company name and size
    if lead['company_name'] == icp['company_name']:
        score += 1
    if lead['company_size'] == icp['company_size']:
        score += 1
    
    # Normalize score to be between 1 and 10
    normalized_score = (score / max_score) * 9 + 1
    
    return normalized_score

def add_lead_score_to_csv(icp, input_csv_file, output_csv_file):
    with open(input_csv_file, 'r') as input_file, open(output_csv_file, 'w', newline='') as output_file:
        reader = csv.DictReader(input_file)
        fieldnames = reader.fieldnames + ['lead_score']
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            lead = {
                'keywords': row.get('keywords', ''),
                'job_function': row.get('job_function', ''),
                'age_category': row.get('age_category', ''),
                'geography': row.get('geography', ''),
                'company_name': row.get('company_name', ''),
                'company_size': row.get('company_size', '')
            }
            lead_score = score_lead(lead, icp)
            row['lead_score'] = lead_score
            writer.writerow(row)

icp = {
    'keywords': 'Data analytics business intelligence',
    'job_function': 'Technology',
    'age_category': '30-40',
    'geography': 'USA',
    'company_name': 'Acme Inc.',
    'company_size': '500-1000'
}

add_lead_score_to_csv(icp, '<input_csv_file>', '<output_csv_file>')
