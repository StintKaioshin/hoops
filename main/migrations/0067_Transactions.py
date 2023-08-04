from django.db import migrations
from main.models import Team

def handle_null_from_team(apps, schema_editor):
    TransactionsEtc = apps.get_model('main', 'TransactionsEtc')
    default_team = Team.objects.first()  # or get a team in some other way

    # Assign the default team to transactions with NULL from_team_id
    TransactionsEtc.objects.filter(from_team__isnull=True).update(from_team=default_team)

class Migration(migrations.Migration):

    dependencies = [
        ('main', '0066_player_trait_three'),  # replace with the actual previous migration name
    ]

    operations = [
        migrations.RunPython(handle_null_from_team),
    ]
