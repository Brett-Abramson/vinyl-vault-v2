# Generated by Django 4.2.7 on 2023-11-15 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vault_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='track',
            options={'ordering': ['order_num']},
        ),
        migrations.AlterUniqueTogether(
            name='track',
            unique_together={('album', 'order_num')},
        ),
    ]
