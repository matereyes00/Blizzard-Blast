from django.shortcuts import render
from django.http import HttpResponse


def homepage(request):
    return render(request, "blizzardblast/templates/index.html")


def order(request):
    return render(request, "blizzardblast/templates/order.html")


def inventory(request):
    return render(request, "blizzardblast/templates/inventory.html")


def schedule(request):
    return render(request, "blizzardblast/templates/schedule.html")


def report(request):
    return render(request, "blizzardblast/templates/report.html")
