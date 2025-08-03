from django import forms
from django.contrib import admin
from django.contrib.auth.models import Permission
from django.urls import path
from django.template.response import TemplateResponse

from .models.customer import Customer, ContactPerson
from .models.products import Product
from .models.sales import Opportunity, Activity, Contract
from .models.support import SupportTicket
from .models.user import User

MANAGE_USER_GROUP = "Manage Users"
MANAGE_CUSTOMER_GROUP = "Manage Customers"
MANAGE_PRODUCT_GROUP = "Manage Products"
MANAGE_SALE_GROUP = "Sale Management"
MANAGE_SUPPORT_GROUP = "Manage Support Ticket"


class UserAdmin(admin.ModelAdmin):
    menu_title = 'Users'
    menu_group = MANAGE_USER_GROUP
    list_per_page = 10
    list_display = ["id", "first_name", "last_name", "username", "email", "date_joined"]
    search_fields = ['first_name', 'last_name', 'username', 'email']
    list_filter = ['date_joined']


class PermissionAdmin(admin.ModelAdmin):
    menu_group = MANAGE_USER_GROUP


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class CustomerAdmin(admin.ModelAdmin):
    menu_title = 'Customers'
    menu_group = MANAGE_CUSTOMER_GROUP
    list_display = ['name', 'email', 'phone', 'company', 'address', 'is_active']
    form = CustomerForm
    search_fields = ['name', 'email', 'address', 'company']
    list_per_page = 10


class ContactPersonForm(forms.ModelForm):
    class Meta:
        model = ContactPerson
        fields = '__all__'


class ContactPersonAdmin(admin.ModelAdmin):
    menu_title = 'Contacts'
    menu_group = MANAGE_CUSTOMER_GROUP
    list_display = ['first_name', 'last_name', 'email', 'phone', 'gender', 'position', 'date_of_birth', 'is_primary',
                    'customer']
    form = ContactPersonForm
    search_fields = ['first_name', 'last_name', 'email', 'customer']
    list_per_page = 10


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class ProductAdmin(admin.ModelAdmin):
    menu_title = 'Products'
    menu_group = MANAGE_PRODUCT_GROUP
    list_display = ['name', 'description', 'price', 'is_active', 'created_at']
    form = ProductForm
    search_fields = ['name', 'description']
    list_per_page = 10


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = '__all__'


class ContractAdmin(admin.ModelAdmin):
    menu_title = 'Contracts'
    menu_group = MANAGE_SALE_GROUP
    list_display = ['name', 'start_date', 'end_date', 'value', 'renewal_reminder_date',
                    'document', 'notes', 'created_at']
    form = ContractForm
    search_fields = ['name']
    list_per_page = 10


class OpportunityForm(forms.ModelForm):
    class Meta:
        model = Opportunity
        fields = '__all__'


class OpportunityAdmin(admin.ModelAdmin):
    menu_title = 'Opportunities'
    menu_group = MANAGE_SALE_GROUP
    list_display = ['name', 'customer', 'description', 'amount', 'stage', 'probability',
                    'expected_close_date', 'created_by', 'created_at', 'updated_at']
    form = OpportunityForm
    search_fields = ['name', 'created_by']
    list_per_page = 10


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = '__all__'


class ActivityAdmin(admin.ModelAdmin):
    menu_title = 'Activities'
    menu_group = MANAGE_SALE_GROUP
    list_display = ['subject', 'customer', 'type', 'notes', 'due_date', 'completed', 'completed_at',
                    'assigned_to', 'created_at', 'updated_at']
    form = ActivityForm
    search_fields = ['subject', 'assigned_to', 'customer']
    list_per_page = 10


class SupportTicketForm(forms.ModelForm):
    class Meta:
        model = SupportTicket
        fields = '__all__'


class SupportTicketAdmin(admin.ModelAdmin):
    menu_title = 'Support Tickets'
    menu_group = MANAGE_SUPPORT_GROUP
    list_display = ['subject', 'description', 'status', 'priority', 'assigned_to',
                    'created_at', 'updated_at', 'resolved_at']
    form = SupportTicketForm
    search_fields = ['subject', 'assigned_to']
    list_per_page = 10


class CRMWebAdminSite(admin.AdminSite):
    site_header = 'CRM Administration'
    site_title = 'CRM Site Admin'


admin_site = CRMWebAdminSite(name='crm_admin')
admin_site.register(User, UserAdmin)
admin_site.register(Permission, PermissionAdmin)
admin_site.register(Customer, CustomerAdmin)
admin_site.register(ContactPerson, ContactPersonAdmin)
admin_site.register(Product, ProductAdmin)
admin_site.register(Contract, ContractAdmin)
admin_site.register(Opportunity, OpportunityAdmin)
admin_site.register(Activity, ActivityAdmin)
admin_site.register(SupportTicket, SupportTicketAdmin)
