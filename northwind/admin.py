from django.contrib import admin
from .models import *

admin.site.register(Supplier)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(Shipper)
admin.site.register(Region)
admin.site.register(Territory)
admin.site.register(EmployeeTerritory)
admin.site.register(Order)
admin.site.register(OrderDetail)
