# Generated by Django 4.0.3 on 2022-03-17 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_api', '0004_song_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='price',
            field=models.DecimalField(decimal_places=2, default='1.29', max_digits=6),
        ),
    ]
