# Django imports
from django.contrib import admin
from django.db.models.fields.json import JSONField

# Third party imports
from jsoneditor.forms import JSONEditor

# Model imports
from .models import DiscordUser
from .models import Player
from .models import HistoryList
from .models import Team
from .models import Coupon
from .models import Transaction
from .models import Transactions
from .models import TradeOffer
from .models import ContractOffer
from .models import Notification
from .models import Award


# Override the default JSONField widget with the JSONEditor widget
class MyAdmin(admin.ModelAdmin):
    formfield_overrides = {
        JSONField: {"widget": JSONEditor},
    }


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'logo', 'abbrev', 'plays_in_main_league', 'show_on_lists', 'is_college_team']
    list_editable = ['is_college_team']
    formfield_overrides = {
        JSONField: {"widget": JSONEditor},
    }

# Register your models here.
admin.site.register(DiscordUser, MyAdmin)
admin.site.register(Player, MyAdmin)
admin.site.register(HistoryList, MyAdmin)
admin.site.register(Coupon, MyAdmin)
admin.site.register(Transaction, MyAdmin)
admin.site.register(Transactions, MyAdmin)
admin.site.register(TradeOffer, MyAdmin)
admin.site.register(ContractOffer, MyAdmin)
admin.site.register(Notification, MyAdmin)
admin.site.register(Award, MyAdmin)
