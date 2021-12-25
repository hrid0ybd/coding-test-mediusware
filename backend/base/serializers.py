from django.db.models import fields
from rest_framework import serializers
from base.models import Persons, Persons, Product, ProductImage, ProductVariant, ProductVariantPrice, Variant


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persons
        fields = ('personId', 'name', 'image', 'division', 'district', 'upozila', 'village', 'address', 'date_of_birth', 'marital_status',
                  'nid_bid', 'dna_sample_id', 'date_created', 'is_late')


class ProductVariantPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariantPrice
        fields = ('id', 'product_id', 'product_variant_one_id',
                  'product_variant_three_id', 'product_variant_two_id')
