# Generated by Django 4.0.3 on 2022-03-21 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_api', '0002_alter_song_audio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='audio',
            field=models.FileField(upload_to='api/songs/'),
        ),
        migrations.AlterField(
            model_name='song',
            name='genre',
            field=models.CharField(blank=True, choices=[('pop', 'Pop'), ('rock', 'Rock'), ('techno', 'Techno'), ('hiphop', 'Hip-hop'), ('jazz', 'Jazz'), ('rap', 'Rap'), ('country', 'Country'), ('metal', 'Metal'), ('alternative', 'Alternative'), ('indie', 'Indie')], default='', max_length=100),
        ),
    ]
