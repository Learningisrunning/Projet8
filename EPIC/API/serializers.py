from  rest_framework.serializers import ModelSerializer
from API.models import Sale, ClientPotentiel, ClientsExistant, Contract, Event, Support

class SaleListSerializer(ModelSerializer):
    class Meta:
        model = Sale
        fields = ['id', 'first_name', 'last_name']

class ClientPotentielListSerializer(ModelSerializer):
    class Meta:
        model = ClientPotentiel
        fields = ['id', 'first_name', 'last_name', 'company_name']

class ClientExistantsListSerializer(ModelSerializer):
    class Meta:
        model = ClientsExistant
        fields = ['id', 'first_name', 'last_name', 'company_name']

class ContractListSerializer(ModelSerializer):
    class Meta:
        model = Contract
        fields = ['id', 'date_created', 'sales_contact', 'client']

class EventListSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'date_created', 'client', 'support_contact', 'event_status']

class SupportListSerializer(ModelSerializer):
    class Meta:
        model = Support
        fields = ['id', 'first_name', 'last_name']
