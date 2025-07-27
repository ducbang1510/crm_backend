from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, ContactPersonViewSet

router = DefaultRouter()
router.register(r'', CustomerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('<int:customer_pk>/contacts/',
         ContactPersonViewSet.as_view({'get': 'list', 'post': 'create'})),
]