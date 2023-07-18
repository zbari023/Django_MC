from django.contrib import admin

# Register your models here.
from .models import Product , Menu


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','menu']


admin.site.register(Product,ProductAdmin)
admin.site.register(Menu)
