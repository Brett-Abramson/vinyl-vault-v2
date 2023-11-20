# Generated by Django 4.2.7 on 2023-11-20 21:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vault_api', '0007_alter_user_managers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='spotify_id',
        ),
        migrations.CreateModel(
            name='SpotifyProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spotify_id', models.CharField(blank=True, max_length=200, null=True)),
                ('access_token', models.TextField(blank=True, null=True)),
                ('refresh_token', models.TextField(blank=True, null=True)),
                ('token_expires', models.DateTimeField(blank=True, null=True)),
                ('scope', models.TextField(blank=True, null=True)),
                ('profile_link', models.URLField(blank=True, max_length=500, null=True)),
                ('profile_pic_url', models.URLField(blank=True, max_length=500, null=True)),
                ('profile_pic_height', models.IntegerField(blank=True, null=True)),
                ('profile_pic_width', models.IntegerField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='spotify_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]