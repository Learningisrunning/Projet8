from  rest_framework.serializers import ModelSerializer
from API.models import Sale, ClientPotentiel, ClientsExistant, Contract, Event, Support


#Serializer des clients potentiels 
class ClientPotentielListSerializer(ModelSerializer):
    class Meta:
        model = ClientPotentiel
        fields = ['id', 'first_name', 'last_name', 'company_name']
    
    def create(self, validated_data):

        sales = Sale.objects.all()

        for sale in sales:
            if sale.id == validated_data['sales_contact']:
                sale_contact = sale
                break

        new_client_potentiels = ClientPotentiel()
        new_client_potentiels.first_name = validated_data['first_name']
        new_client_potentiels.last_name = validated_data['last_name']
        new_client_potentiels.email = validated_data['email']
        new_client_potentiels.phone = validated_data['phone']
        new_client_potentiels.mobile = validated_data['mobile']
        new_client_potentiels.company_name = validated_data['company_name']
        new_client_potentiels.date_created = validated_data['date_created']
        new_client_potentiels.date_update = validated_data['date_updated']
        new_client_potentiels.sales_contact = sale_contact

        new_client_potentiels.save()

        return new_client_potentiels


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

    def create(self, validated_data):

        client_existant = ClientsExistant.objects.filter(id = validated_data['client'])
        support = Support.objects.filter( id = validated_data['support_contact'])
        event_status = Contract.objects.filter(id = validated_data['event_status'])


        new_event = Event()
        new_event.date_created = validated_data['date_created']
        new_event.date_update = validated_data['date_update']
        new_event.attendees = validated_data['attendees']
        new_event.event_date = validated_data['event_date']
        new_event.note = validated_data['note']
        new_event.client = client_existant[0]
        new_event.support_contact = support[0]
        new_event.event_status = event_status[0]
      

        new_event.save()

        return new_event

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
        fields = ['id', 'first_name', 'last_name', 'sales_contact']

    def create(self, validated_data):

        sales = Sale.objects.all()

        for sale in sales:
            if sale.id == validated_data['sales_contact']:
                sale_contact = sale
                break

        new_client_existant = ClientsExistant()
        new_client_existant.first_name = validated_data['first_name']
        new_client_existant.last_name = validated_data['last_name']
        new_client_existant.email = validated_data['email']
        new_client_existant.phone = validated_data['phone']
        new_client_existant.mobile = validated_data['mobile']
        new_client_existant.company_name = validated_data['company_name']
        new_client_existant.date_created = validated_data['date_created']
        new_client_existant.date_update = validated_data['date_updated']
        new_client_existant.sales_contact = sale_contact

        new_client_existant.save()

        return new_client_existant

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