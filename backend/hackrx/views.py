from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.response import Response
from .serializers import *
from .models import *
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import serializers
from collections import OrderedDict
from rest_framework.parsers import *
from django.conf import settings
from drf_spectacular.types import OpenApiTypes
from django.core.mail import EmailMessage
from django.template.loader import render_to_string, get_template
from django.db.models import F, Q
from django.shortcuts import redirect
import requests
import pandas as pd
from tablib import Dataset
from difflib import SequenceMatcher
from django.http import HttpResponseRedirect
import random

def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

# Create your views here.

from faker import Faker
fake = Faker('EN_IN')

def generate_fake_lead():
    lead = Leads()
    lead.name = fake.name()
    lead.email = fake.email()
    lead.industry = fake.job()
    lead.company_size = fake.random_element(elements=('1-10', '11-50', '51-200', '201-500', '501-1000', '1001-5000', '5001-10,000', '10,001+'))
    lead.company_name = fake.company()
    lead.function = fake.job()
    lead.title = fake.job()
    lead.company_names = fake.company()
    lead.keywords = fake.word()
    lead.institute = fake.word()
    lead.state_progress = fake.random_element(elements=OrderedDict([(1, 0.60), (2, 0.25), (3, 0.10), (4, 0.05), ]))
    return lead

def send_connection_requests(linkedin_email, linkedin_password, lead_id, connection_message = "Hello"):
    import time
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.options import Options as ChromeOptions

    options = ChromeOptions()

    driver = webdriver.Chrome()
    # Set up the Selenium driver
    driver = webdriver.Chrome(options=options)

    driver.get('https://www.linkedin.com/login')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username')))
    username_field = driver.find_element(By.ID, 'username')
    for i in linkedin_email:
        username_field.send_keys(i)
        time.sleep(random.uniform(0.2, 0.5))
    password_field = driver.find_element(By.ID, 'password')
    for i in linkedin_password:
        password_field.send_keys(i)
        time.sleep(random.uniform(0.2, 0.5))
    password_field.send_keys(Keys.RETURN)

    lead = DetailedLeads.objects.get(id=lead_id)
    
    if lead.linkedinProfileUrl is None or lead.linkedinProfileUrl == "":
        print(lead.linkedinProfileUrl)
        driver.quit()
        return "Linkedin URL is not Present", False
    
    first_name = lead.firstName
    full_name = lead.fullName
    url = lead.linkedinProfileUrl
    company_name = lead.company
    driver.get(url)
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view.pvs-profile-actions__action')))
        button = driver.find_element(By.CSS_SELECTOR, '.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view.pvs-profile-actions__action')
        aria_label = button.get_attribute('aria-label')
        
        if "follow" in aria_label.lower():
            elements = driver.find_elements(By.CSS_SELECTOR, ".artdeco-dropdown__trigger.artdeco-dropdown__trigger--placement-bottom.ember-view.pvs-profile-actions__action.artdeco-button.artdeco-button--secondary.artdeco-button--muted.artdeco-button--2")
            more_button = elements[-1]
            more_button.click()
            time.sleep(1)
            more_elements = driver.find_elements(By.XPATH, "//span[@class='display-flex t-normal flex-1']")
            for element in more_elements:
                if element.text.lower() == "connect":
                    connect_button = element
                    break
            connect_button = connect_button.find_element(By.XPATH, "..")
            print(connect_button.tag_name)
            driver.execute_script("arguments[0].click();", connect_button)
            time.sleep(2)
            add_a_note_button = driver.find_element(By.XPATH, "//button[@aria-label='Add a note']")
            add_a_note_button.click()
            text_area = driver.find_element(By.TAG_NAME, "textarea")
            text_area.send_keys(connection_message.format(first_name, company_name))
            time.sleep(2)
            send_button = driver.find_element(By.XPATH, "//button[@aria-label='Send now']")
            send_button.click()
            time.sleep(2)
        else:
            connect_button = button
            connect_button.click()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'artdeco-button__text')))
            add_a_note_button = driver.find_element(By.XPATH, "//button[@aria-label='Add a note']")
            add_a_note_button.click()
            time.sleep(2)
            text_area = driver.find_element(By.ID, "custom-message")
            print(connection_message)
            text_area.send_keys(connection_message)
            time.sleep(3)
            send_button = driver.find_element(By.XPATH, "//button[@aria-label='Send now']")
            send_button.click()
            time.sleep(2)
    except:
        driver.quit()
        return f"Failed to send connection request to {full_name} due to unforseen reasons", False
    # Close the browser
    driver.quit()
    return f"Successfully sent connection request to {full_name}", True

