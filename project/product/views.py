from django.shortcuts import render
from product.models import Product, Customer, Order



products = Product.objects.filter(name__exact = "iphone 13")
customer = Customer.objects.filter(last_name__contains = "khoma")
product_start = Product.objects.filter(name__startswith = "per")
product_start = Product.objects.filter(name__endswith = "ter")



gt_1 = Product.objects.filter(price__gt = 100)
gte_1 = Product.objects.filter(price_gte = 100)
lt_1 = Product.objects.filter(price_lt = 100)
lte_1 = Product.objects.filter(price_lte = 100)
rng = Product.objects.filter(price_range = (10, 50))


in_1 = Product.objects.filter(id__in = [1,2,3])
is_null_1 = Product.objects.filter(email_isnull = True)
# Create your views here.
