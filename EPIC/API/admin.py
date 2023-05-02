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

    def get_queryset(self, request):
         user_involve = ""
         sales = Sale.objects.all()

         for sale in sales:
              if sale.user_sale_id == request.user.id:
                    user_involve = sale
                    break
        
         qs = super().get_queryset(request)
   
         if request.user.is_superuser:
              return qs
         return qs.filter(sales_contact = user_involve)

         
@admin.register(ClientsExistant)
class ClientsExistantsAdmin(admin.ModelAdmin):
    
    list_display = ('first_name', 'last_name','company_name', 'sales_contact')
    ordering = ('sales_contact',)
    search_fields = ('first_name', 'sales_contact__first_name')
    list_filter = ('company_name', 'sales_contact__first_name')

    def get_queryset(self, request):
        user_involve_sale = ""
        user_involve_support = ""
        sales = Sale.objects.all()
        supports = Support.objects.all()
         
        for sale in sales:
              if sale.user_sale_id == request.user.id:
                    user_involve_sale = sale
                    break
        
        for support in supports:
              if support.user_support_id == request.user.id:
                    user_involve_support = support
                    break
         
        events = Event.objects.filter(support_contact=user_involve_support)

        list_of_client = []
        for event in events:
             list_of_client.append(event.client_id)
        
        qs = super().get_queryset(request)

        if request.user.is_superuser:
              return qs
        elif user_involve_sale != "":
            return qs.filter(sales_contact = user_involve_sale)
        else: 
            return qs.filter(id__in = list_of_client) 
              

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('event_date', 'attendees', 'client', 'support_contact')
    ordering = ('event_date',)
    search_fields = ('event_date', 'attendees', 'client__first_name', 'support_contact__first_name')
    list_filter = ('event_date', 'client__company_name', 'support_contact__first_name')

    def get_queryset(self, request):
         user_involve = ""
         supports = Support.objects.all()

         for support in supports:
              if support.user_support_id == request.user.id:
                    user_involve = support
                    break
        
         qs = super().get_queryset(request)
  
         if request.user.is_superuser:
              return qs
         return qs.filter(support_contact = user_involve)

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

    def get_queryset(self, request):
         user_involve = ""
         sales = Sale.objects.all()

         for sale in sales:
              if sale.user_sale_id == request.user.id:
                    user_involve = sale
                    break
        
         qs = super().get_queryset(request)
   
         if request.user.is_superuser:
              return qs
         return qs.filter(sales_contact = user_involve)