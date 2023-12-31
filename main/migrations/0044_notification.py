# Generated by Django 4.1.5 on 2023-04-12 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0043_tradeoffer_notes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=100)),
                ('read', models.BooleanField(default=False)),
                ('date', models.DateTimeField()),
                ('discord_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.discorduser')),
            ],
        ),
    ]
