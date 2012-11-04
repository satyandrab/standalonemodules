from django.contrib import admin
from beta.models import BetaRegistration

class BetaRegistrationAdmin(admin.ModelAdmin):
    pass
admin.site.register(BetaRegistration, BetaRegistrationAdmin)