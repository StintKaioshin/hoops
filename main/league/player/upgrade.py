# Custom imports
from ...league import config as league_config
# Python imports
import datetime
import json
# Upgrade methods
def attributeCost(player, attribute, currentValue, futureValue):
    # Define some league config variables
    total_price = 0
    attribute_prices = league_config.attribute_prices
    # Define some player variables
    primary_attributes = player.primary_attributes
    secondary_attributes = player.secondary_attributes
    # Check the attribute tier (60-70, 71-80)
    for i in range((currentValue + 1), (futureValue + 1)):
        for _, tier in attribute_prices.items():
            if i in tier["range"]:
                if attribute in primary_attributes:
                    total_price += tier["primary"]
                    continue
                elif attribute in secondary_attributes:
                    total_price += tier["secondary"]
                    continue
                else:
                    total_price += tier["base"]
    # Return the upgrade cost
    return total_price
def badgeCost(player, badge, currentValue, futureValue):
    # Define some league config variables
    total_price = 0
    badge_prices = league_config.badge_prices
    # Define some player variables
    primary_badges = player.primary_badges
    secondary_badges = player.secondary_badges
    # Check the badge tier (Bronze, Silver, Gold, Hof)
    for i in range((currentValue + 1), (futureValue + 1)):
        for index, tier in badge_prices.items():
            if i == index:
                if badge in primary_badges:
                    total_price += tier["primary"]
                    continue
                elif badge in secondary_badges:
                    total_price += tier["secondary"]
                    continue
                else:
                    total_price += tier["base"]
    # Return the upgrade cost
    return total_price
def hotzoneCost(player, hotzones, currentValue, futureValue):
    return league_config.hotzone_price


def formatAndValidate(player, cleanedFormData):
    hotzone_keys = ['Left Corner Three', 'Left Wing Three', "Middle Three", "Right Wing Three", "Right Corner Three", "Left Corner Midrange", "Left Wing Midrange", "Middle Midrange", "Right Wing Midrange", "Right Corner Midrange", "Inside Left", "Inside Middle" , "Inside Right", "Inside Center"]  # list all expected keys
    # Format the cleaned form data (so it works with the database)
    formatFormData = cleanedFormData.copy()
    print(formatFormData)
    # formatFormData = {k.title(): v for k, v in formatFormData.items()}
    # formatFormData = {k.replace("_", " "): v for k, v in formatFormData.items()}
    # Initialize the upgrade data (will be returned to upgrade the player with)
    # Basically, we'll just be adding the values that were changed and are valid to this dictionary
    upgradeData = {"attributes": {}, "badges": {}, "tendencies": {}, "hotzones": {}}
    error = ""
    # Define some player variables
    primary_badges = player.primary_badges
    secondary_badges = player.secondary_badges
    # Filter out values that are under minimum, over maximum or equal to current value
    for k, v in formatFormData.items():
        # Type cast the value to an integer
        v = int(v)
        # If the key is an attribute
        if k in player.attributes:
            # Initialize the values
            currentValue = player.attributes[k]
            minimumValue = league_config.min_attribute
            maximumValue = league_config.max_attribute
            # Cases
            if v < minimumValue:  # Upgrade value is less than minimum value
                error = f"❌ {k} ({v}) value is less than the minimum value."
                break
            if v > maximumValue:  # Upgrade value is greater than maximum value
                error = f"❌ {k} ({v}) value is greater than the maximum value."
                break
            # Add the value to the upgrade data
            upgradeCost = attributeCost(player, k, currentValue, v)
            upgradeData["attributes"][k] = {
                "cost": upgradeCost,
                "old": currentValue,
                "new": v,
            }
        # If the key is a badge
        if k in player.badges:
            # Finding the maximum value for the badges
            if k in primary_badges:
                maximumValue = league_config.primary_badge_max
            elif k in secondary_badges:
                maximumValue = league_config.secondary_badge_max
            else:
                maximumValue = league_config.tertiary_badge_max
            # Initialize the values
            currentValue = player.badges[k]
            minimumValue = league_config.min_badge
            # Cases
            if v < minimumValue:  # Upgrade value is less than minimum value
                error = f"❌ {k} ({v}) is less than the minimum value."
                break
            if v > maximumValue:  # Upgrade value is greater than maximum value
                error = f"❌ {k} ({v}) is greater than the maximum value."
                break
            # Add the value to the upgrade data
            upgradeCost = badgeCost(player, k, currentValue, v)
            upgradeData["badges"][k] = {
                "cost": upgradeCost,
                "old": currentValue,
                "new": v,
            }
        # If the key is a tendency
        if k in player.tendencies:
            # Initialize the values
            currentValue = player.tendencies[k]
            maximumValue = league_config.max_tendency
            # Cases
            if k in league_config.banned_tendencies:
                if v > currentValue:
                    error = f"❌ {k} cannot be changed."
                    break
            if k in league_config.max_tendencies:
                if v > league_config.max_tendencies[k]:
                    error = f"❌ {k} is greater than the maximum value. ({league_config.max_tendencies[k]})"
                    break
            if v > maximumValue:
                error = f"❌ {k} is greater than the maximum value. ({maximumValue})"
                break
            # Add the value to the ugprade data
            upgradeData["tendencies"][k] = {
                "cost": 0,
                "old": player.tendencies[k],
                "new": v,
            }
        print(f"Processing hotzones. Key: {k}")  # This will print every key being processed

        if k in league_config.initial_hotzones:
            print(f"Upgrading hotzone: {k}")  # This will print the key if it matches a player's hotzone
            upgradeData["hotzones"][k] = {
            "cost": hotzoneCost(player, k, player.hotzones[k], v),
            "old": player.hotzones[k],
            "new": v,
    }
    print('Processed hotzones:', upgradeData["hotzones"])
    return [upgradeData, error]
def createUpgrade(player, cleanedFormData):
    formatResponse = formatAndValidate(player, cleanedFormData)
    upgradeData = formatResponse[0]
    upgradeError = formatResponse[1]
    
    if upgradeError != "":
        return upgradeError
    
    totalCost = 0
    for category in ["attributes", "badges", "tendencies", "hotzones"]:
        for k, v in upgradeData[category].items():
            totalCost += v["cost"]
            print(f"{category} - {k}: {v['cost']}")  # Print the cost breakdown

    print(f"Total Cost: {totalCost}")  # Print total cost for better visibility

    # Check the conditions again
    if totalCost <= 0 and not upgradeData["tendencies"]:
        print(upgradeData)  # Print the entire upgradeData for visibility
        return "😕 Nothing to upgrade!"
    if player.cash < totalCost:
        return "❌ You don't have enough cash for this upgrade!"
    # Check if the player has enough cash
    if player.cash >= totalCost:
        # Subtract the cost from the player's cash
        player.cash -= totalCost
        # Add the upgrades to the player
        for k, v in upgradeData["attributes"].items():
            # Check if the attribute is a physical attribute
            if k in league_config.attribute_categories["physical"]:
                return f"❌ '{k}' cannot be upgraded because it's a physical."
            else:
                player.attributes[k] = v["new"]
        for k, v in upgradeData["badges"].items():
            player.badges[k] = v["new"]
        for k, v in upgradeData["tendencies"].items():
            player.tendencies[k] = v["new"]
        # Add the totalCost to spent & add history list log
        currentTime = datetime.datetime.now()
        timestamp = currentTime.strftime("%Y-%m-%d | %H:%M:%S")
        player.spent += totalCost
        player.upgrades_pending = True
        # Save the player & history lists
        player.save()
        # Return success message
        return f"✅ Congrats, you upgraded your player for ${totalCost}!"
