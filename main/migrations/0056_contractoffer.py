# Generated by Django 4.1.5 on 2023-05-30 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0055_discorduser_auto_collect_rewards'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContractOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('years', models.PositiveSmallIntegerField()),
                ('salary', models.PositiveBigIntegerField()),
                ('option', models.CharField(choices=[('No Option', 'No Option'), ('Team Option', 'Team Option'), ('Player Option', 'Player Option'), ('Restricted Free Agent', 'Restricted Free Agent')], default='No Option', max_length=54)),
                ('benefits', models.CharField(choices=[('No Benefits', 'No Benefits'), ('No Trade Clause', 'No Trade Clause'), ('No Cut Clause', 'No Cut Clause'), ('No Trade Clause + No Cut Clause', 'No Trade Clause + No Cut Clause')], default='No Benefits', max_length=54)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.player')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.team')),
            ],
        ),
    ]
