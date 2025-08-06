from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, AuthInfo
from oauth2_provider.urls import base_urlpatterns

router = DefaultRouter()
router.register(r'', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('oauth2-info/', AuthInfo.as_view()),
]