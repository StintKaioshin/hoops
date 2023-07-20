from discord_webhook import DiscordWebhook, DiscordEmbed

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
