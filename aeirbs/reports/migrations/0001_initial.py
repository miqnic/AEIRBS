# Generated by Django 2.2.6 on 2020-05-27 17:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import reports.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('components', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incident_type', models.CharField(choices=[('FIRE', 'FR'), ('FLOOD', 'FL'), ('EARTHQUAKE', 'EQ'), ('FIRE_FLOOD', 'FR_FL'), ('FIRE_EARTHQUAKE', 'FR_EQ'), ('FLOOD_EARTHQUAKE', 'FL_EQ'), ('FIRE_FLOOD_EARTHQUAKE', 'FR_FL_EQ')], default=reports.utils.IncidentCombinations('FIRE'), max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='TemporaryImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp_image', models.ImageField(upload_to='temp_image')),
            ],
        ),
        migrations.CreateModel(
            name='IncidentReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incident_date_time', models.DateTimeField(auto_now_add=True)),
                ('incident_level', models.CharField(choices=[('FR_FIRST', 'FR_FIRST'), ('FR_SECOND', 'FR_SECOND'), ('FR_THIRD', 'FR_THIRD'), ('FR_FOURTH', 'FR_FOURTH'), ('FR_FIFTH', 'FR_FIFTH'), ('FR_TFALPHA', 'FR_TFALPHA'), ('FR_TFBRAVO', 'FR_TFBRAVO'), ('FR_TFCHARLIE', 'FR_TFCHARLIE'), ('FR_TFDELTA', 'FR_TFDELTA'), ('FR_TFECHO', 'FR_TFECHO'), ('FR_GENERAL', 'FR_GENERAL'), ('FL_FIRST', 'FL_GUTTER'), ('FL_HALFKNEE', 'FL_HALFKNEE'), ('FL_HALFTIRE', 'FL_HALFTIRE'), ('FL_KNEE', 'FL_KNEE'), ('FL_TIRES', 'FL_TIRES'), ('FL_WAIST', 'FL_WAIST'), ('FL_CHEST', 'FL_CHEST'), ('EQ_I', 'EQ_I'), ('EQ_II', 'EQ_II'), ('EQ_III', 'EQ_III'), ('EQ_IV', 'EQ_IV'), ('EQ_V', 'EQ_V'), ('EQ_VI', 'EQ_VI'), ('EQ_VII', 'EQ_VII'), ('EQ_VIII', 'EQ_VIII'), ('EQ_IX', 'EQ_IX'), ('EQ_X', 'EQ_X')], default=reports.utils.IncidentLevels('FR_FIRST'), max_length=20)),
                ('device_sensor_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='components.Device_Sensor')),
                ('incident_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='reports.Incident')),
            ],
        ),
        migrations.CreateModel(
            name='AuditLogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_id', models.CharField(max_length=15, unique=True)),
                ('activity', models.CharField(max_length=100)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('audit_details', models.CharField(default='details', max_length=100)),
                ('audit_type', models.IntegerField(choices=[(0, 'Component Logs'), (1, 'User Logs'), (2, 'Maintenance Logs')])),
                ('audit_isDeleted', models.BooleanField(default=False)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
