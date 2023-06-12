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

#router suppport
router_support = routers.SimpleRouter()
router_support.register('supports', SupportViewtSet, basename='support')

#router clients existants
router_clients_existants = routers.SimpleRouter()
router_clients_existants.register('clientsExistants', ClientsExistantsViewtSet, basename='clientsExistants')

#router clients potentiels
router_clients_potentiels = routers.SimpleRouter()
router_clients_potentiels.register('clientsPotentiels', ClientsPotentielsViewtSet, basename='clientsPotentiels')

#router contract
router_contract = routers.SimpleRouter()
router_contract.register('contracts', ContractViewtSet, basename='contracts')

#router event
router_event = routers.SimpleRouter()
router_event.register('events', EventViewtSet, basename='events')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router_sales.urls)),
    path('api/', include(router_support.urls)),
    path('api/', include(router_clients_potentiels.urls)),
    path('api/', include(router_clients_existants.urls)),
    path('api/', include(router_contract.urls)),
    path('api/', include(router_event.urls)),
]
