# Generated by Django 4.0 on 2021-12-29 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csv',
            name='file_name',
            field=models.FileField(upload_to='cvs'),
        ),
    ]
