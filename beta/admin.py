from django.contrib import admin
from beta.models import BetaRegistration, IPLog

class BetaRegistrationAdmin(admin.ModelAdmin):
    pass
admin.site.register(BetaRegistration, BetaRegistrationAdmin)

class IPLogAdmin(admin.ModelAdmin):
    pass
admin.site.register(IPLog, IPLogAdmin)