# Generated by Django 5.0 on 2023-12-11 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_alter_communityengagement_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communityengagement',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]