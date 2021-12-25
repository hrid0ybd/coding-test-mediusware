from django.contrib import admin
from .models import Persons, Product, ProductImage, ProductVariant, ProductVariantPrice, Variant


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'village', 'district', 'division')
    list_filter = ('date_created', 'division')
    search_fields = ['dna_sample_id', 'nid_bid']


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'sku', 'description')
    list_filter = ('title', 'description')
    search_fields = ['title', 'description']


class ProductImageAdmin(admin.ModelAdmin):
    pass


class ProductVariantPriceAdmin(admin.ModelAdmin):
    pass


class ProductVariantAdmin(admin.ModelAdmin):
    pass


class VariantAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'description')
    list_filter = ('title', 'description')
    search_fields = ['title', 'description']


# Register your models here.
admin.site.site_header = 'Coding Test - Mediusware Ltd.'
admin.site.register(Persons, PersonAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(ProductVariant, ProductVariantPriceAdmin)
admin.site.register(ProductVariantPrice, ProductVariantAdmin)
admin.site.register(Variant, VariantAdmin)
