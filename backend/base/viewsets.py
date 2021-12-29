from rest_framework import viewsets
from . import models
from . import serializers


class ProductVariantViewSet(viewsets.ModelViewSet):
    queryset = models.ProductVariant.objects.all()
    serializer_class = serializers.ProductVariantSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ProductDetailsViewSet(viewsets.ModelViewSet):
    queryset = models.ProductDetails.objects.all()
    serializer_class = serializers.ProductDetailsSerializer


class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = models.ProductImage.objects.all()
    serializer_class = serializers.ProductImageSerializer
