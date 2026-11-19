from django.contrib import admin
from product.models import Product
from product.models import Customer
from product.models import Order

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
# Register your models here.
