from django.contrib import admin

from producer.models import Product, PurchaseCheck


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ...


@admin.register(PurchaseCheck)
class PurchaseCheckAdmin(admin.ModelAdmin):
    ...
