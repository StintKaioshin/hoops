# Generated by Django 4.1.5 on 2023-06-15 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0059_alter_contractoffer_notes'),
        ('stats', '0008_alter_game_game_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeasonAverages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ppg', models.DecimalField(decimal_places=1, default=0, max_digits=4)),
                ('rpg', models.DecimalField(decimal_places=1, default=0, max_digits=4)),
                ('apg', models.DecimalField(decimal_places=1, default=0, max_digits=4)),
                ('spg', models.DecimalField(decimal_places=1, default=0, max_digits=4)),
                ('bpg', models.DecimalField(decimal_places=1, default=0, max_digits=4)),
                ('tpg', models.DecimalField(decimal_places=1, default=0, max_digits=4)),
                ('fgm', models.DecimalField(decimal_places=1, default=0, max_digits=4)),
                ('fga', models.DecimalField(decimal_places=1, default=0, max_digits=4)),
                ('tpm', models.DecimalField(decimal_places=1, default=0, max_digits=4)),
                ('tpa', models.DecimalField(decimal_places=1, default=0, max_digits=4)),
                ('ftm', models.DecimalField(decimal_places=1, default=0, max_digits=4)),
                ('fta', models.DecimalField(decimal_places=1, default=0, max_digits=4)),
                ('orpg', models.DecimalField(decimal_places=1, default=0, max_digits=4)),
                ('fpg', models.DecimalField(decimal_places=1, default=0, max_digits=4)),
                ('gmsc', models.DecimalField(decimal_places=1, default=0, max_digits=4)),
                ('season', models.PositiveSmallIntegerField(default=2, unique=True)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.player')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.team')),
            ],
        ),
    ]
