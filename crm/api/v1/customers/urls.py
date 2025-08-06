from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, ContactPersonViewSet
from oauth2_provider.urls import base_urlpatterns

router = DefaultRouter()
router.register(r'', CustomerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]