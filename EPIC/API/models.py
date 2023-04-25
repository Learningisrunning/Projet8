from django.db import models

# Create your models here.

class Sales(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)

    __str__ = first_name + "." + last_name

class Client(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    company_name = models.CharField(max_length=250)
    date_created = models.DateField()
    date_update = models.DateField()
    sales_contact = models.ForeignKey(Sales, on_delete=models.SET_NULL)

    __str__ = first_name + "." + last_name

class ClientsExistants(Client):
    
    __str__ = Client.first_name

class ClientPotentiels(Client):
    __str__ = Client.first_name

class Contract(models.Model):
    date_created = models.DateField()
    date_update = models.DateField()
    status = models.BooleanField()
    amount = models.FloatField()
    payment_due = models.DateField()
    sales_contact = models.ForeignKey(Sales, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    __str__ = sales_contact + "    " + client

class Support(models.Model):

    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)

    __str__ = first_name + "." + last_name

class Event(models.Model):

    date_created = models.DateField()
    date_update = models.DateField()
    attendees = models.IntegerField()
    event_date = models.DateField()
    note = models.CharField(max_length=350)
    client = models.ForeignKey(Client)
    support_contact = models.ForeignKey(Support)
    event_status = models.ForeignKey(Contract.status)


    __str__ = client + "  " + event_date + "  " + support_contact



