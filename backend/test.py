import csv
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
import pandas as pd

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

from difflib import SequenceMatcher

def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def score_lead(lead, icp):
    score = 0
    max_score = 3
    
    # Compare keywords using cosine similarity
    vectorizer = CountVectorizer()
    lead_keywords_vector = vectorizer.fit_transform([lead['keywords']])
    icp_keywords_vector = vectorizer.transform([icp['keywords']])
    keywords_similarity = cosine_similarity(lead_keywords_vector, icp_keywords_vector)[0][0]
    if keywords_similarity >= 0.9:
        score += 1
    
    # Compare geography using cosine similarity
    vectorizer = CountVectorizer()
    lead_geography_vector = vectorizer.fit_transform([lead['geography']])
    icp_geography_vector = vectorizer.transform([icp['geography']])
    geography_similarity = cosine_similarity(lead_geography_vector, icp_geography_vector)[0][0]
    if geography_similarity >= 0.9:
        score += 1
    
    # Compare company name using cosine similarity
    vectorizer = CountVectorizer()
    lead_company_name_vector = vectorizer.fit_transform([lead['company_name']])
    icp_company_name_vector = vectorizer.transform([icp['company_name']])
    company_name_similarity = cosine_similarity(lead_company_name_vector, icp_company_name_vector)[0][0]
    if company_name_similarity >= 0.9:
        score += 1
    
    # Normalize score to be between 1 and 10
    normalized_score = (score / max_score) * 9 + 1
    
    return normalized_score

# def add_lead_score_to_csv(icp, input_csv_file, output_csv_file):
    # df = pd.read_csv(input_csv_file)
    
#     # def calculate_lead_score(row):
#     #     lead = {
#     #         'keywords': row.get('keywords', ''),
#     #         'job_function': row.get('job_function', ''),
#     #         'age_category': row.get('age_category', ''),
#     #         'geography': row.get('geography', ''),
#     #         'company_name': row.get('company_name', ''),
#     #         'company_size': row.get('company_size', '')
#     #     }
#     #     return score_lead(lead, icp)
    
    # df['lead_score'] = df.apply(calculate_lead_score, axis=1)
    
    # df.to_csv(output_csv_file, index=False)

# icp = {
#     'keywords': 'Software Engineer',
#     'job_function': 'Technology',
#     'age_category': 'Any Age',
#     'geography': 'India',
#     'company_name': 'Bajaj',
#     'company_size': '500-1000'
# }

# from bardapi import Bard
# import os 
# os.environ['_BARD_API_KEY']="ZAg5sP8BYFYcPLP3_Xp1lNZ_FLh4db9m_K8d1QRKYubXwqMmuCzefso1al-aqcC7xz6sDw."
# import json
# import pandas as pd

# df = pd.read_csv(r"C:\Users\HP\Desktop\HackRx\result_3.csv")

# for index, row in df.iterrows():
#     if index == 0 and index == 1:
#         continue
#     row_string = ','.join(row.astype(str))
#     input_text = "Summarise the input text I will give you into the following points: "
#     for index, (key, value) in enumerate(icp.items()):
#         input_text += f"{index}. {key} max-length{len(value) + 2}"

#     input_text += f"input text: {row_string} write the out in json format and don't write anything else"

#     bard_output = Bard().get_answer(input_text)['content']
#     json_string = bard_output.split("json")[1].split("```")[0]
#     convert = json.loads(json_string)

#     input_text = f"icp={icp} lead_data={convert} from a scale of 1-10 score and compare the data with the icp(Ideal Candidate Profile), give keywords and job function the most priority. write it out in json format. don't write any code use your understanding."
#     bard_output = Bard().get_answer(input_text)['content']
#     print(bard_output)
#     break    

# add_lead_score_to_csv(icp, r"C:\Users\HP\Desktop\HackRx\result_3.csv", 'output.csv')


# import nltk
# from nltk.corpus import stopwords
# from nltk.stem import WordNetLemmatizer
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity

# nltk.download('stopwords')
# nltk.download('wordnet')

# def normalize_text(text):
#     stop_words = set(stopwords.words('english'))
#     lemmatizer = WordNetLemmatizer()
#     tokens = nltk.word_tokenize(text)
#     tokens = [lemmatizer.lemmatize(token.lower()) for token in tokens if token.isalpha() and token not in stop_words]
#     return ' '.join(tokens)

# def calculate_cosine_similarity(text1, text2):
#     tfidf_vectorizer = TfidfVectorizer()
#     tfidf_matrix = tfidf_vectorizer.fit_transform([text1, text2])
#     return cosine_similarity(tfidf_matrix[0:1], tfidf_matrix)[0][1]

# icp = {
#     'keywords': 'Data analytics business intelligence',
#     'job_function': 'Technology',
#     'age_category': '30-40',
#     'geography': 'India',
#     'company_name': 'Bajaj',
#     'company_size': '500-1000'
# }

# lead_data = {'keywords': 'Spring Framework, Java, pgAdmin, Spring Boot, Machine Learning, C++, Data Structures, Core Java, Flask, Python (Programming Language), SQL, Django, Competitive Programming, Database Management System (DBMS), Object-Oriented Programming (OOP)', 'job_function': 'Software Engineer-I', 'age_category': '2nd', 'geography': 'Pune, Maharashtra, India', 'company_name': 'Bajaj Markets', 'company_size': '10'}

# icp_text = normalize_text(' '.join(icp.values()))
# lead_text = normalize_text(' '.join(lead_data.values()))

# similarity_score = calculate_cosine_similarity(icp_text, lead_text)
# print(f"Similarity score: {similarity_score * 10:.2f}/1")

import pandas as pd
from collections import OrderedDict
from faker import Faker

fake = Faker()
df = pd.read_csv('result_2.csv')
df['lead_score'] = df.apply(lambda x: fake.random_element(elements=OrderedDict([(6, 0.5), (7,0.4), (8, 0.1)])), axis=1)

    
df.to_csv("output_2.csv", index=False)