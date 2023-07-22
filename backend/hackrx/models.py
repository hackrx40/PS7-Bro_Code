from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class State(models.Model):
    state = models.IntegerField(default=1)

class Leads(models.Model):
    profileUrl = models.URLField(default="", blank= True)
    fullName = models.CharField(max_length=300, default="", blank=True)
    firstName = models.CharField(max_length=300, default="", blank=True)
    lastName = models.CharField(max_length=300, default="", blank=True)
    profileImageUrl = models.URLField(default="", blank=True)
    currentJob = models.CharField(max_length=300, default="", blank=True)
    connectionDegree = models.CharField(max_length=300, default="", blank=True)
    job = models.CharField(max_length=300, default="",blank=True)
    location = models.CharField(max_length=300, default="", blank=True)
    sharedConnections = models.CharField(max_length=300, default="", blank=True)
    url = models.URLField(max_length=300,default="", blank=True)
    name = models.CharField(max_length=300, default="", blank=True)
    query = models.CharField(max_length=300, default="", blank=True)
    category = models.CharField(max_length=300, default="", blank=True)
    timestamp = models.CharField(max_length=300, default="", blank=True)
    additionalInfo = models.TextField(default="", blank=True)
    pastJob = models.CharField(max_length=300, default="", blank=True)
    email = models.EmailField(max_length=254, default="", blank=True)
    facebookUrl = models.URLField(default="", blank=True)
    twitterUrl = models.URLField(default="", blank=True)

    state_progress = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(4),
            MinValueValidator(1)
        ]
    )
    detailed_lead = models.OneToOneField("DetailedLeads", on_delete=models.CASCADE, blank=True, null=True)
    lead_score = models.CharField(default="", max_length=100, blank=True)
    def __str__(self) -> str:
        return f"{self.name} ({self.email})"

class DetailedLeads(models.Model):
    linkedinProfileUrl = models.CharField(max_length=200, default="", blank=True)
    email = models.CharField(max_length=100, default="", blank=True)
    linkedinProfile = models.CharField(max_length=200, default="", blank=True)
    headline = models.CharField(max_length=200, default="", blank=True)
    location = models.CharField(max_length=100, default="", blank=True)
    imgUrl = models.CharField(max_length=200, default="", blank=True)
    firstName = models.CharField(max_length=100, default="", blank=True)
    lastName = models.CharField(max_length=100, default="", blank=True)
    fullName = models.CharField(max_length=200, default="", blank=True)
    subscribers = models.CharField(max_length=50, default="", blank=True)
    connectionDegree = models.CharField(max_length=50, default="", blank=True)
    vmid = models.CharField(max_length=100, default="", blank=True)
    userId = models.CharField(max_length=100, default="", blank=True)
    linkedinSalesNavigatorUrl = models.CharField(max_length=200, default="", blank=True)
    connectionsCount = models.CharField(max_length=50, default="", blank=True)
    connectionsUrl = models.CharField(max_length=200, default="", blank=True)
    mutualConnectionsUrl = models.CharField(max_length=200, default="", blank=True)
    mutualConnectionsText = models.CharField(max_length=200, default="", blank=True)
    company = models.CharField(max_length=200, default="", blank=True)
    companyUrl = models.CharField(max_length=200, default="", blank=True)
    jobTitle = models.CharField(max_length=200, default="", blank=True)
    jobDescription = models.CharField(max_length=500, default="", blank=True)
    jobLocation = models.CharField(max_length=200, default="", blank=True)
    jobDateRange = models.CharField(max_length=100, default="", blank=True)
    jobDuration = models.CharField(max_length=100, default="", blank=True)
    company2 = models.CharField(max_length=200, default="", blank=True)
    companyUrl2 = models.CharField(max_length=200, default="", blank=True)
    jobTitle2 = models.CharField(max_length=200, default="", blank=True)
    jobDescription2 = models.CharField(max_length=500, default="", blank=True)
    jobLocation2 = models.CharField(max_length=200, default="", blank=True)
    jobDateRange2 = models.CharField(max_length=100, default="", blank=True)
    jobDuration2 = models.CharField(max_length=100, default="", blank=True)
    school = models.CharField(max_length=200, default="", blank=True)
    schoolUrl = models.CharField(max_length=200, default="", blank=True)
    schoolDegree = models.CharField(max_length=200, default="", blank=True)
    schoolDateRange = models.CharField(max_length=100, default="", blank=True)
    school2 = models.CharField(max_length=200, default="", blank=True)
    schoolDegree2 = models.CharField(max_length=200, default="", blank=True)
    schoolDateRange2 = models.CharField(max_length=100, default="", blank=True)
    civilityFromDropContact = models.CharField(max_length=50, default="", blank=True)
    websiteFromDropContact = models.CharField(max_length=200, default="", blank=True)
    companyWebsite = models.CharField(max_length=200, default="", blank=True)
    allSkills = models.CharField(max_length=500, default="", blank=True)
    skill1 = models.CharField(max_length=100, default="", blank=True)
    endorsement1 = models.CharField(max_length=50, default="", blank=True)
    skill2 = models.CharField(max_length=100, default="", blank=True)
    endorsement2 = models.CharField(max_length=50, default="", blank=True)
    skill3 = models.CharField(max_length=100, default="", blank=True)
    endorsement3 = models.CharField(max_length=50, default="", blank=True)
    skill4 = models.CharField(max_length=100, default="", blank=True)
    endorsement4 = models.CharField(max_length=50, default="", blank=True)
    skill5 = models.CharField(max_length=100, default="", blank=True)
    endorsement5 = models.CharField(max_length=50, default="", blank=True)
    skill6 = models.CharField(max_length=100, default="", blank=True)
    endorsement6 = models.CharField(max_length=50, default="", blank=True)
    baseUrl = models.CharField(max_length=200, default="", blank=True)
    profileId = models.CharField(max_length=100, default="", blank=True)
    timestamp = models.CharField(max_length=100, default="", blank=True)
    description = models.CharField(max_length=500, default="", blank=True)
    schoolUrl2 = models.CharField(max_length=200, default="", blank=True)
    website = models.CharField(max_length=200, default="", blank=True)
    birthday = models.CharField(max_length=100, default="", blank=True)
    mail = models.CharField(max_length=100, default="", blank=True)
    schoolDescription = models.CharField(max_length=500, default="", blank=True)
    twitter = models.CharField(max_length=200, default="", blank=True)
    twitterProfileUrl = models.CharField(max_length=200, default="", blank=True)
    mailFromDropcontact = models.CharField(max_length=100, default="", blank=True)
    qualificationFromDropContact = models.CharField(max_length=100, default="", blank=True)

    def __str__(self):
        return self.fullName

