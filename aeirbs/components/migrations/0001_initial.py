# Generated by Django 3.0.2 on 2020-02-04 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.CharField(max_length=10, unique=True)),
                ('device_name', models.CharField(max_length=50)),
                ('device_status', models.IntegerField()),
                ('device_image', models.CharField(max_length=50)),
                ('mac_address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensor_id', models.CharField(max_length=10, unique=True)),
                ('sensor_name', models.CharField(max_length=50)),
                ('sensor_type', models.IntegerField()),
                ('sensor_image', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Device_Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_sensor_id', models.CharField(max_length=10, unique=True)),
                ('sensor_status', models.IntegerField()),
                ('floor_location', models.CharField(max_length=50)),
                ('device_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='components.Device')),
                ('sensor_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='components.Sensor')),
            ],
        ),
    ]