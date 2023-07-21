from django import forms
from .league import config as league_config
from django.core import validators

class PlayerForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=16)
    last_name = forms.CharField(label="Last Name", max_length=16)
    cyberface = forms.IntegerField(label="Cyberface", min_value=0, max_value=40000)
    height = forms.ChoiceField(label="Height", choices=league_config.height_choices)
    weight = forms.IntegerField(
        label="Weight",
        min_value=league_config.player_weight_min,
        max_value=league_config.player_weight_max,
    )
    primary_position = forms.ChoiceField(
        label="Primary Position", choices=league_config.position_choices
    )
    secondary_position = forms.ChoiceField(
        label="Secondary Position", choices=league_config.position_choices
    )
    jersey_number = forms.IntegerField(
        label="Jersey Number", min_value=0, max_value=league_config.max_attribute
    )

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
