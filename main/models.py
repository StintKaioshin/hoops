# Django imports
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Custom imports
from .managers import DiscordAuthorizationManager
from .league import config as league_config

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# DiscordUser Models
# DiscordUser Models
class DiscordUser(models.Model):
    # Custom Manager
    objects = DiscordAuthorizationManager()
    # Discord User Model
    is_active = None
    has_module_perms = None
    id = models.BigIntegerField(primary_key=True, serialize=False)
    discord_tag = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='avatars/', null=False)
    public_flags = models.IntegerField()
    flags = models.IntegerField()
    locale = models.CharField(max_length=100)
    mfa_enabled = models.BooleanField()
    last_login = models.DateTimeField(null=True)
    last_reward = models.DateTimeField(null=True, blank=True)
    # Permissions
    can_update_players = models.BooleanField(default=False)
    can_approve_trades = models.BooleanField(default=False)
    # Player Slots
    player_slots = models.SmallIntegerField(default=league_config.max_players)
    auto_collect_rewards = models.BooleanField(default=False)
    can_change_styles = models.BooleanField(default=False)
    USERNAME_FIELD = 'discord_tag'

    def get_username(self):
        return self.discord_tag

    
    def is_authenticated(self, request):
        return True

    # Discord User Methods
    def has_module_perms(self, app_label):  # Added this method
        # This is a basic implementation. You'll need to customize this based on your permission logic.
        if self.is_active:
            return True
        return False

    def __str__(self):
        return f"{self.discord_tag}"



class Team(models.Model):
    # Team Model
    name = models.CharField(max_length=32)
    logo = models.CharField(max_length=100, default=league_config.initial_team_logo)
    abbrev = models.CharField(max_length=3)
    picks = models.JSONField(
        default=league_config.get_default_picks, blank=True, null=True
    )
    plays_in_main_league = models.BooleanField(default=True)
    show_on_lists = models.BooleanField(default=True)
    is_college_team = models.BooleanField(default=False)  # new field
    # Relationships   
    manager = models.ForeignKey(
        "DiscordUser", blank=True, null=True, on_delete=models.CASCADE
    )
    history_list = models.ForeignKey("HistoryList", on_delete=models.CASCADE)
    # Team Methods
    def __str__(self):
        return f"{self.name}"

# Player Models
class Player(models.Model):
    # Player Model
    first_name = models.CharField(default="Unknown", max_length=16)
    last_name = models.CharField(default="Player", max_length=16)
    cyberface = models.SmallIntegerField(default=0)
    height = models.SmallIntegerField(
        choices=league_config.height_choices, default=league_config.height_choices[0][0]
    )
    weight = models.IntegerField(
        validators=[
            MinValueValidator(league_config.player_weight_min),
            MaxValueValidator(league_config.player_weight_max),
        ]
    )
    primary_position = models.CharField(
        max_length=2,
        choices=league_config.position_choices,
        default=league_config.position_choices[0][0],
    )
    secondary_position = models.CharField(
        max_length=2,
        choices=league_config.position_choices,
        default=league_config.position_choices[0][0],
    )
    jersey_number = models.IntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(99)]
    )
    headshot = models.CharField(
        max_length=100,
        default=league_config.initial_headshot,
        blank=True,
    )
    # Attributes & Badges
    primary_attributes = models.JSONField(null=True, blank=True)
    secondary_attributes = models.JSONField(null=True, blank=True)
    primary_badges = models.JSONField(null=True, blank=True)
    secondary_badges = models.JSONField(null=True, blank=True)
    # Player Currencies
    primary_currency = models.BigIntegerField(
        name="cash", default=league_config.primary_currency_start
    )
    salary = models.PositiveBigIntegerField(name="salary", default=0)
    cap_hit = models.PositiveBigIntegerField(name="cap_hit", default=0)
    spent = models.PositiveBigIntegerField(name="spent", default=0)
    # Player Contract Details
    contract_ends_after = models.SmallIntegerField(default=1)
    contract_option = models.CharField(
        max_length=54,
        choices=league_config.contract_option_choices,
        default=league_config.contract_option_choices[0][0],
    )
    contract_benefits = models.CharField(
        max_length=54,
        choices=league_config.contract_benefit_choices,
        default=league_config.contract_benefit_choices[0][0],
    )
    contract_notes = models.CharField(max_length=100, blank=True, null=True)
    # Relationships
    discord_user = models.ForeignKey(
        "DiscordUser", blank=True, null=True, on_delete=models.CASCADE
    )
    current_team = models.ForeignKey(
        "Team", blank=True, null=True, on_delete=models.CASCADE
    )
    history_list = models.ForeignKey("HistoryList", on_delete=models.CASCADE)
    years_played = models.SmallIntegerField(default=1)
    upgrades_pending = models.BooleanField(default=False)
    free_agent = models.BooleanField(default=True)
    use_game_tendencies = models.BooleanField(default=True)
    is_rookie = models.BooleanField(default=False)
    # Attributes, Badges, & Hotzones
    styles = models.JSONField(default=league_config.get_default_styles, blank=True)
    statics = models.JSONField(default=league_config.get_default_statics)
    attributes = models.JSONField(default=league_config.get_default_attributes)
    badges = models.JSONField(default=league_config.get_default_badges)
    hotzones = models.JSONField(default=league_config.get_default_hotzones)
    tendencies = models.JSONField(default=league_config.get_default_tendencies)
    # Player Methods
    def __str__(self):
        return f"[{self.id}] {self.first_name} {self.last_name}"
