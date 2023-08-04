from django.contrib.auth.backends import BaseBackend
from .models import DiscordUser


class DiscordBackend(BaseBackend):
    def authenticate(self, request, user):
        try:
            discord_user = DiscordUser.objects.get(id=user["id"])
        except DiscordUser.DoesNotExist:
            # Create new user (w/ custom manager)
            discord_user = DiscordUser.objects.create_discord_user(user)

        return discord_user

    def get_user(self, user_id):
        try:
            return DiscordUser.objects.get(pk=user_id)
        except DiscordUser.DoesNotExist:
            return None
