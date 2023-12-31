# Generated by Django 4.1.3 on 2023-06-04 21:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('typetest', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='State')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Created Date')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Update Date')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Deleted Date')),
                ('testname', models.CharField(max_length=30)),
                ('testdescription', models.TextField()),
                ('typetest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='typetest.typetest')),
            ],
            options={
                'verbose_name': 'Test',
                'verbose_name_plural': 'Tests',
            },
        ),
        migrations.CreateModel(
            name='HistoricalTest',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='State')),
                ('created_date', models.DateField(blank=True, editable=False, verbose_name='Created Date')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Update Date')),
                ('deleted_date', models.DateField(blank=True, editable=False, verbose_name='Deleted Date')),
                ('testname', models.CharField(max_length=30)),
                ('testdescription', models.TextField()),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('typetest', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='typetest.typetest')),
            ],
            options={
                'verbose_name': 'historical Test',
                'verbose_name_plural': 'historical Tests',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
