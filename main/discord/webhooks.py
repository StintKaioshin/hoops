from discord_webhook import DiscordWebhook, DiscordEmbed

webhook_urls = {
    "upgrade": "https://discord.com/api/webhooks/1131755543451668560/DFXdYbF8_sz-8VoXT23AbEyi_NTDk3HK-fF3sgpCWLdf2TP7hxelqKLp90Xc8tpy6X8Y",
    "creation": "https://discord.com/api/webhooks/1131755543451668560/DFXdYbF8_sz-8VoXT23AbEyi_NTDk3HK-fF3sgpCWLdf2TP7hxelqKLp90Xc8tpy6X8Y",
    "coupon": "https://discord.com/api/webhooks/1131755543451668560/DFXdYbF8_sz-8VoXT23AbEyi_NTDk3HK-fF3sgpCWLdf2TP7hxelqKLp90Xc8tpy6X8Y",
    "cash": "https://discord.com/api/webhooks/1131755543451668560/DFXdYbF8_sz-8VoXT23AbEyi_NTDk3HK-fF3sgpCWLdf2TP7hxelqKLp90Xc8tpy6X8Y",
    "trade": "https://discord.com/api/webhooks/1131755543451668560/DFXdYbF8_sz-8VoXT23AbEyi_NTDk3HK-fF3sgpCWLdf2TP7hxelqKLp90Xc8tpy6X8Y",
    "style": "https://discord.com/api/webhooks/1131755543451668560/DFXdYbF8_sz-8VoXT23AbEyi_NTDk3HK-fF3sgpCWLdf2TP7hxelqKLp90Xc8tpy6X8Y",
}

default_webhook_msg = "Webhook test message"


def send_webhook(url, title="", message=""):
    # Create the webhook
    webhook = DiscordWebhook(url=webhook_urls[url])
    # Create an embed
    webhook_embed = DiscordEmbed(title=title, description=message, color="03b2f8")
    webhook_embed.set_timestamp()
    webhook_embed.set_footer(text="Powered by virtualbl.com")
    # Add embed object to webhook
    webhook.add_embed(webhook_embed)
    # Send webhook
    webhook.execute()
