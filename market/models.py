from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    full_name = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    position = models.CharField(max_length=50)
    age = models.IntegerField(verbose_name='ageism is bad')

    def __str__(self):
        return self.full_name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'name - {self.name}, price - {self.price}'


class Cart(models.Model):
    products = models.ManyToManyField(Product)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    overall_sum = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.products_in_cart = None

    def __str__(self):
        return f'client - {self.client.username}, cost - {self.overall_sum}'

    def calc_sum(self):
        over_sum = 0
        for product in self.products.all():
            over_sum += product.price

        self.overall_sum = over_sum
