# Generated by Django 4.0.1 on 2022-01-21 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_properties_delete_propertiesredio'),
    ]

    operations = [
        migrations.AddField(
            model_name='properties',
            name='latitud',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='properties',
            name='longitud',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
