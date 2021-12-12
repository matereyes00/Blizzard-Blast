from django.shortcuts import render
from django.http import HttpResponse

from .forms import AddInventoryForm, AddOrderForm
from .models import *


def homepage(request):
    return render(request, "blizzardblast/templates/index.html")


def order(request):
    return render(request, "blizzardblast/templates/order.html")


def receipt(request):
    return render(request, "blizzardblast/templates/receipt.html")


def inventory(request):
    return render(request, "blizzardblast/templates/inventory.html")


def schedule(request):
    # 1: FILTER EMPLOYEES BY MANAGER FOR THE DAY - mate
    ismanager_query = EmployeeRole.objects.all().filter(is_manager='Y')
    
    # 2: FILTER EMPLOYEES AND ROLES IN ALPHABETICAL ORDER - felizia
    employee_role_order_query = EmployeeRole.objects.all().order_by('role_description')

    # 3 : FILTER BY WEEK - dedz
    week_query1 = EmployeeRole.objects.all().filter(role_date__range=["2025-09-01", "2025-09-06"]).order_by('role_date') 
    week_query2 = EmployeeRole.objects.all().filter(role_date__range=["2025-09-08", "2025-09-13"]).order_by('role_date')

    # 4: FILTER EMPLOYEES BY ROLES - xtine
    role_query1 = EmployeeRole.objects.all().filter(role_description='Cashier')
    role_query2 = EmployeeRole.objects.all().filter(role_description='Preparation')
    role_query3 = EmployeeRole.objects.all().filter(role_description='Cleaning')

    # 5: FILTER EMPLOYEES AND ROLES BY DATE IN ORDER - xx
    date_order_query = EmployeeRole.objects.all().order_by('role_date')

    return render(request, "blizzardblast/templates/schedule.html", {
        'manager': ismanager_query
        }
    )



def report(request):
    return render(request, "blizzardblast/templates/report.html")


def addorder(request):
    form = AddOrderForm()
    return render(request, "blizzardblast/templates/addorder.html", {'form': form})

def addinventory(request):
    form = AddInventoryForm()
    return render(request, "blizzardblast/templates/addinventory.html", {'inventory_form':form})
