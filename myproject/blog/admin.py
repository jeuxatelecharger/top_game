from django.contrib import admin
from .models import Categorys, Products
# Register your models here.
class AdminCategorie(admin.ModelAdmin):
    list_display = ('name','date_added')


class AdminProduct(admin.ModelAdmin):
    list_display =('title' , 'price' , 'category' , 'date_added')

admin.site.register(Products , AdminProduct)
admin.site.register(Categorys ,AdminCategorie)