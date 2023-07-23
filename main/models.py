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