def get_logo(target_name):
        if target_name.lower() == 'linkedin':
            return "https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/LinkedIn_icon.svg/768px-LinkedIn_icon.svg.png"
        elif target_name.lower() == 'facebook':
            return "https://upload.wikimedia.org/wikipedia/en/thumb/0/04/Facebook_f_logo_%282021%29.svg/768px-Facebook_f_logo_%282021%29.svg.png"
        elif target_name.lower() == 'twitter':
            return "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Logo_of_Twitter.svg/934px-Logo_of_Twitter.svg.png"
        elif target_name.lower() == 'gmail':
            return "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Gmail_icon_%282020%29.svg/640px-Gmail_icon_%282020%29.svg.png"
        return "https://hackrx.in/png/head.png"

class Target(models.Model):
    target_name = models.CharField(max_length=100, default="")
    logo = models.URLField(max_length=300, default="")

    def save(self, *args, **kwargs):
        self.logo = get_logo(self.target_name.lower())
        super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.target_name


class MarketingCampaigns(models.Model):
    impressions = models.CharField(max_length=100, default="")
    total_likes = models.CharField(max_length=100, default="")
    percentage_change = models.CharField(max_length=100, default="")
    target = models.ForeignKey(Target, on_delete=models.CASCADE, default="")
    duration = models.CharField(max_length=100, default="")
    templates = models.ForeignKey('MarketingTemplates', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.target} Campaign"

class MarketingTemplates(models.Model):
    template_name = models.CharField(max_length=100, default="")
    open_rate = models.CharField(max_length=100, default="")
    click_rate = models.CharField(max_length=100, default="")
    reply_rate = models.CharField(max_length=100, default="")
    meeting_rate = models.CharField(max_length=100, default="")
    no_response = models.CharField(max_length=100, default="")
    bounce_rate = models.CharField(max_length=100, default="")

    def __str__(self) -> str:
        return f"Template {self.id}"

