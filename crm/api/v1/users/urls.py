from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ApplicationViewSet
from oauth2_provider.urls import base_urlpatterns

router = DefaultRouter()
router.register(r'', UserViewSet)
router.register(r'applications', ApplicationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]