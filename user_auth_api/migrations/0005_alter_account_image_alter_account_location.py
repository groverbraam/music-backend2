# Generated by Django 4.0.3 on 2022-03-21 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth_api', '0004_alter_account_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='image',
            field=models.CharField(blank=True, default='https://imgur.com/V4RclNb', max_length=100),
        ),
        migrations.AlterField(
            model_name='account',
            name='location',
            field=models.CharField(blank=True, default='unknown', max_length=100),
        ),
    ]
