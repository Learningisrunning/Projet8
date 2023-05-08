from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
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
    permission_classes = [IsAuthenticated]
    search_fields = ['last_name', 'email']
    filter_backends = (filters.SearchFilter,)
    

    def get_queryset(self):
        return ClientPotentiel.objects.all()

class ClientsExistantsViewtSet(ModelViewSet):
    serializer_class = ClientExistantsListSerializer
    detail_serializer_class = ClientExistantsDetailSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ['last_name', 'email']
    filter_backends = (filters.SearchFilter,)
    

    def get_queryset(self):
        return ClientsExistant.objects.all()
    
    def get_serializer_class(self):
        if self.action == "retrieve":
            return self.detail_serializer_class
        return super().get_serializer_class()
    
class ContractViewtSet(ModelViewSet):
    serializer_class = ContractListSerializer
    detail_serializer_class = ContractDetailSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ['client__last_name', 'client__email', 'date_created', 'amount']
    filter_backends = (filters.SearchFilter,)

    def get_queryset(self):
        return Contract.objects.all()
    def get_serializer_class(self):
        if self.action == "retrieve":
            return self.detail_serializer_class
        return super().get_serializer_class()

class EventViewtSet(ModelViewSet):
    serializer_class = EventListSerializer
    detail_serializer_class = EventDetailsSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ['client__last_name', 'client__email', 'date_created']
    filter_backends = (filters.SearchFilter,)

    def get_queryset(self):
        return Event.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return self.detail_serializer_class
        return super().get_serializer_class()
    
class SupportViewtSet(ModelViewSet):
    serializer_class = SupportListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Support.objects.all()
    
