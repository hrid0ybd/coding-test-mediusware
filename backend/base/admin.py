from django.contrib import admin
from .models import Product, ProductImage, ProductVariant, ProductVariantPrice, Variant


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
admin.site.site_header = 'Demo CRUD Project'
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(ProductVariant, ProductVariantPriceAdmin)
admin.site.register(ProductVariantPrice, ProductVariantAdmin)
admin.site.register(Variant, VariantAdmin)
