# Generated by Django 4.1.3 on 2023-06-20 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalquestion',
            name='questionname',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='questionname',
            field=models.CharField(max_length=200),
        ),
    ]
