from django.db import models


class ProductVariant(models.Model):
    colors = (
        ('Red', 'Red'),
        ('Blue', 'Blue'),
        ('Green', 'Green'),
        ('White', 'White'),
        ('Black', 'Black'),
        ('Orange', 'Orange'),

    )
    variant_color = models.CharField(max_length=100, choices=colors)
    sizes = (
        ('s', 's'),
        ('m', 'm'),
        ('l', 'l'),
        ('xl', 'xl'),
        ('xxl', 'xxl'),
        ('xxxl', 'xxxl'),

    )
    variant_size = models.CharField(
        max_length=100, choices=sizes)

    def __str__(self):
        return self.variant_color, self.variant_size


class Product(models.Model):
    title = models.CharField(max_length=255)
    sku = models.SlugField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ProductDetails(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_variant_size = models.ForeignKey(ProductVariant, on_delete=models.CASCADE,
                                             related_name='product_variant_size')
    product_variant_color = models.ForeignKey(ProductVariant, on_delete=models.CASCADE,
                                              related_name='product_variant_color')
    price = models.FloatField()
    stock = models.FloatField()


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    file_path = models.URLField()

    def __str__(self):
        return self.file_path
