from django.urls import path, include
from rest_framework.routers import DefaultRouter

from crm.api.v1.support.views import SupportTicketViewSet

router = DefaultRouter()
router.register(r'', SupportTicketViewSet)

urlpatterns = [
    path('', include(router.urls)),
]