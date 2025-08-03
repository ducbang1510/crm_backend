from rest_framework import viewsets, permissions, status, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView
from crm.models.customer import Customer, ContactPerson
from crm.utils.pagination import CustomerPagination
from .serializers import CustomerSerializer, ContactPersonSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.filter(is_active=True)
    pagination_class = CustomerPagination
    serializer_class = CustomerSerializer

    @action(methods=['get'], detail=True, url_path="contacts")
    def get_contacts(self, request, pk):
        c = self.get_object()
        return Response(
            ContactPersonSerializer(c.contacts.order_by("-id").all(), many=True, context={"request": self.request}).data,
            status=status.HTTP_200_OK)

    def get_queryset(self):
        customers = Customer.objects.filter(is_active=True)

        sort_value = self.request.query_params.get('sort')
        if sort_value is not None:
            if sort_value == '1':
                customers = customers.order_by('name')
            elif sort_value == '2':
                customers = customers.order_by('email')
            elif sort_value == '3':
                customers = customers.order_by('company')
            elif sort_value == '4':
                customers = customers.order_by('created_at')
        else:
            pass

        keyword = self.request.query_params.get('keyword')
        if keyword is not None:
            customers = customers.filter(name__icontains=keyword)

        return customers

class ContactPersonViewSet(viewsets.ModelViewSet):
    serializer_class = ContactPersonSerializer

    def get_queryset(self):
        return ContactPerson.objects.filter(
            customer_id=self.kwargs['id']
        )