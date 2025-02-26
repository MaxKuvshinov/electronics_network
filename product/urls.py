from django.urls import path, include
from rest_framework.routers import SimpleRouter
from product.apps import ProductConfig
from product.views import ProductViewSet

app_name = ProductConfig.name

router = SimpleRouter()
router.register(r"product", ProductViewSet, basename="product")

urlpatterns = [
    path("", include(router.urls)),
]