# Generated by Django 4.1.5 on 2023-03-14 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_team_picks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='trait_three',
        ),
        migrations.AddField(
            model_name='player',
            name='cyberface',
            field=models.SmallIntegerField(default=0),
        ),
    ]
