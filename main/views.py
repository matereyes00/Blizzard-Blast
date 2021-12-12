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
    for employee in Employee.objects.raw('SELECT * FROM employee'):
        print(employee.employee_name)

    for role in EmployeeRole.objects.all():
        print(role.role_description)
    return render(request, "blizzardblast/templates/schedule.html")


def report(request):
    return render(request, "blizzardblast/templates/report.html")


def addorder(request):
    form = AddOrderForm()
    return render(request, "blizzardblast/templates/addorder.html", {'form': form})
