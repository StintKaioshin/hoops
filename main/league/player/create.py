from ...models import Player
from ...models import HistoryList
from ...league import config as league_config
from ...league.player import physicals as league_physicals

max_players = league_config.max_players
min_max_heights = league_config.min_max_heights
min_max_weights = league_config.min_max_weights
position_attributes = league_config.position_starting_attributes
primary_attribute_bonus = league_config.primary_attribute_bonus
secondary_attribute_bonus = league_config.secondary_attribute_bonus
primary_badge_bonus = league_config.primary_badge_bonus
secondary_badge_bonus = league_config.secondary_badge_bonus


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
    # Check if the attributes and badges the user selected are validated
    if Player.objects.filter(cyberface=formData["cyberface"]).exists():
        if int(formData["cyberface"]) != 1:
            return [False, "❌ You are trying to make a player with an existing cyberface."]
    # If everything is good, create the player
    return [True, None]

def createPlayer(user, formData):
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
    newPlayer.primary_attributes = {
        "primary_attr1": formData.get("primary_attr1", None),
        "primary_attr2": formData.get("primary_attr2", None),
        "primary_attr3": formData.get("primary_attr3", None),
        "primary_attr4": formData.get("primary_attr4", None),
        "primary_attr5": formData.get("primary_attr5", None),
    }
    newPlayer.secondary_attributes = {
        "secondary_attr1": formData.get("secondary_attr1", None),
        "secondary_attr2": formData.get("secondary_attr2", None),
        "secondary_attr3": formData.get("secondary_attr3", None),
        "secondary_attr4": formData.get("secondary_attr4", None),
        "secondary_attr5": formData.get("secondary_attr5", None),
    }
    # Update the player's badges
    newPlayer.primary_badges = {
        "primary_badge1": formData.get("primary_badge1", None),
        "primary_badge2": formData.get("primary_badge2", None),
        "primary_badge3": formData.get("primary_badge3", None),
        "primary_badge4": formData.get("primary_badge4", None),
        "primary_badge5": formData.get("primary_badge5", None),
    }
    newPlayer.secondary_badges = {
        "secondary_badge1": formData.get("secondary_badge1", None),
        "secondary_badge2": formData.get("secondary_badge2", None),
        "secondary_badge3": formData.get("secondary_badge3", None),
        "secondary_badge4": formData.get("secondary_badge4", None),
        "secondary_badge5": formData.get("secondary_badge5", None),
    }
    # Save the player
    # Get base attributes for the player's primary position
    new_attributes = position_attributes[newPlayer.primary_position]
    newPlayer.primary_attributes = formData["primary_attributes"]
    newPlayer.secondary_attributes = formData["secondary_attributes"]
    newPlayer.primary_badges = formData["primary_badges"]
    newPlayer.secondary_badges = formData["secondary_badges"]

# Add base attributes to newPlayer.attributes
    for attribute, value in new_attributes.items():
        newPlayer.attributes[attribute] = value

# Overwrite any base attributes that are also primary or secondary attributes
    combined_attributes = list(newPlayer.primary_attributes.keys()) + list(newPlayer.secondary_attributes.keys())
    for attribute in combined_attributes:
        if attribute in new_attributes:
            newPlayer.attributes[attribute] = new_attributes[attribute]

    updatedPlayer = league_physicals.setStartingPhysicals(newPlayer)
# Save the player
    historyList.save()
    updatedPlayer.save()
# Return the player
    return updatedPlayer

