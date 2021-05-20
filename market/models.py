from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    full_name = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    position = models.CharField(max_length=50)
    age = models.IntegerField(verbose_name='ageism is bad')


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Cart(models.Model):
    products = models.ManyToManyField(Product)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    overall_sum = models.DecimalField(max_digits=10, decimal_places=2)