# List Models (for players)
class HistoryList(models.Model):
    history = models.JSONField(default=league_config.get_default_history, blank=True)
# Team & Statistic Models
# Currency Transaction Models
class Transaction(models.Model):
    # Transaction Model
    transaction_type = models.CharField(
        max_length=16,
        choices=league_config.transaction_type_choices,
        default=league_config.transaction_type_choices[0][0],
    )
    amount = models.PositiveBigIntegerField()
    reason = models.CharField(max_length=100, blank=True)
    # Relationships
    giver = models.ForeignKey("DiscordUser", on_delete=models.CASCADE)
    player = models.ForeignKey("Player", on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=False)
    # Transaction Methods
    def __str__(self):
        return f"{self.transaction_type}: {self.amount}"
        
class GameLog(models.Model):
    team_name = models.ForeignKey(Team, on_delete=models.CASCADE)
    playbook = models.CharField(max_length=100)
    offensive_focus = models.CharField(max_length=100)
    offensive_tempo = models.CharField(max_length=100)
    offensive_rebounding = models.CharField(max_length=100)
    defensive_focus = models.CharField(max_length=100)
    defensive_aggression = models.CharField(max_length=100)
    defensive_rebounding = models.CharField(max_length=100)
    team_sliders = models.IntegerField()
    run_plays = models.IntegerField()
    offense_vs_defense = models.IntegerField()
    average_temp = models.IntegerField()
    bench_depth = models.IntegerField()
    guards_vs_forwards = models.IntegerField()
    zone_usage = models.IntegerField()
    inside_vs_outside = models.IntegerField()

class GameLogPlayerSetting(models.Model):
    game_log = models.ForeignKey(GameLog, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    touches = models.IntegerField()
    play_initiator = models.BooleanField(default=False)



# Trade Models
class TradeOffer(models.Model):
    # Trade Offer Model
    offer = models.JSONField(default=league_config.get_default_trade_offer)
    accepted = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    finalized = models.BooleanField(default=False)
    notes = models.CharField(max_length=100, blank=True)
    # Relationships
    sender = models.ForeignKey("Team", on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(
        "Team", on_delete=models.CASCADE, related_name="receiver"
    )
    # Trade Offer Methods
    def __str__(self):
        return f"{self.sender} -> {self.receiver}"
# Offer Models
class ContractOffer(models.Model):
    # Contract Offer Model
    years = models.PositiveSmallIntegerField()
    salary = models.PositiveBigIntegerField()
    option = models.CharField(
        max_length=54,
        choices=league_config.contract_option_choices,
        default=league_config.contract_option_choices[0][0],
    )
    benefits = models.CharField(
        max_length=54,
        choices=league_config.contract_benefit_choices,
        default=league_config.contract_benefit_choices[0][0],
    )
    notes = models.CharField(max_length=100, blank=True, null=True, default="No notes.")
    # Relationships
    team = models.ForeignKey("Team", on_delete=models.CASCADE)
    player = models.ForeignKey("Player", on_delete=models.CASCADE)
    # Boolean Fields
    accepted = models.BooleanField(default=False)
    # Contract Offer Methods
    def __str__(self):
        return f"{self.team.abbrev} -> {self.player.first_name} {self.player.last_name}"

class TransactionsEtc(models.Model):
    PLAYER_SIGNED = 'PS'
    PLAYER_TRADED = 'PT'
    PLAYER_DROPPED = 'PD'

    TRANSACTION_TYPE_CHOICES = [
        (PLAYER_SIGNED, 'Player Signed'),
        (PLAYER_TRADED, 'Player Traded'),
        (PLAYER_DROPPED, 'Player Dropped'),
    ]

    transaction_type = models.CharField(
        max_length=2,
        choices=TRANSACTION_TYPE_CHOICES,
        default=PLAYER_SIGNED,
    )

    # Null values are now allowed for from_team and to_team
    from_team = models.ForeignKey(Team, related_name='transactions_made', on_delete=models.CASCADE, null=True)
    to_team = models.ForeignKey(Team, related_name='transactions_received', on_delete=models.CASCADE, null=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_transaction_type_display()} - {self.from_team.name if self.from_team else 'N/A'} to {self.to_team.name if self.to_team else 'N/A'} - {self.player.first_name} {self.player.last_name} - {self.timestamp}"

# Coupon Models
class Coupon(models.Model):
    code = models.CharField(max_length=16, unique=True)
    name = models.CharField(max_length=16, default="Default Coupon")
    amount = models.PositiveBigIntegerField()
    one_use = models.BooleanField(default=False)
    used = models.BooleanField(default=False)
    # Coupon Methods
    def __str__(self):
        return f"{self.code}"
# Notification Models
class Notification(models.Model):
    # Notifcation Model
    title = models.CharField(max_length=32, default="Notification")
    message = models.CharField(max_length=100, default="Content")
    read = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=False)
    # Relationships
    discord_user = models.ForeignKey("DiscordUser", on_delete=models.CASCADE)
# Award Models
class Award(models.Model):
    # Award Model
    name = models.CharField(
        max_length=6,
        choices=league_config.award_name_choices,
        default=league_config.award_name_choices[0][0],
    )
    description = models.CharField(max_length=16, default="Description")
    # Relationships
    player = models.ForeignKey("Player", on_delete=models.CASCADE)
    season = models.PositiveSmallIntegerField(default=1)
    # Award Methods
    def __str__(self):
        return f"S{self.season} - {self.name} - {self.player}"
