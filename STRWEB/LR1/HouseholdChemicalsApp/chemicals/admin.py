from django.contrib import admin
from .models import Employee , Product , ProductType , Manufacturer , Order , Customer
from django.contrib.auth.models import User

admin.site.register(Employee)
admin.site.register(Product)
admin.site.register(ProductType)
admin.site.register(Manufacturer)
admin.site.register(Order)
admin.site.register(Customer)
