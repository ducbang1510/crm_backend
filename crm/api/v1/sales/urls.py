from django.urls import path, include
from rest_framework.routers import DefaultRouter

from crm.api.v1.sales.views import OpportunityViewSet, ActivityViewSet, ContractViewSet, \
    ActivityBaseOnOpportunityViewSet, ActivityBaseOnCustomerViewSet

router = DefaultRouter()
router.register(r'opportunities', OpportunityViewSet, 'opportunity')
router.register(r'activities', ActivityViewSet)
router.register(r'contracts', ContractViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('opportunities/<int:opportunity_pk>/activities/',
         ActivityBaseOnOpportunityViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('customers/<int:customer_pk>/activities/',
         ActivityBaseOnCustomerViewSet.as_view({'get': 'list', 'post': 'create'})),
]