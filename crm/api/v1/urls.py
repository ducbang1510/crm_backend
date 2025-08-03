from django.urls import path, include

urlpatterns = [
    path('users/', include('crm.api.v1.users.urls')),
    path('customers/', include('crm.api.v1.customers.urls')),
    path('sales/', include('crm.api.v1.sales.urls')),
    path('support/', include('crm.api.v1.support.urls')),
    path('products/', include('crm.api.v1.products.urls')),
]