from ...models import Player
from ...models import HistoryList

from ...league import config as league_config
from ...league.player import physicals as league_physicals

max_players = league_config.max_players
min_max_heights = league_config.min_max_heights
min_max_weights = league_config.min_max_weights

position_attributes = league_config.position_starting_attributes
trait_unlocks = league_config.trait_badge_unlocks
archetype_bonuses = league_config.archetype_attribute_bonuses
primary_bonus = league_config.archetype_primary_bonus
secondary_bonus = league_config.archetype_secondary_bonus


def playerCount(user):
    return Player.objects.filter(discord_user=user).count()


def validatePlayerCreation(user, formData):
    # Check if the user has reached the max number of players
    if playerCount(user) >= user.player_slots:
        return [False, "❌ You have reached the max number of players."]
    # Check if the user is trying to make a player with a height or weight that is not allowed (primary position)
    if (int(formData["height"])) < (
        min_max_heights[formData["primary_position"]]["min"]
    ):
        return [False, "❌ You are trying to make a player under the minimum height."]
    if (int(formData["height"])) > (
        min_max_heights[formData["primary_position"]]["max"]
    ):
        return [False, "❌ You are trying to make a player over the maximum height."]
    if (int(formData["weight"])) < (
        min_max_weights[formData["primary_position"]]["min"]
    ):
        return [False, "❌ You are trying to make a player under the minimum weight."]
    if (int(formData["weight"])) > (
        min_max_weights[formData["primary_position"]]["max"]
    ):
        return [False, "❌ You are trying to make a player over the maximum weight."]
    # Check if the user is trying to make a player with a height or weight that is not allowed (secondary position)
    if (int(formData["height"])) < (
        min_max_heights[formData["secondary_position"]]["min"]
    ):
        return [False, "❌ You are trying to make a player under the minimum height."]
    if (int(formData["height"])) > (
        min_max_heights[formData["secondary_position"]]["max"]
    ):
        return [False, "❌ You are trying to make a player over the maximum height."]
    if (int(formData["weight"])) < (
        min_max_weights[formData["secondary_position"]]["min"]
    ):
        return [False, "❌ You are trying to make a player under the minimum weight."]
    if (int(formData["weight"])) > (
        min_max_weights[formData["secondary_position"]]["max"]
    ):
       return [False, "❌ You are trying to make a player over the maximum weight."]

    # Check if the user is trying to make a player with an existing cyberface
    if Player.objects.filter(cyberface=formData["cyberface"]).exists():
        if int(formData["cyberface"]) != 1:
            return [
                False,
                "❌ You are trying to make a player with an existing cyberface.",
            ]
    # If everything is good, create the player
    return [True, None]


def createPlayer(user, formData):
    # Create the player's relationship objects
    historyList = HistoryList.objects.create()
    # Create the player
    newPlayer = Player.objects.create(
        # Customs
        first_name=formData["first_name"],
        last_name=formData["last_name"],
        cyberface=formData["cyberface"],
        weight=formData["weight"],
        height=formData["height"],
        primary_position=formData["primary_position"],
        secondary_position=formData["secondary_position"],
        jersey_number=formData["jersey_number"],
        # Relationships
        discord_user=user,
        history_list=historyList,
    )
    # Update the player's attributes
    newPlayer.attributes = {
        "primary_attr1": formData["primary_attr1"],
        "primary_attr2": formData["primary_attr2"],
        "primary_attr3": formData["primary_attr3"],
        "secondary_attr1": formData["secondary_attr1"],
        "secondary_attr2": formData["secondary_attr2"],
        "secondary_attr3": formData["secondary_attr3"],
    }
    # Update the player's badges
    newPlayer.badges = {
        "primary_badge1": formData["primary_badge1"],
        "primary_badge2": formData["primary_badge2"],
        "primary_badge3": formData["primary_badge3"],
        "secondary_badge1": formData["secondary_badge1"],
        "secondary_badge2": formData["secondary_badge2"],
        "secondary_badge3": formData["secondary_badge3"],
    }
    # Save the player
    historyList.save()
    newPlayer.save()
    # Return the player
    return newPlayer
