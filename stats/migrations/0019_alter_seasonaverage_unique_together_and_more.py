# Generated by Django 4.1.5 on 2023-06-15 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0018_rename_average_type_seasonaverage_game_type_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='seasonaverage',
            unique_together={('season', 'team', 'player', 'game_type')},
        ),
        migrations.AlterUniqueTogether(
            name='seasontotal',
            unique_together={('season', 'team', 'player', 'game_type')},
        ),
    ]
