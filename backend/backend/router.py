from base.viewsets import ProductVariantPriceViewSet, ProductVariantViewSet, ProductViewSet, VariantViewSet, ProductImageViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register('product-variant-price', ProductVariantPriceViewSet)
router.register('product-variant', ProductVariantViewSet)
router.register('product', ProductViewSet)
router.register('variant', VariantViewSet)
router.register('product-image', ProductImageViewSet)
