# Generated by Django 4.1.6 on 2023-08-28 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "linkedinJobs",
            "0003_alter_historicallinkedinjobs_posibilitypercentage_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="historicallinkedinjobs",
            name="jobCompany",
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name="historicallinkedinjobs",
            name="jobDate",
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name="historicallinkedinjobs",
            name="jobLocation",
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name="linkedinjobs",
            name="jobCompany",
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name="linkedinjobs",
            name="jobDate",
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name="linkedinjobs",
            name="jobLocation",
            field=models.CharField(default=None, max_length=100),
        ),
    ]