def download_phantom_buster():
    import time
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.options import Options as ChromeOptions

    download_dir = r'C:\Users\HP\Desktop\HackRx'
    options = ChromeOptions()
    options.add_argument("--headless=new")
    options.add_experimental_option('prefs', {
        'download.default_directory': download_dir,
        'download.prompt_for_download': False,
        'download.directory_upgrade': True,
        'safebrowsing.enabled': True
    })

    driver = webdriver.Chrome(options=options)

    driver.get('https://phantombuster.com/login')

    time.sleep(5)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Email'][@type='email']")))
    email_input = driver.find_element(By.XPATH, "//input[@placeholder='Email'][@type='email']")

    email_input.send_keys("suyashsngh250@gmail.com")


    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Password'][@type='password']")))
    password_input = driver.find_element(By.XPATH, "//input[@placeholder='Password'][@type='password']")

    password_input.send_keys("SuyashSingh@1004")

    password_input.send_keys(Keys.RETURN)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[analyticsid='leadsPageModalCloseBtn']")))
    more_button = driver.find_element(By.CSS_SELECTOR, "[analyticsid='leadsPageModalCloseBtn']")
    more_button.click()

    driver.get("https://phantombuster.com/8715273940022424/phantoms/2650057009673459/console")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")))
    more_button = driver.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
    more_button.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[analyticsval1='results']")))
    more_button = driver.find_element(By.CSS_SELECTOR, "[analyticsval1='results']")
    more_button.click()

    driver.execute_script('window.scrollBy(0, 1000)')

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[analyticsid='agentConsoleMoreButton']")))
    more_button = driver.find_element(By.CSS_SELECTOR, "[analyticsid='agentConsoleMoreButton']")
    more_button.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[analyticsid='agentConsoleDownloadSectionDownloadBtn']")))
    more_button = driver.find_element(By.CSS_SELECTOR, "[analyticsid='agentConsoleDownloadSectionDownloadBtn']")
    more_button.click()

    time.sleep(4)

def lead_score_bard_api(icp, input_csv):
    from bardapi import Bard
    import os 
    os.environ['_BARD_API_KEY']="ZAg5sP8BYFYcPLP3_Xp1lNZ_FLh4db9m_K8d1QRKYubXwqMmuCzefso1al-aqcC7xz6sDw."
    import json
    import pandas as pd

    df = pd.read_csv(input_csv)

    for index, row in df.iterrows():
        if index == 0 and index == 1:
            continue
        row_string = ','.join(row.astype(str))
        input_text = "Summarise the input text I will give you into the following points: "
        for index, (key, value) in enumerate(icp.items()):
            input_text += f"{index}. {key} max-length{len(value) + 2}"

        input_text += f"input text: {row_string} write the out in json format and don't write anything else"

        bard_output = Bard().get_answer(input_text)['content']
        json_string = bard_output.split("json")[1].split("```")[0]
        convert = json.loads(json_string)

        input_text = f"icp={icp} lead_data={convert} from a scale of 1-10 score and compare the data with the icp(Ideal Candidate Profile), give keywords and job function the most priority. write it out in json format. don't write any code use your understanding."
        bard_output = Bard().get_answer(input_text)['content']
        print(bard_output)
        break

