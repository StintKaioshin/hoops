# Generated by Django 4.1.5 on 2023-06-06 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0005_alter_game_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='day',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
