# Generated by Django 4.1.5 on 2023-02-25 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_remove_player_accepted_offer'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='years_played',
            field=models.SmallIntegerField(default=1),
        ),
    ]
