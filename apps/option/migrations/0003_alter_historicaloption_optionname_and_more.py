# Generated by Django 4.1.6 on 2023-09-08 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("option", "0002_alter_historicaloption_optionname_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicaloption",
            name="optionname",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="option",
            name="optionname",
            field=models.TextField(),
        ),
    ]
