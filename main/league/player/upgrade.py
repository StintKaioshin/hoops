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


def formatAndValidate(player, cleanedFormData):
    # Format the cleaned form data (so it works with the database)
    formatFormData = cleanedFormData.copy()
    upgradeData = {"attributes": {}, "badges": {}, "tendencies": {}}
    error = ""
    primary_badges = player.primary_badges
    secondary_badges = player.secondary_badges

    # Filter out values that are under minimum, over maximum or equal to current value
    for k, v in formatFormData.items():
        v = int(v)
        category, key = k.split("_")  # Split the prefixed key into category and key
        currentValue = getattr(player, category)[key]  # Access the current value using the category and key
        minimumValue = league_config.min_values[category]  # Access the minimum value using the category
        maximumValue = league_config.max_values[category]  # Access the maximum value using the category
        # Set the maximum value for badges
        if category == "badges":
            if key in primary_badges:
                maximumValue = league_config.primary_badge_max
            elif key in secondary_badges:
                maximumValue = league_config.secondary_badge_max
            else:
                maximumValue = league_config.tertiary_badge_max
        # Cases
        if v < minimumValue:
            error = f"❌ {k} ({v}) value is less than the minimum value."
            break
        if v > maximumValue:
            error = f"❌ {k} ({v}) value is greater than the maximum value."
            break
        # Add the value to the upgrade data
        upgradeCost = attributeCost(player, k, currentValue, v) if category == "attributes" else badgeCost(player, k, currentValue, v)
        upgradeData[category][key] = {
            "cost": upgradeCost,
            "old": currentValue,
            "new": v,
        }

    return [upgradeData, error]

def createUpgrade(player, cleanedFormData):
    # Format the form data
    formatResponse = formatAndValidate(player, cleanedFormData)
    upgradeData = formatResponse[0]
    upgradeError = formatResponse[1]

    # Check if there were any errors
    if upgradeError != "":
        return upgradeError

    # Initialize the total cost
    totalCost = 0

    # Calculate the total cost
    for k, v in upgradeData["attributes"].items():
        totalCost += v["cost"]
    for k, v in upgradeData["badges"].items():
        totalCost += v["cost"]
    for k, v in upgradeData["tendencies"].items():
        totalCost += v["cost"]

    # Return if cost is below zero & no tendencies were upgraded, or player doesn't have enough cash
    if totalCost <= 0 and not upgradeData["tendencies"]:
        return "😕 Nothing to upgrade!"
    if player.cash < totalCost:
        return "❌ You don't have enough cash for this upgrade!"

    # Check if the player has enough cash
    if player.cash >= totalCost:
        # Subtract the cost from the player's cash
        player.cash -= totalCost

        # Add the upgrades to the player
        for k, v in upgradeData["attributes"].items():
            key = k.split("_")[1]  # Remove prefix from key
            # Check if the attribute is a physical attribute
            if key in league_config.attribute_categories["physical"]:
                return f"❌ '{key}' cannot be upgraded because it's a physical."
            else:
                player.attributes[key] = v["new"]

        for k, v in upgradeData["badges"].items():
            key = k.split("_")[1]  # Remove prefix from key
            player.badges[key] = v["new"]

        for k, v in upgradeData["tendencies"].items():
            key = k.split("_")[1]  # Remove prefix from key
            player.tendencies[key] = v["new"]

        # Add the totalCost to spent & add history list log
        currentTime = datetime.datetime.now()
        timestamp = currentTime.strftime("%Y-%m-%d | %H:%M:%S")
        player.spent += totalCost
        player.history_list.history["upgrade_logs"].append(
            {
                "cost": totalCost,
                "data": upgradeData,
                "timestamp": timestamp,
            }
        )
        player.upgrades_pending = True

        # Save the player & history lists
        player.save()
        player.history_list.save()

        # Return success message
        return f"✅ Congrats, you upgraded your player for ${totalCost}!"
    
