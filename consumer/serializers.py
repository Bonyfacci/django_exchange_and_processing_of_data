from rest_framework import serializers
from .models import Place, Category, Purchase, CategoryAnalytics, OverallAnalytics


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'


class CategoryAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryAnalytics
        fields = '__all__'


class OverallAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OverallAnalytics
        fields = '__all__'


class PlaceSerializer(serializers.ModelSerializer):
    purchases = PurchaseSerializer(many=True, read_only=True)
    overall_analytics = OverallAnalyticsSerializer(read_only=True)

    class Meta:
        model = Place
        fields = '__all__'
