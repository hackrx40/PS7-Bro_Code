from django.urls import path
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()

router.register(r'leads', LeadsAPI, basename='leads')
router.register(r'campaigns', MarketingCampaignsAPI, basename='campaigns')

urlpatterns = [
    path("", index, name="index")
]