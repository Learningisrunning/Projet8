from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from API.serializers import SaleListSerializer, ClientExistantsListSerializer, ClientPotentielListSerializer, ContractListSerializer, EventListSerializer, SupportListSerializer
from API.models import Sale, ClientPotentiel, ClientsExistant, Event, Contract, Support
# Create your views here.

class SalesViewtSet(ModelViewSet):
    serializer_class = SaleListSerializer

    def get_queryset(self):
        return Sale.objects.all()
    
class ClientsPotentielsViewtSet(ModelViewSet):
    serializer_class = ClientPotentielListSerializer

    def get_queryset(self):
        return ClientPotentiel.objects.all()

class ClientsExistantsViewtSet(ModelViewSet):
    serializer_class = ClientExistantsListSerializer

    def get_queryset(self):
        return ClientsExistant.objects.all()
    
class ContractViewtSet(ModelViewSet):
    serializer_class = ContractListSerializer

    def get_queryset(self):
        return Contract.objects.all()

class EventViewtSet(ModelViewSet):
    serializer_class = EventListSerializer

    def get_queryset(self):
        return Event.objects.all()
    
class SupportViewtSet(ModelViewSet):
    serializer_class = SupportListSerializer

    def get_queryset(self):
        return Support.objects.all()
    
