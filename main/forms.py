import json
from django import forms
from .league import config as league_config
from django.core import validators

player_styles = open("main/league/looyh/styles.json")
player_styles = json.load(player_styles)


class PlayerForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    height = forms.IntegerField(required=True, validators=[validators.MinValueValidator(1), validators.MaxValueValidator(100)])
    weight = forms.IntegerField(required=True, validators=[validators.MinValueValidator(1), validators.MaxValueValidator(300)])
    cyberface = forms.ImageField(required=True)
    primary_position = forms.ChoiceField(choices=[(x, x) for x in ["PG", "SG", "SF", "PF", "C"]], required=True)
    secondary_position = forms.ChoiceField(choices=[(x, x) for x in ["PG", "SG", "SF", "PF", "C"]], required=True)
    jersey_number = forms.IntegerField(required=True, validators=[validators.MinValueValidator(0), validators.MaxValueValidator(99)])
    referral_code = forms.CharField(max_length=100, required=False)

    def __init__(self, *args, **kwargs):
        attribute_categories = kwargs.pop('attribute_categories', None)
        badge_categories = kwargs.pop('badge_categories', None)
        super(PlayerForm, self).__init__(*args, **kwargs)

        if attribute_categories:
            for category in attribute_categories:
                for attribute in attribute_categories[category]:
                    self.fields[f'{category}_{attribute}'] = forms.IntegerField(required=True, validators=[validators.MinValueValidator(1), validators.MaxValueValidator(100)])

        if badge_categories:
            for category in badge_categories:
                for badge in badge_categories[category]:
                    self.fields[f'{category}_{badge}'] = forms.ChoiceField(choices=[(x, x) for x in ["Bronze", "Silver", "Gold", "Hall of Fame"]], required=False)

        self.fields = sorted(self.fields, key=lambda x: x[0])


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
