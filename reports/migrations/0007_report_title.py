# Generated by Django 4.0 on 2022-01-02 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0006_report_image_str'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='title',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]