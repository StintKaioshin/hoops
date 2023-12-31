# Generated by Django 4.1.5 on 2023-05-25 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0052_alter_award_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award',
            name='name',
            field=models.CharField(choices=[('MVP', 'MVP'), ('DPOY', 'DPOY'), ('MIP', 'MIP'), ('ROY', 'ROY'), ('6MOY', '6MOY'), ('AH1ST', 'AH1ST'), ('AH2ND', 'AH2ND'), ('D1ST', 'D1ST'), ('D2ND', 'D2ND'), ('KOTS', 'KOTS'), ('RING', 'RING'), ('FMVP', 'FMVP'), ('ASG', 'ASG'), ('ASGMVP', 'ASGMVP'), ('3PTWIN', '3PTWIN'), ('DNKWIN', 'DNKWIN')], default='MVP', max_length=6),
        ),
        migrations.AlterField(
            model_name='player',
            name='discord_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.discorduser'),
        ),
        migrations.AlterField(
            model_name='team',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.discorduser'),
        ),
    ]
