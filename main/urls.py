from django.urls import path, include
from .views import *

urlpatterns = [
    # main views
    path('', homepage, name='homepage'),
    # order view
    path('order', order, name='order'),
    path('receipt', receipt, name='receipt'),
    path('inventory', inventory, name='inventory'),
    path('schedule', schedule, name='schedule'),
    path('report', report, name='report'),
    

    #forms
    path('addorder', addorder, name='addorder'),
    path('additem', additem, name='additem'),
    path('addcustomer', addcustomer, name='addcustomer'),
    path('addingredient', addingredient, name='addingredient'),
    path('addBaseFlavor', addbaseflavor, name='addBaseFlavor'),
    path('addinventory', addinventory, name='addinventory'),

    #queries
    path('manager_query', manager_query, name='manager_query'),
    path('week_query', week_query, name='week_query'),
    path('role_query', role_query, name='role_query'),
    path('alphabetical_query', alphabetical_query, name='alphabetical_query')

]
