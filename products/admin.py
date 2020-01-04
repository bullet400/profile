from django.contrib import admin

# Register your models here.
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display =('title','summary','image','icon','pub_date')

admin.site.register(Product, ProductAdmin)
