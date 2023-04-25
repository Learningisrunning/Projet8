from django.contrib import admin
from API.models import ClientPotentiel, ClientsExistant, Event, Support, Sale, Contract, User
# Register your models here.


admin.site.register(ClientPotentiel)
admin.site.register(ClientsExistant)
admin.site.register(Event)
admin.site.register(Support)
admin.site.register(Sale)
admin.site.register(Contract)
admin.site.register(User)