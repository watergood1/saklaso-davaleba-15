from django.db import models


class Product(models.Model):
    name = models.CharField()
    price = models.FloatField()
    quantity = models.IntegerField()




class Customer(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    age = models.IntegerField()
    email = models.EmailField()



class Order(models.Model):
    product = models.CharField()
    customer = models.CharField()
    amount = models.IntegerField()
# Create your models here.
