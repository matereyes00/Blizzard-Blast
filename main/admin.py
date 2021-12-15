from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(Orders)
admin.site.register(Employee)
admin.site.register(EmployeeRole)
admin.site.register(Customer)
admin.site.register(BaseFlavor)
admin.site.register(Size)

admin.site.register(Item)
admin.site.register(Ingredient)
