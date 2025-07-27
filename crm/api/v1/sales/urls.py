from django.urls import path, include
from rest_framework.routers import DefaultRouter

from crm.api.v1.sales.views import OpportunityViewSet

router = DefaultRouter()
router.register(r'', OpportunityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]