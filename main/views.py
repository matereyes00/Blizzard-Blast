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

    # filter employees and roles by date in order
    for row in EmployeeRole.objects.raw('''SELECT * FROM employeerole RIGHT JOIN employee ON (employeerole.employee_id=employee.employee_id)
     ORDER BY role_date ASC'''):
        print(row.employee_name, row.role_description, row.role_date)

    # filter employees and roles in alphabetical order
    for row in EmployeeRole.objects.raw('''SELECT * FROM employeerole RIGHT JOIN employee ON (employeerole.employee_id=employee.employee_id)
     ORDER BY employee_name, role_date ASC'''):
        print(row.employee_name, row.role_description, row.role_date)

    # filter employees by roles
    for row in EmployeeRole.objects.raw('''SELECT role_id,employee_name, role_date FROM employeerole RIGHT JOIN employee ON (employeerole.employee_id=employee.employee_id)
    WHERE role_description ILIKE 'cashier' '''):
        print(row.employee_name, row.role_description, row.role_date, '- filter by roles')

    # filter employees by manager for the day
    for row in EmployeeRole.objects.raw('''SELECT role_id,employee_name, role_date FROM employeerole RIGHT JOIN employee ON (employeerole.employee_id=employee.employee_id)
    WHERE is_manager ILIKE 'Y' '''):

        print(row.employee_name, row.role_description, row.role_date, '- manager for the day')

    # filter employees by week
    for row in EmployeeRole.objects.raw('''SELECT * FROM employeerole RIGHT JOIN employee ON (employeerole.employee_id=employee.employee_id)
    WHERE role_date <= '2025-09-06' AND role_date >= '2025-09-01' ORDER BY role_date '''):
        pass

        # employeeroles = {}
        # for role in EmployeeRole.objects.raw('''SELECT * FROM employeerole'''):

        # print dates when they're managers
        #     if role.is_manager == 'Y':
        #         print(role.employee.employee_name, 'is a manager on', role.role_date)
        #
        #     employeename = role.employee.employee_name
        #     employeerole = role.role_description
        #     day_mgr = []
        #     if role.employee.employee_name not in employeeroles:
        #         employeeroles[employeename] = employeerole
        #
        # print(employeeroles)

    return render(request, "blizzardblast/templates/schedule.html")


def report(request):
    return render(request, "blizzardblast/templates/report.html")


def addorder(request):
    form = AddOrderForm()
    return render(request, "blizzardblast/templates/addorder.html", {'form': form})
