# Generated by Django 4.1.5 on 2023-02-22 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_player_height_limits_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='accepted_offer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='player',
            name='free_agent',
            field=models.BooleanField(default=True),
        ),
    ]
