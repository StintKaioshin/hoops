from django import forms
from .league import config as league_config
from django.core import validators
from .models import GameLog, GameLogPlayerSetting, Player



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
    referral_code = forms.CharField(label="Referral Code", required=False, max_length=16)
    def __init__(self, *args, **kwargs):
        attribute_categories = kwargs.pop('attribute_categories', None)
        badge_categories = kwargs.pop('badge_categories', None)
        super(PlayerForm, self).__init__(*args, **kwargs)
        # Combine all attributes and badges into single choices lists
        attribute_choices = []
        badge_choices = []
        if attribute_categories:
            for category in attribute_categories:
                for attribute in attribute_categories[category]:
                    attribute_choices.append((attribute, attribute))
        if badge_categories:
            for category in badge_categories:
                for badge in badge_categories[category]:
                    badge_choices.append((badge, badge))
        # Add the static fields
        for i in range(1, 6):
            self.fields[f'primary_attr{i}'] = forms.ChoiceField(choices=attribute_choices, required=True)
            self.fields[f'primary_badge{i}'] = forms.ChoiceField(choices=badge_choices, required=False)
            self.fields[f'secondary_attr{i}'] = forms.ChoiceField(choices=attribute_choices, required=True)
            self.fields[f'secondary_badge{i}'] = forms.ChoiceField(choices=badge_choices, required=False)
class UpgradeForm(forms.Form):
    # Your UpgradeForm fields here...
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

class GameLogForm(forms.ModelForm):
    class Meta:
        model = GameLog
        fields = ['team_name', 'playbook', 'offensive_focus', 'offensive_tempo', 'offensive_rebounding', 
                  'defensive_focus', 'defensive_aggression', 'defensive_rebounding', 'team_sliders', 
                  'run_plays', 'offense_vs_defense', 'average_temp', 'bench_depth', 'guards_vs_forwards', 
                  'zone_usage', 'inside_vs_outside']


class GameLogPlayerSettingForm(forms.ModelForm):
    class Meta:
        model = GameLogPlayerSetting
        fields = ['player', 'touches', 'player_initiator']
    
    def __init__(self, *args, **kwargs):
        team = kwargs.pop('team', None)
        super(GameLogPlayerSettingForm, self).__init__(*args, **kwargs)
        if team:
            self.fields['player'].queryset = Player.objects.filter(team=team)



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
