# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.db.models.fields import *


class BaseFlavor(models.Model):
    bf_id = models.AutoField(primary_key=True)
    bf_name = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'base_flavor'
    def __str__(self):
        return self.bf_name

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    
    class Meta:
        managed = False
        db_table = 'customer'

    def __str__(self):
        return self.customer_name

class Ingredient(models.Model):
    INGREDIENT_CATEGORIES = [
        ('nuts','nuts'),
        ('fruits','fruits'),
        ('chocolate','chocolate'),
        ('baked','baked'),
        ('mix-in','mix-in'),
        # ('base','base'),
        ('topping','topping')
    ]
    
    REPLENISHED_STOCK = [
        ('Y', 'Y'),
        ('N', 'N'),
    ]

    ingredient_id = models.AutoField(primary_key=True)
    ingredient_name = models.CharField(max_length=255, blank=True)
    category = models.CharField(max_length=200, choices=INGREDIENT_CATEGORIES)
    quantity = models.IntegerField()
    price_per_serving = models.FloatField()
    replenished_stock = models.CharField(max_length=1, choices=REPLENISHED_STOCK)

    class Meta:
        managed = False
        db_table = 'ingredient'

    def __str__(self):
        return self.ingredient_name

class Size(models.Model):
    SIZES = [
        ('8', '8'),
        ('12', '12'),
        ('16', '16'),
    ] 

    size_id = models.AutoField(primary_key=True)
    serv_size = models.CharField(max_length=100, choices=SIZES)

    class Meta:
        managed = False
        db_table = 'size'

    def __str__(self):
        return str(self.serv_size)

class Employee(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    employee_name = models.CharField(max_length=255)

    def __str__(self):
        return self.employee_name

    class Meta:
        managed = False
        db_table = 'employee'


class EmployeeRole(models.Model):
    ROLES = [
        ('Cashier', 'Cashier'),
        ('Preparation', 'Preparation'),
        ('Cleaning', 'Cleaning'),
    ]

    IS_MANAGER = [
        ('Y', 'Y'),
        ('N', 'N'),
    ]

    role_id = models.AutoField(primary_key=True)
    role_date = models.DateField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    role_description = models.CharField(max_length=20, choices=ROLES)
    is_manager = models.CharField(max_length=1, choices=IS_MANAGER)

    def __str__(self):
        return self.employee.employee_name + " is tasked for " + self.role_description
    
    class Meta:
        managed = False
        db_table = 'employeerole'

class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    bf = models.ForeignKey(BaseFlavor, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    io_quantity = models.IntegerField()
    total_sales = models.FloatField()

    def __str__(self):
        return self.bf.bf_name + " with " + self.ingredient.ingredient_name + "  || size: " + str(self.size.serv_size)
    class Meta:
        managed = False
        db_table = 'item'

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    order_date = models.DateField()
    class Meta:
        managed = False
        db_table = 'orders'
        verbose_name_plural = "Orders"

    def __str__(self):
        return self.customer.customer_name + " ordered " + str(self.item) + "  from: " + self.employee.employee_name + " on " + str(self.order_date)