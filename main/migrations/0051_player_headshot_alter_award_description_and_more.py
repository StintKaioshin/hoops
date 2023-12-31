# Generated by Django 4.1.5 on 2023-05-01 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0050_award'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='headshot',
            field=models.CharField(blank=True, default='https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png', max_length=100),
        ),
        migrations.AlterField(
            model_name='award',
            name='description',
            field=models.CharField(default='Description', max_length=16),
        ),
        migrations.AlterField(
            model_name='award',
            name='name',
            field=models.CharField(choices=[('MVP', 'MVP'), ('DPOY', 'DPOY'), ('MIP', 'MIP'), ('ROY', 'ROY'), ('6MOY', '6MOY'), ('AH1ST', 'AH1ST'), ('AH2ND', 'AH2ND'), ('D1ST', 'D1ST'), ('D2ND', 'D2ND'), ('KOTS', 'KOTS')], default='MVP', max_length=5),
        ),
    ]
