from  rest_framework.serializers import ModelSerializer
from API.models import Sale, ClientPotentiel, ClientsExistant, Contract, Event, Support


#Serializer des clients potentiels 
class ClientPotentielListSerializer(ModelSerializer):
    class Meta:
        model = ClientPotentiel
        fields = ['id', 'first_name', 'last_name', 'company_name']


#Serializer des supports
class SupportListSerializer(ModelSerializer):
    class Meta:
        model = Support
        fields = ['id', 'first_name', 'last_name']

#Serializer des events
class EventListSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'date_created', 'client']

class EventDetailsSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'date_created', 'client', 'support_contact', 'event_status']

#Serializer des contrats 
class ContractListSerializer(ModelSerializer):
    class Meta:
        model = Contract
        fields = ['id', 'date_created', 'sales_contact', 'client']

class ContractDetailSerializer(ModelSerializer):
    event_contract = EventListSerializer(many = True)

    class Meta:
        model = Contract
        fields = ['id', 'date_created', 'sales_contact', 'client', 'event_contract']

#Serializer des Clients Existants
class ClientExistantsListSerializer(ModelSerializer):
    class Meta:
        model = ClientsExistant
        fields = ['id', 'first_name', 'last_name']

class ClientExistantsDetailSerializer(ModelSerializer):
    client_contract = ContractListSerializer(many = True)
    class Meta:
        model = ClientsExistant
        fields = ['id', 'first_name', 'last_name', 'company_name', 'client_contract']

#serializer des Sales 
class SaleListSerializer(ModelSerializer):
    class Meta:
        model = Sale
        fields = ['id', 'first_name', 'last_name']

class SaleDetailSerializer(ModelSerializer):
    sales_contact_client = ClientExistantsListSerializer(many = True) 
    class Meta:
        model = Sale
        fields = ['id', 'first_name', 'last_name', 'sales_contact_client']