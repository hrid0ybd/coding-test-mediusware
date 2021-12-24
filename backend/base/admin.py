from django.contrib import admin
from .models import Persons, Product, ProductImage, ProductVariant, ProductVariantPrice, Variant


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'village', 'district', 'division')
    list_filter = ('date_created', 'division')
    search_fields = ['dna_sample_id', 'nid_bid']


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'sku', 'description')
    list_filter = ('created_at', 'updated_at')
    search_fields = ['title', 'description']


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'file_path')
    list_filter = ('created_at', 'updated_at')
    search_fields = ['product']


class ProductVariantPriceAdmin(admin.ModelAdmin):
    list_display = ('product_variant_one',
                    'product_variant_two', 'product_variant_three')
    list_filter = ('created_at', 'updated_at')
    search_fields = ['product']


class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ('id', 'product')
    list_filter = ('created_at', 'updated_at')
    search_fields = ['product', 'id', 'variant_title']


class VariantAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'description')
    list_filter = ('created_at', 'updated_at')
    search_fields = ['title', 'description']


# Register your models here.
admin.site.site_header = 'Coding Test - Mediusware Ltd.'
admin.site.register(Persons, PersonAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(ProductVariant, ProductVariantPriceAdmin)
admin.site.register(ProductVariantPrice, ProductVariantAdmin)
admin.site.register(Variant, VariantAdmin)
