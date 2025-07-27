from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet
from oauth2_provider.models import Application

router = DefaultRouter()
router.register(r'', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]