# Generated by Django 4.2.3 on 2023-07-21 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackrx', '0004_detailedleads_leads_detailed_lead'),
    ]

    operations = [
        migrations.AddField(
            model_name='leads',
            name='state',
            field=models.IntegerField(default=1),
        ),
    ]
