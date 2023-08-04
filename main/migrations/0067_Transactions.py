from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('main', '0066_player_trait_three'),
    ]

    operations = [
    migrations.RunSQL(
        'ALTER TABLE main_transactionsetc ALTER COLUMN from_team_id DROP NOT NULL',
        'ALTER TABLE main_transactionsetc ALTER COLUMN from_team_id SET NOT NULL'
    )
    ]
