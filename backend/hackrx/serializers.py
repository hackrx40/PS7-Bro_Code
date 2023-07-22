from rest_framework.serializers import *
from .models import *
from rest_framework.exceptions import *
from django.core.files.base import ContentFile
import base64

class DetailedLeadsSerializer(ModelSerializer):
    class Meta:
        model = DetailedLeads
        fields = "__all__"

class LeadsSerializer(ModelSerializer):
    detailed_leads = SerializerMethodField()
    class Meta:
        model = Leads
        fields = ['id', 'profileUrl', 'fullName', 'firstName', 'lastName', 'profileImageUrl', 'currentJob', 'connectionDegree', 'job', 'location', 'sharedConnections', 'url', 'name', 'query', 'category', 'timestamp', 'additionalInfo', 'pastJob', 'detailed_leads', "state_progress", "lead_score", "email"]

    def get_detailed_leads(self, obj):
        return DetailedLeadsSerializer(obj.detailed_lead).data

class TargetSerializer(ModelSerializer):
    class Meta:
        model = Target
        fields = "__all__"

        extra_kwargs = {
            "logo": {"required": False}
        }

class MarketingTemplatesSerializer(ModelSerializer):
    class Meta:
        model = MarketingTemplates
        fields = "__all__"
        extra_kwargs = {
            "target": {"required": False}
        }
    
    def create(self, validated_data):
        validated_data["template_html"] = self.initial_data["file"].read()
        return super().create(validated_data)

class MarketingCampaignsSerializer(ModelSerializer):
    target = TargetSerializer(required=False)
    marketing_templates = SerializerMethodField()
    class Meta:
        model = MarketingCampaigns
        fields = ['id', 'impressions', 'total_likes', 'percentage_change', 'target', 'duration', 'marketing_templates', "templates"]
    
    def create(self, validated_data):
        try:
            target = validated_data.pop("target")
            target, created = Target.objects.get_or_create(**target)
        except:
            target = Target.objects.get(target_name="gmail")
        validated_data["target"] = target
        template_name = self.initial_data["template_name"]
        template = MarketingTemplates.objects.get(template_name=template_name)
        validated_data["templates"] = template
        instance = MarketingCampaigns.objects.create(**validated_data)
        return instance


    def get_marketing_templates(self, obj):
        return MarketingTemplatesSerializer(MarketingTemplates.objects.all(), many=True).data
    

from import_export import resources

class LeadsResource(resources.ModelResource):

    class Meta:
        model = Leads
        import_id_fields = ["profileUrl"]
        skip_unchanged = True
        use_bulk = True
    
class DetailedLeadsResource(resources.ModelResource):

    class Meta: 
        models = DetailedLeads
        import_id_fields =  ['linkedinProfileUrl']
        fields = ['linkedinProfileUrl', 'email', 'linkedinProfile', 'headline', 'location', 'imgUrl', 'firstName', 'lastName', 'fullName', 'subscribers', 'connectionDegree', 'vmid', 'userId', 'linkedinSalesNavigatorUrl', 'connectionsCount', 'connectionsUrl', 'mutualConnectionsUrl', 'mutualConnectionsText', 'company', 'companyUrl', 'jobTitle', 'jobDescription', 'jobLocation', 'jobDateRange', 'jobDuration', 'company2', 'companyUrl2', 'jobTitle2', 'jobDescription2', 'jobLocation2', 'jobDateRange2', 'jobDuration2', 'school', 'schoolUrl', 'schoolDegree', 'schoolDateRange', 'school2', 'schoolDegree2', 'schoolDateRange2', 'civilityFromDropContact', 'websiteFromDropContact', 'companyWebsite', 'allSkills', 'skill1', 'endorsement1', 'skill2', 'endorsement2', 'skill3', 'endorsement3', 'skill4', 'endorsement4', 'skill5', 'endorsement5', 'skill6', 'endorsement6', 'baseUrl', 'profileId', 'timestamp', 'description', 'schoolUrl2', 'website', 'birthday', 'mail', 'schoolDescription', 'twitter', 'twitterProfileUrl', 'mailFromDropcontact', 'qualificationFromDropContact']
        skip_unchanged = True
        use_bulk = True