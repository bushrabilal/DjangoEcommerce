from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, Blank=True)
    name = models.CharField(max_length=100,null=True)
    email = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    price = models.FloatField()
    digital = models.BooleansField(default=False,null=True, Blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete= models.SET_NULL,null=True, Blank=True)
    ordered_date = models.DateTimeField(auto_now_add=True)
    complete = models.BooleansField(default=False)
    transaction_id =models.CharField(max_length=100, null=True)