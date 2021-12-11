from django.shortcuts import render
from django.http import HttpResponse

from .forms import AddInventoryForm, AddOrderForm


def homepage(request):
    return render(request, "blizzardblast/templates/index.html")

def order(request):
    return render(request, "blizzardblast/templates/order.html")

def receipt(request):
    return render(request, "blizzardblast/templates/receipt.html")

def inventory(request):
    return render(request, "blizzardblast/templates/inventory.html")

def schedule(request):
    return render(request, "blizzardblast/templates/schedule.html")

def report(request):
    return render(request, "blizzardblast/templates/report.html")

def addorder(request):
    form = AddOrderForm()
    return render(request, "blizzardblast/templates/addorder.html", {'form': form})

def addinventory(request):
    form = AddInventoryForm()
    return render(request, "blizzardblast/templates/addinventory.html", {'inventory_form':form})