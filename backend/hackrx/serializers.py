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

class MarketingTemplatesSerializer(ModelSerializer):
    class Meta:
        model = MarketingTemplates
        fields = "__all__"
    
    def create(self, validated_data):
        validated_data["template_html"] = self.initial_data["file"].read()
        return super().create(validated_data)

class MarketingCampaignsSerializer(ModelSerializer):
    target = TargetSerializer()
    marketing_templates = SerializerMethodField()
    class Meta:
        model = MarketingCampaigns
        fields = ['id', 'impressions', 'total_likes', 'percentage_change', 'target', 'duration', 'marketing_templates', "templates"]
    
    def create(self, validated_data):
        target = validated_data.pop("target")
        try:
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