# Generated by Django 4.1.5 on 2023-04-08 16:38

from django.db import migrations, models
import main.league.config


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0034_player_use_game_tendencies'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='statics',
            field=models.JSONField(default=main.league.config.get_default_statics),
        ),
    ]
