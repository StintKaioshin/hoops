# Generated by Django 4.1.5 on 2023-05-30 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0057_contractoffer_accepted'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractoffer',
            name='notes',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
