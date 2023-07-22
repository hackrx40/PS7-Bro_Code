from django.contrib import admin

# Register your models here.

from .models import Leads, MarketingCampaigns, MarketingTemplates, Target, State, DetailedLeads

admin.site.register(Leads)
admin.site.register(MarketingCampaigns)
admin.site.register(MarketingTemplates)
admin.site.register(Target)
admin.site.register(State)
admin.site.register(DetailedLeads)