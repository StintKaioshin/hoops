# Generated by Django 4.1.5 on 2023-06-15 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0019_alter_seasonaverage_unique_together_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='seasonaverage',
            name='manual_entry',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='seasontotal',
            name='manual_entry',
            field=models.BooleanField(default=False),
        ),
    ]
