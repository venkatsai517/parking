# Generated by Django 5.0.1 on 2024-02-06 06:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parking_area_no', models.CharField(max_length=100)),
                ('vehicle_type', models.CharField(max_length=100)),
                ('vehicle_limit', models.CharField(max_length=200)),
                ('parking_charge', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('activated', 'Activated'), ('deactivated', 'Deactivated')], default='activated', max_length=100)),
                ('doc', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Add_vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_no', models.CharField(max_length=200)),
                ('vehicle_type', models.CharField(max_length=200)),
                ('parking_charge', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('parked', 'Parked'), ('leaved', 'Leaved')], default='parked', max_length=200)),
                ('arrival_time', models.DateTimeField(auto_now_add=True)),
                ('parking_area_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking.category')),
            ],
        ),
    ]