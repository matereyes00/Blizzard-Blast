from django.urls import path, include
from .views import *

urlpatterns = [
    path('', homepage, name='homepage'),
    path('order', order, name='order'),
    path('inventory', inventory, name='inventory'),
    path('schedule', schedule, name='schedule'),
    path('report', report, name='report'),
    path('receipt', receipt, name='receipt'),
    path('addorder', addorder, name='addorder' ),
    path('addinventory', addinventory, name='addinventory')
]