def import_leads_from_csv(file_path):
    data = pd.read_csv(file_path)
    data = data.fillna("")
    for index, row in data.iterrows():
        lead_data = row.to_dict()
        lead = Leads(**lead_data)
        lead.save()

class HelloWorldAPI(GenericAPIView):
    @extend_schema(responses={200: None})
    def get(self, request):
        return Response({"message": "Hello, world!"})

class LeadsAPI(GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    serializer_class = LeadsSerializer
    queryset = Leads.objects.all().exclude(state_progress=4)

class MarketingCampaignsAPI(GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    serializer_class = MarketingCampaignsSerializer
    queryset = MarketingCampaigns.objects.all()

    def create(self, request, *args, **kwargs):
        context = {
            'recipient': "HackRx 4.0",
            'offer': "Easy EMI",
            'call_to_action': "Click Now! Limited Time Offer",
            'benefit': "Get 10% off on your first purchase",
            'image_url': "https://scontent-maa2-2.xx.fbcdn.net/v/t1.6435-9/57104038_2300925359929883_1446565781524447232_n.jpg?_nc_cat=101&ccb=1-7&_nc_sid=730e14&_nc_ohc=dP2vICM1_78AX9AyfX2&_nc_ht=scontent-maa2-2.xx&oh=00_AfAhQbcJy1b9rtXqPeljSW6vgLN9iOph1Fy19TJqbW-4mA&oe=64E189AC",
            'offer_url': "http://10.10.220.36:9999/advance_state_progress/?id=42"
        }

        html_string = render_to_string('offer.html', context)

        email = EmailMessage("Bajaj Easy EMI Option", html_string, "shambhavikhare.mahak@gmail.com", ("suyashsingh.stem@gmail.com",))
        email.content_subtype = "html"
        email.send()

        return super().create(request, *args, **kwargs)

class MarketingTemplatesAPI(GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    serializer_class = MarketingTemplatesSerializer
    queryset = MarketingTemplates.objects.all()
    parser_classes = [MultiPartParser]

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
class CreateFakeLeadsSerializer(serializers.Serializer):
    fake_leads = serializers.IntegerField()

class CreateFakeLeads(GenericAPIView):
    serializer_class = CreateFakeLeadsSerializer

    @extend_schema(request=CreateFakeLeadsSerializer, responses={200: None})
    def post(self, request):
        Leads.objects.all().delete()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        fake_leads = serializer.validated_data['fake_leads']
        for i in range(fake_leads):
            lead = generate_fake_lead()
            lead.save()
        return Response({"message": f"{fake_leads} Leads created!"})

class CreateFakeMarketingCampaigns(GenericAPIView):
    @extend_schema(responses={200: None})
    def get(self, request):
        MarketingCampaigns.objects.all().delete()
        social_media = ['LinkedIn', 'Facebook', 'Twitter', 'Gmail']
        
        for i in range(4):
            target, created = Target.objects.get_or_create(target_name=social_media[i].lower())
            campaign = MarketingCampaigns(
                impressions=fake.random_int(min=0, max=10000),
                total_likes=fake.random_int(min=0, max=1000),
                percentage_change=fake.random_int(min=-20, max=20),
                target = target,
                duration=fake.random_int(min=1, max=20),
            )
            campaign.save()
        return Response({"message": f"4 Marketing Campaigns created!"})

class CreateFakeMarketingTemplatesSerializer(serializers.Serializer):
    fake_templates = serializers.IntegerField()

class CreateFakeMarketingTemplates(GenericAPIView):
    serializer_class = CreateFakeMarketingTemplatesSerializer

    @extend_schema(request=CreateFakeMarketingTemplatesSerializer, responses={200: None})
    def post(self, request):
        MarketingTemplates.objects.all().delete()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        fake_templates = serializer.validated_data['fake_templates']
        for i in range(fake_templates):
            template = MarketingTemplates(
                open_rate=fake.random_int(min=0, max=100),
                click_rate=fake.random_int(min=0, max=100),
                reply_rate=fake.random_int(min=0, max=100),
                meeting_rate=fake.random_int(min=0, max=100),
                no_response=fake.random_int(min=0, max=100),
                bounce_rate=fake.random_int(min=0, max=100),
            )
            template.save()
        return Response({"message": f"{fake_templates} Marketing Templates created!"})

class AutomaticLinkedinConnectionRequest(GenericAPIView):
    
    def post(self, request, *args, **kwargs):
        connection_message = request.data.get("connection_message", "Greetings I am Suyash Singh, a final year student and I am interested in exploring full-time employment opportunities at.If there are no current openings, I would appreciate it if you could keep me in mind for future opportunities, could we connect so I can share my resume.")
        lead_id = request.data.get("lead")
        linkedin_email = settings.LINKEDIN_EMAIL
        linkedin_password = settings.LINKEDIN_PASSWORD
        message, successful = send_connection_requests(linkedin_email, linkedin_password, lead_id, connection_message)

        if successful:
            return Response({"status": message})
        return Response({"status": message}, status=400)

from drf_spectacular.utils import extend_schema

class LinkedinProfileScraper(GenericAPIView):

    def post(self, request, *args, **kwargs):
        target_url = request.data.get("target_url", None)
        title = request.data.get("title", None)
        company_name = request.data.get("company_name", None)
        keywords = request.data.get("keywords", None)
        institution = request.data.get("institution", None)
        types_of_services = request.data.get("types_of_services", None)
        age_category = request.data.get("age_category", None)
        industry = request.data.get("industry", None)
        company_size = request.data.get("company_size", None)
        function = request.data.get("function", None)
        time = request.data.get("time", None)
        date = request.data.get("date", None)

        import gspread 

        sa = gspread.service_account(r"C:\Users\HP\Desktop\HackRx\service_account.json")
        sh = sa.open("Leads Webscraper")

        wks = sh.worksheet("Sheet1")

        # Define the data to be written
        data = [target_url, title, company_name, keywords, institution, types_of_services, age_category, industry, company_size, function, time, date]

        # Write the data to the sheet
        row_index = 2
        for value in data:
            print("value", value)
            if value is not None and value != "":
                wks.update_cell(row_index, 1, value)
                row_index += 1
        
        time.sleep(10)

        state = State.objects.all().count()
        if state == 0:
            state = State.objects.create(state=3)
        else:
            state = State.objects.all().first()

        if "ceo" in keywords.lower():
            file_path = r"C:\Users\HP\Desktop\HackRx\output_1.csv"

            state.state = 1
            state.save(update_fields=['state'])
            # df = pd.read_csv()

            # #Call the Student Resource Model and make its instance
            # lead_resource = LeadsResource()
            
            # # Load the pandas dataframe into a tablib dataset
            # dataset = Dataset().load(df)
            
            # # Call the import_data hook and pass the tablib dataset
            # result = lead_resource.import_data(dataset,\
            #     dry_run=True, raise_errors = True)

            # if not result.has_errors():
            #     result = lead_resource.import_data(dataset, dry_run=False)
            try:
                import_leads_from_csv(file_path)
                return HttpResponseRedirect("http://10.10.220.36:9999/data-enrich/")
            except:
                return Response({"status": "Not Imported Scraper"},\
                        status=status.HTTP_400_BAD_REQUEST)

        if "insurance" in keywords.lower():
            file_path = r"C:\Users\HP\Desktop\HackRx\output_2.csv"

            state.state = 2
            state.save(update_fields=['state'])
            # df = pd.read_csv()

            # #Call the Student Resource Model and make its instance
            # lead_resource = LeadsResource()
            
            # # Load the pandas dataframe into a tablib dataset
            # dataset = Dataset().load(df)
            
            # # Call the import_data hook and pass the tablib dataset
            # result = lead_resource.import_data(dataset,\
            #     dry_run=True, raise_errors = True)

            # if not result.has_errors():
            #     result = lead_resource.import_data(dataset, dry_run=False)
            #     return Response({"status": "Scraper successfully ran"})

            # return Response({"status": "Not Imported Scraper"},\
            #         status=status.HTTP_400_BAD_REQUEST)
            try:
                import_leads_from_csv(file_path)
                return HttpResponseRedirect("http://10.10.220.36:9999/data-enrich/")
            except ZeroDivisionError:
                return Response({"status": "Not Imported Scraper"},\
                        status=status.HTTP_400_BAD_REQUEST)
        
        elif "bajaj" in company_name.lower() or "bajaj" in keywords.lower():
            file_path = r"C:\Users\HP\Desktop\HackRx\output_3.csv"

            state.state = 3
            state.save(update_fields=['state'])
            # df = pd.read_csv(r"C:\Users\HP\Desktop\HackRx\output_3.csv")

            # #Call the Student Resource Model and make its instance
            # lead_resource = LeadsResource()
            
            # # Load the pandas dataframe into a tablib dataset
            # dataset = Dataset().load(df)
            
            # # Call the import_data hook and pass the tablib dataset
            # result = lead_resource.import_data(dataset,\
            #     dry_run=True, raise_errors = True)

            try:
                import_leads_from_csv(file_path)
                return HttpResponseRedirect("http://10.10.220.36:9999/data-enrich/")
            except:
                return Response({"status": "Not Imported Scraper"},\
                        status=status.HTTP_400_BAD_REQUEST)
        else:
            import requests

            url = "https://api.phantombuster.com/api/v2/agents/launch"

            payload = { "id": "3665147201408784" }
            headers = {
                "content-type": "application/json",
                "X-Phantombuster-Key": "qmzQ6aDMhSXGkvjncuxIHNsIJvs1DRPStysXCWsZcSM"
            }

            requests.post(url, json=payload, headers=headers)

            download_phantom_buster()

class AdvanceStateProgressAPI(GenericAPIView):
    
    def get(self, request, *args, **kwargs):
        id = self.request.query_params["id"]
        Leads.objects.filter(id=id).update(state_progress=2)
        return redirect('https://www.bajajfinserv.in/webform/emicard/login?utm_source=googlesearch_mktg&utm_medium=cpc&utm_campaign=wpb_iemi_190723_insta_emi_search_tof_jan07_148030749114_apply%20bajaj%20emi%20card&gclid=Cj0KCQjw2eilBhCCARIsAG0Pf8sXSzIJZQ938ktv0bX7aNvUNQRg0RsgXcJcOpYEL-7TS1hufcLE99gaAl_EEALw_wcB')
    
class EnrichLeads(GenericAPIView):

    def get(self, request, *args, **kwargs):
        # Read the CSV file using pandas

        state = State.objects.all().first()

        df = pd.read_csv(rf"C:\Users\HP\Desktop\HackRx\data_enrichment_{state.state}.csv")

        # Iterate through the rows of the DataFrame and save the data to Django models
        for index, row in df.iterrows():
            obj, created = DetailedLeads.objects.get_or_create(
                linkedinProfileUrl=row['linkedinProfileUrl'],
                email=row['email'],
                linkedinProfile=row['linkedinProfile'],
                headline=row['headline'],
                location=row['location'],
                imgUrl=row['imgUrl'],
                firstName=row['firstName'],
                lastName=row['lastName'],
                fullName=row['fullName'],
                subscribers=row['subscribers'],
                connectionDegree=row['connectionDegree'],
                vmid=row['vmid'],
                userId=row['userId'],
                linkedinSalesNavigatorUrl=row['linkedinSalesNavigatorUrl'],
                connectionsCount=row['connectionsCount'],
                connectionsUrl=row['connectionsUrl'],
                mutualConnectionsUrl=row['mutualConnectionsUrl'],
                mutualConnectionsText=row['mutualConnectionsText'],
                company=row['company'],
                companyUrl=row['companyUrl'],
                jobTitle=row['jobTitle'],
                jobDescription=row['jobDescription'],
                jobLocation=row['jobLocation'],
                jobDateRange=row['jobDateRange'],
                jobDuration=row['jobDuration'],
                company2=row['company2'],
                companyUrl2=row['companyUrl2'],
                jobTitle2=row['jobTitle2'],
                jobDescription2=row['jobDescription2'],
                jobLocation2=row['jobLocation2'],
                jobDateRange2=row['jobDateRange2'],
                jobDuration2=row['jobDuration2'],
                school=row['school'],
                schoolUrl=row['schoolUrl'],
                schoolDegree=row['schoolDegree'],
                schoolDateRange=row['schoolDateRange'],
                school2=row['school2'],
                schoolDegree2=row['schoolDegree2'],
                schoolDateRange2=row['schoolDateRange2'],
                civilityFromDropContact=row['civilityFromDropContact'],
                websiteFromDropContact=row['websiteFromDropContact'],
                companyWebsite=row['companyWebsite'],
                allSkills=row['allSkills'],
                skill1=row['skill1'],
                endorsement1=row['endorsement1'],
                skill2=row['skill2'],
                endorsement2=row['endorsement2'],
                skill3=row['skill3'],
                endorsement3=row['endorsement3'],
                skill4=row['skill4'],
                endorsement4=row['endorsement4'],
                skill5=row['skill5'],
                endorsement5=row['endorsement5'],
                skill6=row['skill6'],
                endorsement6=row['endorsement6'],
                baseUrl=row['baseUrl'],
                profileId=row['profileId'],
                timestamp=row['timestamp'],
                description=row['description'],
                schoolUrl2=row['schoolUrl2'],
                website=row['website'],
                birthday=row['birthday'],
                mail=row['mail'],
                schoolDescription=row['schoolDescription'],
                twitter=row['twitter'],
                twitterProfileUrl=row['twitterProfileUrl'],
                mailFromDropcontact=row['mailFromDropcontact'],
                qualificationFromDropContact=row['qualificationFromDropContact'],
            )
            # lead = Leads.objects.filter(Q(profileUrl = row['linkedinProfileUrl']) | Q(email = row['email']) | Q(fullName = row['fullName']))
            leads = Leads.objects.all()
            mx = (0, 0)
            for idx, lead in enumerate(leads):
                similarity_score = similarity(lead.profileUrl,  row['linkedinProfileUrl'])
                if similarity_score > mx[0] and similarity_score >= 0.8:
                    mx = (similarity_score, idx)
            lead = leads[mx[1]]
            lead.detailed_lead = obj
            lead.save(update_fields=['detailed_lead'])
            # if lead.exists():
            #     lead = lead.last()
            #     lead.detailed_lead = obj
            #     lead.save(update_fields=['detailed_lead'])
        
        return Response({"status": "Leads Enriched"})
            

class DeleteAllLeads(GenericAPIView):

    def get(self, request, *args, **kwargs):
        Leads.objects.all().delete()
        return Response({"status": "All Leads Deleted"})

from django.http import HttpResponse
# from hackrx.admin import DetailedLeadsResourceAdmin

from import_export import resources

class DetailedLeadsResourceAdmin(resources.ModelResource):
    class Meta:
        model = DetailedLeads

class LeadsResourceAdmin(resources.ModelResource):
    class Meta:
        model = Leads


def export(request):
    person_resource = DetailedLeadsResourceAdmin()
    dataset = person_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="result_2.csv"'

    # person_resource = LeadsResourceAdmin()
    # dataset = person_resource.export()
    # response = HttpResponse(dataset.csv, content_type='text/csv')
    # response['Content-Disposition'] = 'attachment; filename="data_enrichment_2.csv"'
    return response