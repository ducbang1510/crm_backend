from django.contrib import admin
from django.urls import path, include
from .admin import admin_site
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('api/v1/', include('crm.api.v1.urls')),  # Version 1
    path('admin/', admin_site.urls),

    path('accounts/login/', auth_views.LoginView.as_view(template_name='admin/login.html'), name='login'),
    path('admin-password-reset/', auth_views.PasswordResetView.as_view(), name='admin_password_reset',),
    path('admin-password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done',),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm',),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete',),
]