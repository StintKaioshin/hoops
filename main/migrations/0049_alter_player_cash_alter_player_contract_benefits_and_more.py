# Generated by Django 4.1.5 on 2023-04-18 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0048_player_contract_benefits_player_contract_ends_after_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='cash',
            field=models.BigIntegerField(default=1000),
        ),
        migrations.AlterField(
            model_name='player',
            name='contract_benefits',
            field=models.CharField(choices=[('No Benefits', 'No Benefits'), ('No Trade Clause', 'No Trade Clause'), ('No Cut Clause', 'No Cut Clause'), ('No Trade Clause + No Cut Clause', 'No Trade Clause + No Cut Clause')], default='No Benefits', max_length=54),
        ),
        migrations.AlterField(
            model_name='player',
            name='contract_option',
            field=models.CharField(choices=[('No Option', 'No Option'), ('Team Option', 'Team Option'), ('Player Option', 'Player Option'), ('Restricted Free Agent', 'Restricted Free Agent')], default='No Option', max_length=54),
        ),
    ]
