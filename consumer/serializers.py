from rest_framework import serializers
from .models import Place, Category, Purchase, CategoryAnalytics, OverallAnalytics, PurchaseAnalytics, \
    PurchaseInCategory


class PlaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Place
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PurchaseInCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseInCategory
        fields = '__all__'


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'


class CategoryAnalyticsSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = CategoryAnalytics
        fields = '__all__'


class PurchaseAnalyticsSerializer(serializers.ModelSerializer):
    place = PlaceSerializer(read_only=True)
    category_analytics = CategoryAnalyticsSerializer(many=True, read_only=True)

    class Meta:
        model = PurchaseAnalytics
        fields = '__all__'


class OverallAnalyticsSerializer(serializers.ModelSerializer):
    purchase_analytics = PurchaseAnalyticsSerializer(many=True, read_only=True)

    class Meta:
        model = OverallAnalytics
        fields = '__all__'
