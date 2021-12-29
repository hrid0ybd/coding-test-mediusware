from django.db.models import fields
from rest_framework import serializers
from base.models import Product, ProductImage, ProductVariant, ProductDetails


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'title', 'sku', 'description', 'created_at')


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('id', 'file_path', 'product_id')


class ProductVariantSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductVariant
        fields = ('id',  'variant_color', 'variant_size')


class ProductDetailsSerializer(serializers.ModelSerializer):

    product_title = serializers.CharField(
        source='product.title', read_only=True)

    product_description = serializers.CharField(
        source='product.description', read_only=True)

    variant_color = serializers.CharField(
        source='product_variant_color.variant_color', read_only=True)

    variant_size = serializers.CharField(
        source='product_variant_size.variant_size', read_only=True)

    class Meta:
        model = ProductDetails
        fields = ('id', 'product_title', 'product_description',
                  'variant_color', 'variant_size', 'price', 'stock')
