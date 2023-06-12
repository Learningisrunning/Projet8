from rest_framework.permissions import BasePermission
from API.models import Sale, Support, Event
       
class IsaSale(BasePermission):

    """Mise en place de la permission qui permet de savoir
        si un utilisateur est sales et donc de lui accorder 
        des droits en fonction"""

    message = "Seul le sale associé à ce client peut accéder à cette page"

    def has_object_permission(self, request, view, obj):

        if request.user.is_superuser == True:
            return True

        sale_obj = obj.sales_contact
        sales = Sale.objects.all()
        supports = Support.objects.all()
        events = Event.objects.all()


        for sale in sales:
            if request.user.id == sale.user_sale_id:
                user_connected = sale
                break
            else:
                user_connected = 0

        #On vérifie si le USER est le sales associé 
        
        list_methods_allow_all = ['GET']

        if request.method in list_methods_allow_all and request.user.groups.filter(name="Support"):
            user_co = request.user
            for support in supports: 
                if support.user_support_id == user_co.id:
                    for event in events:
                        if event.support_contact_id == support.id and event.client_id == obj.client_ptr_id:
                            return True
            return False

        else :
            return sale_obj == user_connected

    message = "cette page est strictement réservé au sales."

    def has_permission(self, request, view):

        if request.user.is_superuser == True:
            return True

        user_connected = request.user
        sales = Sale.objects.all()
        supports = Support.objects.all()
        events = Event.objects.all()

        list_methods_allow_supports = ['GET']


        for sale in sales:
            if user_connected.id == sale.user_sale_id:
                return True
        if request.method in list_methods_allow_supports:
            for support in supports: 
                if support.user_support_id == user_connected.id and view.basename != "clientsPotentiels" and view.basename !="contracts":
                    return True

        else:
            return False    
     


class IsaSupport(BasePermission):

    """Mise en place de la permission qui permet de savoir
        si un utilisateur est support et donc de lui accorder 
        des droits en fonction"""

    message = "Seul le support associé à cet event peut accéder à cette page"

    def has_object_permission(self, request, view, obj):

        if request.user.is_superuser == True:
            return True
        support_id = obj.support_contact_id
        supports = Support.objects.all()

        for support in supports:
            if request.user.id == support.user_support_id:
                user_connected = support
                break
            else:
                user_connected = request.user

        #On vérifie si le USER est le sales associé 
        
        return support_id == user_connected.id

    def has_permission(self, request, view):
        if request.user.is_superuser == True:
            return True
        if request.user.groups.filter(name="Support"):
            return True
        elif request.method == "POST" and request.user.groups.filter(name="Sales"):
            return True
        else:
            return False
