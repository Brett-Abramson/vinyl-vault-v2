# Generated by Django 4.2.7 on 2023-11-16 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vault_api', '0002_alter_track_options_alter_track_unique_together'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='spotify_ID',
            new_name='spotify_id',
        ),
    ]
