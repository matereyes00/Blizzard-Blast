# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Employee(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    employee_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'employee'


class EmployeeRole(models.Model):
    ROLES = [
        ('Cashier', 'Cashier'),
        ('Preparation', 'Preparation'),
        ('Cleaning', 'Cleaning'),
    ]

    role_date = models.DateField()
    employee = models.ForeignKey(Employee, models.DO_NOTHING)
    role_description = models.CharField(max_length=20, choices=ROLES)
    is_manager = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'employeerole'
