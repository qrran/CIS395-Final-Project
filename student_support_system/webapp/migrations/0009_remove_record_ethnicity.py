# Generated by Django 5.0 on 2023-12-11 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_remove_communityengagement_engagement_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='ethnicity',
        ),
    ]