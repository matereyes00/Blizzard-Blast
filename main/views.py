from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import *
from .models import *


# ========================== MAIN VIEWS ==========================
def homepage(request):
    return render(request, "blizzardblast/templates/index.html")

# ========================== ORDERS =====================================
def order(request):
    return render(request, "blizzardblast/templates/order.html")

def orderSlip(request):
    orders_context = Orders.objects.all()
    return render(request, "blizzardblast/templates/filtered_views/orderslip.html", {'orders': orders_context})

def receipt(request):
    return render(request, "blizzardblast/templates/filtered_views/receipt.html")

# ========================== INVENTORY =====================================
def inventory(request):
    return render(request, "blizzardblast/templates/inventory.html")

# ADD ONS / INGREDIENTS
def addOnIngredients(request):
    ingredients_context = Ingredient.objects.all()

    contexts = {
        'inventory' : ingredients_context
    }

    return render(request, "blizzardblast/templates/filtered_views/addons_ingredient.html", contexts)

# BASE FLAVORS 
def baseFlavors(request):
    show_bfs = BaseFlavor.objects.all()
    contexts = {
        'show_bfs' : show_bfs
    }
    return render(request, "blizzardblast/templates/filtered_views/baseFlavors.html", contexts)

def schedule(request):
    all_values = EmployeeRole.objects.all()
    return render(request, 
        "blizzardblast/templates/schedule.html", 
        {'all_values': all_values}
    )

def report(request):
    return render(request, "blizzardblast/templates/report.html")

# ========================== SCHEDULE QUERIES ==========================
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


# ========================== FORMS ==========================
def addorder(request):
    form = AddOrderForm()
    context = {'form': form }
    
    if request.method == 'POST':
        #print("Printing post: ", request.POST)
        form = AddOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/order')

    return render(request, "blizzardblast/templates/forms/addorder.html", context)

def additem(request):
    form = AddItemForm()
    context = {'form':form}
    if request.method == 'POST':
        form = AddItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/order')
    return render(request, "blizzardblast/templates/forms/additem.html", context)

def addcustomer(request):
    form = AddCustomerForm()
    context = {'form':form}
    if request.method == 'POST':
        form = AddCustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/order')
    return render(request, "blizzardblast/templates/forms/addcustomer.html", context)

def addingredient(request):
    form = AddIngredient()
    context = {'form':form}
    if request.method == 'POST':
        form = AddIngredient(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/inventory')
    return render(request, "blizzardblast/templates/forms/addingredient.html", context)

def updateIngredient(request,pk):
    ingredient = Ingredient.objects.get(ingredient_id=pk)
    form = AddIngredient(instance=ingredient)
    context = {'form':form}
    # this handles updating the values in the form
    if request.method == 'POST':
        form = AddIngredient(request.POST, instance=ingredient)
        if form.is_valid():
            form.save()
            return redirect('/inventory')
    return render(request, "blizzardblast/templates/forms/addingredient.html", context)

def addbaseflavor(request):
    form = AddBaseFlavor()
    context = {'form':form}
    
    if request.method == 'POST':
        form = AddBaseFlavor(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/inventory')
    
    return render(request, "blizzardblast/templates/forms/addBaseFlavor.html", context)

def updateBaseFlavor(request,pk):
    bf = BaseFlavor.objects.get(bf_id=pk)
    form = AddBaseFlavor(instance=bf)
    context = {'form':form}
    # this handles updating the values in the form
    if request.method == 'POST':
        form = AddBaseFlavor(request.POST, instance=bf)
        if form.is_valid():
            form.save()
            return redirect('/inventory')
    return render(request, "blizzardblast/templates/forms/addBaseFlavor.html", context)

def addinventory(request):
    form = AddInventoryForm()
    return render(request, "blizzardblast/templates/forms/addinventory.html", {'form':form})
