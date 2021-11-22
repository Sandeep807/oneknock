# Generated by Django 3.2.9 on 2021-11-22 12:26

from django.db import migrations, models
import service.models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicecategory',
            name='id',
            field=models.IntegerField(default=service.models.generate_id, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='servicesubcategory',
            name='id',
            field=models.IntegerField(default=service.models.generate_id, editable=False, primary_key=True, serialize=False),
        ),
    ]
