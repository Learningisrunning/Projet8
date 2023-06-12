from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from API.permissions import IsaSale, IsaSupport
from API.serializers import SaleListSerializer, ClientExistantsListSerializer, ClientPotentielListSerializer, ContractListSerializer, EventListSerializer, SupportListSerializer
from API.serializers import SaleDetailSerializer, ClientExistantsDetailSerializer, ContractDetailSerializer, EventDetailsSerializer
from API.models import Sale, ClientPotentiel, ClientsExistant, Event, Contract, Support
# Create your views here.

class SalesViewtSet(ModelViewSet):
    serializer_class = SaleListSerializer
    detail_serializer_class = SaleDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Sale.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()
    
class ClientsPotentielsViewtSet(ModelViewSet):
    serializer_class = ClientPotentielListSerializer
    permission_classes = [IsAuthenticated, IsaSale]
    search_fields = ['last_name', 'email']
    filter_backends = (filters.SearchFilter,)
    

    def get_queryset(self):
        if self.action == 'list' or self.action == 'destroy' or self.action == 'update':
            user_connected = self.request.user
            sales = Sale.objects.all()

            # récupérer les client Existant en fonction du sales connecté
            if self.request.user.groups.filter(name="Sales"):
                for sale in sales:
                    if user_connected.id == sale.user_sale_id:
                        user_sales = sale.pk
                        break
                return ClientPotentiel.objects.filter(sales_contact = user_sales)
            # récupérer tous les clients si superadmin
            if self.request.user.is_superuser == True:
                return ClientPotentiel.objects.all()
            
             
    def perform_create(self, serializer):
        if self.action == 'create':
            new_client_potentiel = self.serializer_class.create(self, self.request.data)

            return new_client_potentiel
        return super().perform_create(serializer)

class ClientsExistantsViewtSet(ModelViewSet):
    serializer_class = ClientExistantsListSerializer
    detail_serializer_class = ClientExistantsDetailSerializer
    permission_classes = [IsAuthenticated, IsaSale]
    search_fields = ['last_name', 'email']
    filter_backends = (filters.SearchFilter,)
    
    

    def get_queryset(self):
        if self.action == 'list' or self.action == 'destroy' or self.action == 'update':
            user_connected = self.request.user

            events = Event.objects.all()
            sales = Sale.objects.all()
            # récupérer les client Existant en fonction du sales connecté
            if self.request.user.groups.filter(name="Sales"):
                for sale in sales:
                    if user_connected.id == sale.user_sale_id:
                        user_sales = sale.pk
                        break
                return ClientsExistant.objects.filter(sales_contact = user_sales)

            # récupérer les clients Existants en fonction du support connecté
            if self.request.user.groups.filter(name="Support"):
                clients_liste = []
                for event in events:
                    if event.support_contact.user_support_id == user_connected.id:
                        clients_liste.append(event.client_id)
                if clients_liste != []:
                    return ClientsExistant.objects.filter(id__in = clients_liste )
                
            if self.request.user.is_superuser == True:
                return ClientsExistant.objects.all()

    def perform_create(self, serializer):
        if self.action == 'create':
            new_client_existant = self.serializer_class.create(self, self.request.data)

            return new_client_existant
        return super().perform_create(serializer)

        
    
    def get_serializer_class(self):
        if self.action == "retrieve":
            return self.detail_serializer_class
        return super().get_serializer_class()
    
class ContractViewtSet(ModelViewSet):
    serializer_class = ContractListSerializer
    detail_serializer_class = ContractDetailSerializer
    permission_classes = [IsAuthenticated, IsaSale]
    search_fields = ['client__last_name', 'client__email', 'date_created', 'amount']
    filter_backends = (filters.SearchFilter,)

    def get_queryset(self):
        user_connected = self.request.user
        sales = Sale.objects.all()

        # récupérer les client Existant en fonction du sales connecté
        if self.request.user.groups.filter(name="Sales"):
            for sale in sales:
                if user_connected.id == sale.user_sale_id:
                    user_sales = sale.pk
                    break
            return Contract.objects.filter(sales_contact = user_sales)

        if self.request.user.is_superuser == True:
            return Contract.objects.all()
        

    def get_serializer_class(self):
        if self.action == "retrieve":
            return self.detail_serializer_class
        return super().get_serializer_class()

class EventViewtSet(ModelViewSet):
    serializer_class = EventListSerializer
    detail_serializer_class = EventDetailsSerializer
    permission_classes = [IsAuthenticated,IsaSupport]
    search_fields = ['client__last_name', 'client__email', 'date_created']
    filter_backends = (filters.SearchFilter,)

    def get_queryset(self):
        if self.action == 'list' or self.action == 'destroy' or self.action == 'update':
            user_connected = self.request.user
            events = Event.objects.all()
            supports = Support.objects.all()

            if self.request.user.groups.filter(name="Support"):
                    clients_liste = []
                    for support in supports:
                        if support.user_support == user_connected:
                            support_is = support
                            break
                    for event in events:
                        if event.support_contact == support_is:
                            clients_liste.append(event.client_id)
                    if clients_liste != []:
                        return Event.objects.filter(client_id__in = clients_liste )

            if self.request.user.is_superuser == True:
                    return Event.objects.all()
        
    def perform_create(self, serializer):
        if self.action == 'create':
            new_event = self.serializer_class.create(self, self.request.data)

            return new_event
        return super().perform_create(serializer)
   
        

    def get_serializer_class(self):
        if self.action == "retrieve" :
            return self.detail_serializer_class
        return super().get_serializer_class()
    
class SupportViewtSet(ModelViewSet):
    serializer_class = SupportListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Support.objects.all()
    
