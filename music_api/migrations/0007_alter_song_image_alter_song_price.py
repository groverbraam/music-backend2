# Generated by Django 4.0.3 on 2022-03-17 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_api', '0006_alter_song_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='image',
            field=models.CharField(blank=True, default='https://i.imgur.com/D3aOVsJ.png', max_length=100),
        ),
        migrations.AlterField(
            model_name='song',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default='1.29', max_digits=6),
        ),
    ]