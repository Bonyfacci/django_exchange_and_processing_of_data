from rest_framework import serializers
from .models import Product, PurchaseCheck


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class PurchaseCheckSerializer(serializers.ModelSerializer):
    items = ProductSerializer(many=True)

    class Meta:
        model = PurchaseCheck
        fields = '__all__'

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        purchase_check = PurchaseCheck.objects.create(**validated_data)

        for item_data in items_data:
            product = Product.objects.create(**item_data)
            purchase_check.items.add(product)

        return purchase_check
