# Generated by Django 4.2.3 on 2023-07-21 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hackrx', '0003_alter_leads_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetailedLeads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linkedinProfileUrl', models.CharField(default='', max_length=200)),
                ('email', models.CharField(default='', max_length=100)),
                ('linkedinProfile', models.CharField(default='', max_length=200)),
                ('headline', models.CharField(default='', max_length=200)),
                ('location', models.CharField(default='', max_length=100)),
                ('imgUrl', models.CharField(default='', max_length=200)),
                ('firstName', models.CharField(default='', max_length=100)),
                ('lastName', models.CharField(default='', max_length=100)),
                ('fullName', models.CharField(default='', max_length=200)),
                ('subscribers', models.CharField(default='', max_length=50)),
                ('connectionDegree', models.CharField(default='', max_length=50)),
                ('vmid', models.CharField(default='', max_length=100)),
                ('userId', models.CharField(default='', max_length=100)),
                ('linkedinSalesNavigatorUrl', models.CharField(default='', max_length=200)),
                ('connectionsCount', models.CharField(default='', max_length=50)),
                ('connectionsUrl', models.CharField(default='', max_length=200)),
                ('mutualConnectionsUrl', models.CharField(default='', max_length=200)),
                ('mutualConnectionsText', models.CharField(default='', max_length=200)),
                ('company', models.CharField(default='', max_length=200)),
                ('companyUrl', models.CharField(default='', max_length=200)),
                ('jobTitle', models.CharField(default='', max_length=200)),
                ('jobDescription', models.CharField(default='', max_length=500)),
                ('jobLocation', models.CharField(default='', max_length=200)),
                ('jobDateRange', models.CharField(default='', max_length=100)),
                ('jobDuration', models.CharField(default='', max_length=100)),
                ('company2', models.CharField(default='', max_length=200)),
                ('companyUrl2', models.CharField(default='', max_length=200)),
                ('jobTitle2', models.CharField(default='', max_length=200)),
                ('jobDescription2', models.CharField(default='', max_length=500)),
                ('jobLocation2', models.CharField(default='', max_length=200)),
                ('jobDateRange2', models.CharField(default='', max_length=100)),
                ('jobDuration2', models.CharField(default='', max_length=100)),
                ('school', models.CharField(default='', max_length=200)),
                ('schoolUrl', models.CharField(default='', max_length=200)),
                ('schoolDegree', models.CharField(default='', max_length=200)),
                ('schoolDateRange', models.CharField(default='', max_length=100)),
                ('school2', models.CharField(default='', max_length=200)),
                ('schoolDegree2', models.CharField(default='', max_length=200)),
                ('schoolDateRange2', models.CharField(default='', max_length=100)),
                ('civilityFromDropContact', models.CharField(default='', max_length=50)),
                ('websiteFromDropContact', models.CharField(default='', max_length=200)),
                ('companyWebsite', models.CharField(default='', max_length=200)),
                ('allSkills', models.CharField(default='', max_length=500)),
                ('skill1', models.CharField(default='', max_length=100)),
                ('endorsement1', models.CharField(default='', max_length=50)),
                ('skill2', models.CharField(default='', max_length=100)),
                ('endorsement2', models.CharField(default='', max_length=50)),
                ('skill3', models.CharField(default='', max_length=100)),
                ('endorsement3', models.CharField(default='', max_length=50)),
                ('skill4', models.CharField(default='', max_length=100)),
                ('endorsement4', models.CharField(default='', max_length=50)),
                ('skill5', models.CharField(default='', max_length=100)),
                ('endorsement5', models.CharField(default='', max_length=50)),
                ('skill6', models.CharField(default='', max_length=100)),
                ('endorsement6', models.CharField(default='', max_length=50)),
                ('baseUrl', models.CharField(default='', max_length=200)),
                ('profileId', models.CharField(default='', max_length=100)),
                ('timestamp', models.CharField(default='', max_length=100)),
                ('description', models.CharField(default='', max_length=500)),
                ('schoolUrl2', models.CharField(default='', max_length=200)),
                ('website', models.CharField(default='', max_length=200)),
                ('birthday', models.CharField(default='', max_length=100)),
                ('mail', models.CharField(default='', max_length=100)),
                ('schoolDescription', models.CharField(default='', max_length=500)),
                ('twitter', models.CharField(default='', max_length=200)),
                ('twitterProfileUrl', models.CharField(default='', max_length=200)),
                ('mailFromDropcontact', models.CharField(default='', max_length=100)),
                ('qualificationFromDropContact', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='leads',
            name='detailed_lead',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hackrx.detailedleads'),
        ),
    ]
