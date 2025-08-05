from rest_framework import viewsets, permissions, status, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView
from crm.models.customer import Customer, ContactPerson
from crm.utils.pagination import CustomerPagination
from .serializers import CustomerSerializer, ContactPersonSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    pagination_class = CustomerPagination
    serializer_class = CustomerSerializer

    @action(methods=['get'], detail=True, url_path="contacts")
    def get_contacts(self, request, pk):
        customer = self.get_object()

        return Response(
            ContactPersonSerializer(customer.contacts.order_by("-id").all(), many=True, context={"request": self.request}).data,
            status=status.HTTP_200_OK)

    @action(methods=['post'], detail=True, url_path="add-contact")
    def get_contacts(self, request, pk):
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email = request.data.get('email')
        phone = request.data.get('phone')
        gender = request.data.get('gender')
        position = request.data.get('position')
        date_of_birth = request.data.get('date_of_birth')
        is_primary= request.data.get('is_primary')

        if gender is None:
            gender = ContactPerson.OTHER

        if is_primary is None:
            is_primary = False

        if first_name and last_name and email and phone and position:
            contact = ContactPerson.objects.create(first_name=first_name, last_name=last_name, email=email, phone=phone,
                                                   gender=gender, date_of_birth=date_of_birth, is_primary=is_primary,
                                                   customer=self.get_object())
            return Response(ContactPersonSerializer(contact).data,
                            status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)


    def get_queryset(self):
        customers = Customer.objects.all()

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
            customers = customers.order_by('name')

        keyword = self.request.query_params.get('keyword')
        if keyword is not None:
            customers = customers.filter(name__icontains=keyword)

        is_active = self.request.query_params.get('is_active')
        if is_active is not None:
            customers = customers.filter(is_active=is_active)

        return customers

class ContactPersonViewSet(viewsets.ViewSet, generics.RetrieveUpdateAPIView):
    queryset = ContactPerson.objects.all()
    serializer_class = ContactPersonSerializer

    def get_queryset(self):
        contacts = ContactPerson.objects.all()

        customer_id = self.request.query_params.get('customer_id')
        if customer_id is not None:
            contacts = contacts.filter(customer_id=customer_id)

        return contacts