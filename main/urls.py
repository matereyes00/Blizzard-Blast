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
    
    #queries
    path('manager_query', manager_query, name='manager_query'),
    path('week_query', week_query, name='week_query'),
    path('role_query', role_query, name='role_query'),
    path('alphabetical_query', alphabetical_query, name='alphabetical_query'),
    
    # filtered views
    path('baseFlavors', baseFlavors, name='baseFlavors'),
    path('addOnIngredients', addOnIngredients, name='addOnIngredients'),
    path('receipt', receipt, name='receipt'),
    path('orderslip', orderSlip, name='orderslip'),

    #forms
    path('addorder', addorder, name='addorder'),
    path('additem', additem, name='additem'),
    path('addcustomer', addcustomer, name='addcustomer'),
    
    # CRUD - FOR ADD ONS
    path('addingredient', addingredient, name='addingredient'),
    path('update_ingredient/<str:pk>/', updateIngredient, name='update_ingredient'),
    
    # CRUD - FOR BASE FLAVORS
    path('addBaseFlavor', addbaseflavor, name='addBaseFlavor'),
    path('update_baseflavor/<str:pk>/', updateBaseFlavor, name='update_baseflavor'),

    path('addinventory', addinventory, name='addinventory'),

]
