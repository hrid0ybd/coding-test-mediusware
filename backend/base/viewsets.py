from rest_framework import viewsets
from . import models
from . import serializers


class ProductVariantPriceViewSet(viewsets.ModelViewSet):
    queryset = models.ProductVariantPrice.objects.all()
    serializer_class = serializers.ProductVariantPriceSerializer


class ProductVariantViewSet(viewsets.ModelViewSet):
    queryset = models.ProductVariant.objects.all()
    serializer_class = serializers.ProductVariantSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class VariantViewSet(viewsets.ModelViewSet):
    queryset = models.Variant.objects.all()
    serializer_class = serializers.VariantSerializer


class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = models.ProductImage.objects.all()
    serializer_class = serializers.ProductImageSerializer
