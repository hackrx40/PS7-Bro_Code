from django.urls import path
from .views import *
from django.views.generic import TemplateView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from rest_framework import routers

router = routers.SimpleRouter()
# convert the follwing url to router
# path('leads/', LeadsAPI.as_view(), name='leads'),
# path('campaigns/', MarketingCampaignsAPI.as_view(), name='campaigns'),
# path('campaign-template/', MarketingTemplatesAPI.as_view(), name='campaign-template'),

router.register(r'leads', LeadsAPI, basename='leads')
router.register(r'campaigns', MarketingCampaignsAPI, basename='campaigns')
router.register(r'campaign-template', MarketingTemplatesAPI, basename='campaign-template')

urlpatterns = [
    path('', HelloWorldAPI.as_view(), name='index'),
    path('connection-request/', AutomaticLinkedinConnectionRequest.as_view(), name='connection-request'),
    path('scraper/', LinkedinProfileScraper.as_view(), name='scraper'),
    path("advance_state_progress/", AdvanceStateProgressAPI.as_view(), name="advance_state_progress"),
    path('create-fake-leads/', CreateFakeLeads.as_view(), name='create-fake-leads'),
    path('create-fake-marketing-campaigns/', CreateFakeMarketingCampaigns.as_view(), name='create-fake-campaigns'),
    path('create-fake-marketing-template/', CreateFakeMarketingTemplates.as_view(), name='create-fake-marketing-template'),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("schema/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="schema-docs"),
    path("delete-leads/", DeleteAllLeads.as_view(), name="delete-all-leads"),
    path("data-enrich/", EnrichLeads.as_view(), name="data-enrich"),
    # path("export/",export,name="export")
]

urlpatterns += router.urls