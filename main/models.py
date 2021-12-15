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

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'customer'

class Ingredient(models.Model):
    REPLENISHED_STOCK = [
        ('Y', 'Y'),
        ('N', 'N'),
    ]
    ingredient_id = models.AutoField(primary_key=True)
    ingredient_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price_per_serving = models.FloatField()
    replenished_stock = models.CharField(max_length=1, choices=REPLENISHED_STOCK)

    class Meta:
        managed = False
        db_table = 'ingredient'

class Size(models.Model):
    SIZES = [
        ('8', '8'),
        ('12', '12'),
        ('16', '16'),
    ] 

    size_id = models.AutoField(primary_key=True)
    serv_size = models.CharField(max_length=2, choices=SIZES)

    class Meta:
        managed = False
        db_table = 'size'


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
    employee = models.ForeignKey(Employee, models.DO_NOTHING)
    role_description = models.CharField(max_length=20, choices=ROLES)
    is_manager = models.CharField(max_length=1, choices=IS_MANAGER)

    def __str__(self):
        return self.employee.employee_name + " is tasked for " + self.role_description
    
    class Meta:
        managed = False
        db_table = 'employeerole'

class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    bf = models.ForeignKey(BaseFlavor, models.DO_NOTHING)
    ingredient = models.ForeignKey(Ingredient, models.DO_NOTHING)
    size = models.ForeignKey(Size, models.DO_NOTHING)
    io_quantity = models.IntegerField()
    total_sales = models.FloatField()

    def ingredientname(self):
        return self.ingredient.ingredient_name, self.size.serv_size, self.bf.bf_name
    class Meta:
        managed = False
        db_table = 'item'

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer, models.DO_NOTHING)
    item_id = models.ForeignKey(Item, models.DO_NOTHING)
    employee_id = models.ForeignKey(Employee, models.DO_NOTHING)
    order_date = models.DateField()
    class Meta:
        managed = False
        db_table = 'orders'