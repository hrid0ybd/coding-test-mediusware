from django.db.models import fields
from rest_framework import serializers
from base.models import Product, ProductImage, ProductVariant, ProductVariantPrice, Variant


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


class ProductVariantSerializer(serializers.ModelSerializer):

    product_title = serializers.CharField(
        source='product.title', read_only=True)
    product_description = serializers.CharField(
        source='product.description', read_only=True)
    variant_size = serializers.CharField(
        source='variant.title', read_only=True)

    class Meta:
        model = ProductVariant
        fields = ('id', 'variant_title', 'price',
                  'stock', 'product_id', 'variant_id', 'product_title', 'product_description', 'variant_size')


class ProductVariantPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariantPrice
        fields = ('id', 'product_variant_one_id',
                  'product_variant_three_id', 'product_variant_two_id')
