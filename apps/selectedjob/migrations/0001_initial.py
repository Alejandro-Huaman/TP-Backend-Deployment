# Generated by Django 4.2.1 on 2023-09-09 22:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('linkedinJobs', '0004_historicallinkedinjobs_jobcompany_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SelectedJob',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='State')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Created Date')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Update Date')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Deleted Date')),
                ('register', models.DateField(auto_now_add=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='linkedinJobs.linkedinjobs')),
            ],
            options={
                'verbose_name': 'SelectedJob',
                'verbose_name_plural': 'SelectedJobs',
            },
        ),
        migrations.CreateModel(
            name='HistoricalSelectedJob',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='State')),
                ('created_date', models.DateField(blank=True, editable=False, verbose_name='Created Date')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Update Date')),
                ('deleted_date', models.DateField(blank=True, editable=False, verbose_name='Deleted Date')),
                ('register', models.DateField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('job', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='linkedinJobs.linkedinjobs')),
            ],
            options={
                'verbose_name': 'historical SelectedJob',
                'verbose_name_plural': 'historical SelectedJobs',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
