from django.contrib import admin
from market.models import Cart, Product, Employee


class CartAdmin(admin.ModelAdmin):
    fields = ('products', 'client', 'overall_sum')


class ProductAdmin(admin.ModelAdmin):
    fields = ('name', 'price')


class EmployeeAdmin(admin.ModelAdmin):
    fields = ('full_name', 'salary', 'position', 'age')


admin.site.register(Cart, CartAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Employee, EmployeeAdmin)
