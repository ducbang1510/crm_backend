from rest_framework.serializers import ModelSerializer
from crm.models.customer import ContactPerson, Customer


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'email', 'phone', 'company', 'address', 'is_active', 'created_at', 'updated_at']

class ContactPersonSerializer(ModelSerializer):
    class Meta:
        model = ContactPerson
        fields = ['id', 'first_name', 'last_name', 'email', 'phone',
                  'gender', 'position', 'date_of_birth', 'is_primary', 'customer']