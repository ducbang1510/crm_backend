from rest_framework import viewsets
from crm.models.customer import Customer, ContactPerson
from crm.utils.pagination import CustomerPagination
from .serializers import CustomerSerializer, ContactPersonSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    pagination_class = CustomerPagination
    serializer_class = CustomerSerializer
    filterset_fields = ['is_active', 'company']
    search_fields = ['name', 'email']

class ContactPersonViewSet(viewsets.ModelViewSet):
    serializer_class = ContactPersonSerializer

    def get_queryset(self):
        return ContactPerson.objects.filter(
            customer_id=self.kwargs['customer_pk']
        )