# Generated by Django 4.1.5 on 2023-04-11 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0041_tradeoffer_finalized'),
    ]

    operations = [
        migrations.AddField(
            model_name='discorduser',
            name='can_approve_trades',
            field=models.BooleanField(default=False),
        ),
    ]