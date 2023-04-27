from django.contrib import admin
from API.models import ClientPotentiel, ClientsExistant, Event, Support, Sale, Contract, User
# Register your models here.


#admin.site.register(ClientPotentiel)
#admin.site.register(ClientsExistant)
#admin.site.register(Event)
#admin.site.register(Support)
#admin.site.register(Sale)
#admin.site.register(Contract)
admin.site.register(User)

@admin.register(ClientPotentiel)
class ClientPotentielAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','company_name', 'sales_contact')
    ordering = ('sales_contact',)
    search_fields = ('first_name', 'sales_contact__first_name')
    list_filter = ('company_name', 'sales_contact__first_name')

@admin.register(ClientsExistant)
class ClientsExistantsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','company_name', 'sales_contact')
    ordering = ('sales_contact',)
    search_fields = ('first_name', 'sales_contact__first_name')
    list_filter = ('company_name', 'sales_contact__first_name')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('event_date', 'attendees', 'client', 'support_contact')
    ordering = ('event_date',)
    search_fields = ('event_date', 'attendees', 'client__first_name', 'support_contact__first_name')
    list_filter = ('event_date', 'client__company_name', 'support_contact__first_name')

@admin.register(Support)
class SupportAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    ordering = ('first_name',)
    search_fields = ('first_name', 'last_name')
    list_filter = ('first_name', 'last_name')

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    ordering = ('first_name',)
    search_fields = ('first_name', 'last_name')
    list_filter = ('first_name', 'last_name')

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('date_created', 'date_update', 'payment_due', 'sales_contact', 'client')
    ordering = ('payment_due',)
    search_fields = ('date_created', 'payment_due', 'sales_contact__first_name', 'client__first_name')
    list_filter = ('date_created', 'payment_due', 'sales_contact__first_name', 'client__first_name')
