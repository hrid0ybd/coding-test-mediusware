from django.db.models import fields
from rest_framework import serializers
from base.models import Product, ProductImage, ProductVariant, ProductVariantPrice, Variant


class ProductVariantPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariantPrice
        fields = ('id', 'product_variant_one_id',
                  'product_variant_three_id', 'product_variant_two_id')


class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = ('id', 'variant_title', 'price',
                  'stock', 'product_id', 'variant_id')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'sku', 'description', 'created_at')


class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = ('id', 'title', 'description', 'active')


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('id', 'file_path', 'product_id')
