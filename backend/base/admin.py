from django.contrib import admin
from .models import Product, ProductVariant, ProductImage, ProductDetails


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'sku', 'description')
    list_filter = ('title', 'description')
    search_fields = ['title', 'description']


class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ('variant_color', 'variant_size')
    list_filter = ('variant_color', 'variant_size')
    search_fields = ['variant_color', 'variant_size']


class ProductImageAdmin(admin.ModelAdmin):
    pass


class ProductDetailsAdmin(admin.ModelAdmin):
    pass


# Register your models here.
admin.site.site_header = 'Coding Test - Mediusware Ltd.'
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductVariant, ProductVariantAdmin)
admin.site.register(ProductDetails, ProductDetailsAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
