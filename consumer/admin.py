from django.contrib import admin

from consumer.models import Place, Category, Purchase, CategoryAnalytics, OverallAnalytics


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    ...


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    ...


@admin.register(CategoryAnalytics)
class CategoryAnalyticsAdmin(admin.ModelAdmin):
    ...


@admin.register(OverallAnalytics)
class OverallAnalyticsAdmin(admin.ModelAdmin):
    ...
