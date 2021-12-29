from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    sku = models.SlugField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Variant(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    file_path = models.URLField()

    def __str__(self):
        return self.file_path


class ProductVariant(models.Model):
    colors = (
        ('Red', 'Red'),
        ('Blue', 'Blue'),
        ('Green', 'Green'),
        ('White', 'White'),
        ('Black', 'Black'),
        ('Orange', 'Orange'),

    )
    variant_title = models.CharField(max_length=100, choices=colors)
    variant = models.ForeignKey(
        Variant, on_delete=models.CASCADE, related_name='variants')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='products')
    price = models.FloatField()
    stock = models.FloatField()

    def __str__(self):
        return self.variant_title


class ProductVariantPrice(models.Model):
    product_variant_one = models.ForeignKey(ProductVariant, on_delete=models.CASCADE,
                                            related_name='product_variant_one')
    product_variant_two = models.ForeignKey(ProductVariant, on_delete=models.CASCADE,
                                            related_name='product_variant_two')
    product_variant_three = models.ForeignKey(ProductVariant, on_delete=models.CASCADE,
                                              related_name='product_variant_three')
