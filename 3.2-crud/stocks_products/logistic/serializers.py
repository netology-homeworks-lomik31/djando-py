from rest_framework import serializers
from .models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['id', 'stock', 'product', 'quantity', 'price']
        extra_kwargs = {'stock': {'required': False}}


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['id', 'address', 'products', 'positions']

    def create(self, validated_data):
        positions = validated_data.pop('positions')
        stock = super().create(validated_data)

        for i in positions:
            StockProduct(
                stock=stock,
                product=i['product'],
                quantity=i['quantity'],
                price=i['price']
            ).save()

        return stock

    def update(self, instance, validated_data):
        positions = validated_data.pop('positions')
        stock = super().update(instance, validated_data)

        for i in positions:
            product = StockProduct.objects.update_or_create(stock=stock, product_id=i['product'], defaults={'price': 0, 'quantity': 1})
            for j, k in i.items():
                setattr(product, j, k)
            product.save()

        return stock
