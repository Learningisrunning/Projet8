from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):

    def __str__(self):
        return self.username

class Sale(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    user_sale = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_sale')

    def __str__(self):
        return self.first_name + " " + self.last_name

class Client(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    company_name = models.CharField(max_length=250)
    date_created = models.DateField()
    date_update = models.DateField()
    sales_contact = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name='sales_contact_client')

    def __str__(self): 
        return self.first_name + " " + self.last_name

class ClientsExistant(Client):

    def __str__(self):
        return self.first_name + " " + self.last_name

class ClientPotentiel(Client):

   def __str__(self):
       return self.first_name + " " + self.last_name

class Contract(models.Model):
    date_created = models.DateField()
    date_update = models.DateField()
    status = models.BooleanField()
    amount = models.FloatField()
    payment_due = models.DateField()
    sales_contact = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name='sales_contact')
    client = models.ForeignKey(ClientsExistant, on_delete=models.CASCADE, related_name='client_contract')

    def __str__(self):
        return self.sales_contact.first_name + "    " + self.client.first_name

class Support(models.Model):

    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    user_support = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_support')
    
    def __str__(self):
        return self.first_name + " " + self.last_name

class Event(models.Model):

    date_created = models.DateField()
    date_update = models.DateField()
    attendees = models.IntegerField()
    event_date = models.DateField()
    note = models.CharField(max_length=350)
    client = models.ForeignKey(ClientsExistant, on_delete=models.CASCADE, related_name='client_event')
    support_contact = models.ForeignKey(Support, on_delete=models.CASCADE, related_name='support_contact')
    event_status = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name='event_contract')


    def __str__(self):
        return self.client.first_name + "  " + str(self.event_date) + "  " + self.support_contact.first_name



