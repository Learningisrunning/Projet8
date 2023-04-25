from django.contrib import admin
from models import ClientPotentiels, ClientsExistants, Event, Support, Sales, Contract
# Register your models here.

admin.site.register(ClientPotentiels)
admin.site.register(ClientsExistants)
admin.site.register(Event)
admin.site.register(Support)
admin.site.register(Sales)
admin.site.register(Contract)
