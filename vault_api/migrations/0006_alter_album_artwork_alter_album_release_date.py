# Generated by Django 4.2.7 on 2023-11-16 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vault_api', '0005_alter_comment_options_remove_comment_date_posted_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='artwork',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='release_date',
            field=models.DateField(blank=True),
        ),
    ]