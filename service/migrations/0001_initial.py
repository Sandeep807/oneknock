# Generated by Django 3.2.9 on 2021-11-20 06:35

from django.db import migrations, models
import django.db.models.deletion
import service.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceCategory',
            fields=[
                ('id', models.IntegerField(default=service.models.generate_id, editable=False, primary_key=True, serialize=False)),
                ('service_name', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='service/logo/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceSubCategory',
            fields=[
                ('id', models.IntegerField(default=service.models.generate_id, editable=False, primary_key=True, serialize=False)),
                ('sub_service_name', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='sub_service/logo/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('services', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service', to='service.servicecategory')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceBooking',
            fields=[
                ('id', models.IntegerField(default=service.models.generate_id, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('type', models.CharField(blank=True, max_length=100, null=True)),
                ('problem', models.TextField()),
                ('flat', models.TextField()),
                ('zip_code', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sub_services', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.servicesubcategory')),
            ],
        ),
    ]
