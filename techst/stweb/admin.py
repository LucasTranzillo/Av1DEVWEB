from django.contrib import admin
from .models import Product, Client, Service


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'amount')
class ClientAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'age')
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('serviceType', 'price', 'description')


admin.site.register(Product, ProductAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Service, ServiceAdmin)

