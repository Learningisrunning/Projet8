"""EPIC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from API.views import SalesViewtSet, ClientsPotentielsViewtSet, ClientsExistantsViewtSet, ContractViewtSet, EventViewtSet, SupportViewtSet
from rest_framework import routers
from rest_framework_nested import routers

#router sales
router_sales = routers.SimpleRouter()
router_sales.register('sales', SalesViewtSet, basename='sales')

#router clients potentiels
router_clients_potentiels = routers.NestedSimpleRouter(router_sales, r'sales', lookup = 'sales')
router_clients_potentiels.register(r'clients-potentiels', ClientsPotentielsViewtSet, basename='clients-potentiels')

#router clients existants
router_clients_existants = routers.NestedSimpleRouter(router_sales, r'sales', lookup = 'sales')
router_clients_existants.register(r'clientsExistants', ClientsExistantsViewtSet, basename='clients-existants')

#router contract
router_contract = routers.NestedSimpleRouter(router_clients_existants, r'clientsExistants', lookup = 'clientsExistants')
router_contract.register(r'contracts', ContractViewtSet, basename='contracts')

#router event
router_event = routers.NestedSimpleRouter(router_contract, r'contracts', lookup = 'contracts')
router_event.register(r'event', EventViewtSet, basename='event')

#router suppport
router_support = routers.NestedSimpleRouter(router_event, r'event', lookup = 'event')
router_support.register(r'support', SupportViewtSet, basename='support')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router_sales.urls)),
    path('api/', include(router_clients_potentiels.urls)),
    path('api/', include(router_clients_existants.urls)),
    path('api/', include(router_contract.urls)),
    path('api/', include(router_event.urls)),
    path('api/', include(router_support.urls)),
]
