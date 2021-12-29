from base.viewsets import ProductVariantViewSet, ProductViewSet, ProductImageViewSet, ProductDetailsViewSet
from rest_framework import routers

router = routers.DefaultRouter()


router.register('product', ProductViewSet)
router.register('product-variant', ProductVariantViewSet)
router.register('product-details', ProductDetailsViewSet)
router.register('product-image', ProductImageViewSet)
