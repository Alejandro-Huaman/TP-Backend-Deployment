# Generated by Django 4.1.6 on 2023-08-28 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("linkedinJobs", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicallinkedinjobs",
            name="posibilityPercentage",
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name="linkedinjobs",
            name="posibilityPercentage",
            field=models.FloatField(),
        ),
    ]
