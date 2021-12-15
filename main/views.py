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
    all_values = EmployeeRole.objects.all()

    # 5: FILTER EMPLOYEES AND ROLES BY DATE IN ORDER - xx
    date_order_query = EmployeeRole.objects.all().order_by('role_date')

    return render(request, "blizzardblast/templates/schedule.html", {
        'all_values': all_values
    }
    )

# 1: FILTER EMPLOYEES BY MANAGER FOR THE DAY - mate
def manager_query(request):
    ismanager_query = EmployeeRole.objects.all().filter(is_manager='Y')
    return render(request, "blizzardblast/templates/queries/manager_query.html", {'manager': ismanager_query})

# 3 : FILTER BY WEEK - dedz
def week_query(request):
    week_query1 = EmployeeRole.objects.all().filter(
        role_date__range=["2025-09-01", "2025-09-06"]).order_by('role_date')
    week_query2 = EmployeeRole.objects.all().filter(
        role_date__range=["2025-09-08", "2025-09-13"]).order_by('role_date')
    return render(request, "blizzardblast/templates/queries/week_query.html", {
        'week_query1': week_query1, 'week_query2': week_query2
    }
    )

# 4: FILTER EMPLOYEES BY ROLES - xtine
def role_query(request):
    role_query1 = EmployeeRole.objects.all().filter(role_description='Cashier')
    role_query2 = EmployeeRole.objects.all().filter(role_description='Preparation')
    role_query3 = EmployeeRole.objects.all().filter(role_description='Cleaning')
    return render(request, "blizzardblast/templates/queries/role_query.html", {
        'cashier': role_query1, 'preparation': role_query2, 'cleaning': role_query3
    }
    )

# 2: FILTER EMPLOYEES IN ALPHABETICAL ORDER - felizia
def alphabetical_query(request):
    alphabetical_query = EmployeeRole.objects.order_by(
        'employee__employee_name')
    for i in alphabetical_query:
        print(i)

    return render(request, "blizzardblast/templates/queries/alphabetical_query.html", {
        'alphabetical': alphabetical_query
    })


def report(request):
    return render(request, "blizzardblast/templates/report.html")


def addorder(request):
    form = AddOrderForm()
    return render(request, "blizzardblast/templates/addorder.html", {'form': form})


def addinventory(request):
    form = AddInventoryForm()
    return render(request, "blizzardblast/templates/addinventory.html", {'inventory_form': form})
