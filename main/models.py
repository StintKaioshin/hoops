# Custom imports
import json

# Django imports
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

# Main imports
from .league import config as league_config
from copy import deepcopy

player_styles = open("main/league/looyh/styles.json")
player_styles = json.load(player_styles)
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


class UpgradeForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(UpgradeForm, self).__init__(*args, **kwargs)
        # For each key in attributes, create integerfield
        for key in league_config.initial_attributes:
            if key in league_config.attribute_categories["physical"]:
                continue
            self.fields[key] = forms.IntegerField(
                label=key,
                min_value=0,
                max_value=league_config.max_attribute,
                widget=forms.NumberInput(attrs={"onchange": "updatePrice()"}),
            )
        # For each key in badges, create choicefield
        for key in league_config.initial_badges:
            self.fields[key] = forms.ChoiceField(
                label=key,
                choices=league_config.badge_upgrade_choices,
                widget=forms.Select(attrs={"onchange": "updatePrice()"}),
            )
        # For each key in tendencies, create integerfield
        for key in league_config.initial_tendencies:
            # If players cannot change this tendency, skip
            if key in league_config.banned_tendencies:
                continue
            # If players can change this tendency, create field
            self.fields[key] = forms.IntegerField(
                label=key,
                min_value=league_config.min_tendency,
                max_value=league_config.max_tendency,
                widget=forms.NumberInput(attrs={"onchange": "updatePrice()"}),
            )
        # For each key in hotzones, create choicefield
        # for key in league_config.initial_hotzones:
        #     self.fields[key] = forms.ChoiceField(
        #         label=key,
        #         choices=league_config.hotzone_choices,
        #         widget=forms.Select(attrs={"onchange": "updatePrice()"}),
        #     )

class StylesForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(StylesForm, self).__init__(*args, **kwargs)
        for style, data in player_styles.items():
            # Create the ChoiceField
            self.fields[style] = forms.ChoiceField(
                label=style,
                choices=data["options"],
                widget=forms.Select(),
            )

class TradeForm(forms.Form):
    pass
