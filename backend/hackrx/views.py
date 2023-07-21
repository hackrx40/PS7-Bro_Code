from django.shortcuts import render

# Create your views here.

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

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

# Example usage
icp = {
    'keywords': 'Data analytics business intelligence',
    'job_function': 'Technology',
    'age_category': '30-40',
    'geography': 'USA',
    'company_name': 'Acme Inc.',
    'company_size': '500-1000'
}

lead = {
    'keywords': 'Data analytics marketing',
    'job_function': 'Sales',
    'age_category': '30-40',
    'geography': 'USA',
    'company_name': 'Acme Inc.',
    'company_size': '500-1000'
}

score = score_lead(lead, icp)
print(f"Lead score: {score}")


def index(request):
    context = {
    'recipient': "HackRx 4.0",
    'offer': "Easy EMI",
    'call_to_action': "Click Now! Limited Time Offer",
    'benefit': "Get 10% off on your first purchase",
    'image_url': "https://scontent-maa2-2.xx.fbcdn.net/v/t1.6435-9/57104038_2300925359929883_1446565781524447232_n.jpg?_nc_cat=101&ccb=1-7&_nc_sid=730e14&_nc_ohc=dP2vICM1_78AX9AyfX2&_nc_ht=scontent-maa2-2.xx&oh=00_AfAhQbcJy1b9rtXqPeljSW6vgLN9iOph1Fy19TJqbW-4mA&oe=64E189AC",
    'offer_url': "https://www.facebook.com/hackrx4/"
    }

    return render(request, 'offer.html', context=context)


from rest_framework.serializers import *
from .models import *
from rest_framework.exceptions import *
from django.core.files.base import ContentFile
import base64

class LeadsSerializer(ModelSerializer):
    class Meta:
        model = Leads
        fields = "__all__"

class TargetSerializer(ModelSerializer):
    class Meta:
        model = Target
        fields = "__all__"