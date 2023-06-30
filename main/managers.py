from django.contrib.auth import models


class DiscordAuthorizationManager(models.UserManager):
    def create_discord_user(self, user):
        discord_tag = "%s#%s" % (user["username"], user["discriminator"])
        new_user = self.create(
            id=user["id"],
            discord_tag=discord_tag,
            avatar=user["avatar"],
            public_flags=user["public_flags"],
            flags=user["flags"],
            locale=user["locale"],
            mfa_enabled=user["mfa_enabled"],
        )
        return new_user
