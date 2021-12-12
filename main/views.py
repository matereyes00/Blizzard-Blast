from django.shortcuts import render
from django.http import HttpResponse

from .forms import AddOrderForm
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

    # 😁 filter employees and roles by date in order
    for row in EmployeeRole.objects.raw('''SELECT * FROM employeerole RIGHT JOIN employee ON (employeerole.employee_id=employee.employee_id)
     ORDER BY role_date ASC'''):
        print(row.employee_name, row.role_description, row.role_date)

    # 😁 filter employees and roles in alphabetical order
    for row in EmployeeRole.objects.raw('''SELECT * FROM employeerole RIGHT JOIN employee ON (employeerole.employee_id=employee.employee_id)
     ORDER BY employee_name, role_date ASC'''):
        print(row.employee_name, row.role_description, row.role_date)

    # 😁 filter employees by roles
    for row in EmployeeRole.objects.raw('''SELECT role_id,employee_name, role_date FROM employeerole RIGHT JOIN employee ON (employeerole.employee_id=employee.employee_id)
    WHERE role_description ILIKE 'cashier' '''):
        print(row.employee_name, row.role_description, row.role_date, '- filter by roles')

    # 😁 filter employees by manager for the day
    for row in EmployeeRole.objects.raw('''SELECT role_id,employee_name, role_date FROM employeerole RIGHT JOIN employee ON (employeerole.employee_id=employee.employee_id)
    WHERE is_manager ILIKE 'Y' '''):

        print(row.employee_name, row.role_description, row.role_date, '- manager for the day')

    # 😁 filter employees by week
    for row in EmployeeRole.objects.raw('''SELECT * FROM employeerole RIGHT JOIN employee ON (employeerole.employee_id=employee.employee_id)
    WHERE role_date <= '2025-09-06' AND role_date >= '2025-09-01' ORDER BY role_date '''):
        pass

    # 1: FILTER EMPLOYEES BY MANAGER FOR THE DAY 
    ismanager_query = EmployeeRole.objects.all().filter(is_manager='Y')
    
    # 2: FILTER EMPLOYEES AND ROLES IN ALPHABETICAL ORDER
    employee_role_order_query = EmployeeRole.objects.all().order_by('role_description')

    # 3 : FILTER BY WEEK
    week_query1 = EmployeeRole.objects.all().filter(role_date__range=["2025-09-01", "2025-09-06"]).order_by('role_date') 
    week_query2 = EmployeeRole.objects.all().filter(role_date__range=["2025-09-08", "2025-09-13"]).order_by('role_date')

    # 4: FILTER EMPLOYEES BY ROLES
    role_query1 = EmployeeRole.objects.all().filter(role_description='Cashier')
    role_query2 = EmployeeRole.objects.all().filter(role_description='Preparation')
    role_query3 = EmployeeRole.objects.all().filter(role_description='Cleaning')

    # 5: FILTER EMPLOYEES AND ROLES BY DATE IN ORDER 
    date_order_query = EmployeeRole.objects.all().order_by('role_date')

    return render(request, "blizzardblast/templates/schedule.html", {
        'manager': employee_role_order_query
        }
    )


def report(request):
    return render(request, "blizzardblast/templates/report.html")


def addorder(request):
    form = AddOrderForm()
    return render(request, "blizzardblast/templates/addorder.html", {'form': form})
