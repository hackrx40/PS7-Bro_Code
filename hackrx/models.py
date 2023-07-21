from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Leads(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    industry = models.CharField(max_length=100, blank=True, null=True)
    company_size = models.CharField(max_length=100, blank=True, null=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    function = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    company_names = models.CharField(max_length=100, blank=True, null=True)
    keywords = models.CharField(max_length=200, blank=True, null=True)
    institute = models.CharField(max_length=200, blank=True, null=True)
    linkedin = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    lead_score = models.CharField(max_length=100, blank=True, null=True)
    state_progress = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(4),
            MinValueValidator(1)
        ],
        blank=True, null=True
    )

    def __str__(self) -> str:
        return f"{self.name} ({self.email})"

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
    target_name = models.CharField(max_length=100, blank=True, null=True)
    logo = models.URLField(max_length=300, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.logo = get_logo(self.target_name.lower())
        super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.target_name


class MarketingCampaigns(models.Model):
    impressions = models.CharField(max_length=100, blank=True, null=True)
    total_likes = models.CharField(max_length=100, blank=True, null=True)
    percentage_change = models.CharField(max_length=100, blank=True, null=True)
    target = models.ForeignKey(Target, on_delete=models.CASCADE, blank=True, null=True)
    duration = models.CharField(max_length=100, blank=True, null=True)
    templates = models.ForeignKey('MarketingTemplates', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.target} Campaign"

class MarketingTemplates(models.Model):
    template_name = models.CharField(max_length=100, blank=True, null=True)
    template_html = models.BinaryField(blank=True, null=True)
    open_rate = models.CharField(max_length=100, blank=True, null=True)
    click_rate = models.CharField(max_length=100, blank=True, null=True)
    reply_rate = models.CharField(max_length=100, blank=True, null=True)
    meeting_rate = models.CharField(max_length=100, blank=True, null=True)
    no_response = models.CharField(max_length=100, blank=True, null=True)
    bounce_rate = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self) -> str:
        return f"Template {self.id}"

