from rest_framework import viewsets, permissions, status, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView
from django.db.models import Q
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from crm.models import Opportunity, Contract
from crm.models.customer import Customer, ContactPerson
from crm.utils.pagination import CustomerPagination
from .serializers import CustomerSerializer, ContactPersonSerializer
from ..sales.serializers import OpportunitySerializer, ContractSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomerPagination
    serializer_class = CustomerSerializer

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('name', openapi.IN_QUERY,
                description="Filter contacts by name (searches first_name and last_name)", type=openapi.TYPE_STRING
            ),
            openapi.Parameter('email', openapi.IN_QUERY,
                description="Filter contacts by email", type=openapi.TYPE_STRING
            ),
            openapi.Parameter('is_primary', openapi.IN_QUERY,
                description="Filter by primary status (true/false)", type=openapi.TYPE_BOOLEAN
            ),
            openapi.Parameter('position', openapi.IN_QUERY,
                description="Filter by position", type=openapi.TYPE_STRING
            ),
        ],
        responses={status.HTTP_200_OK: ContactPersonSerializer(many=True)}
    )
    @action(methods=['get'], detail=True, url_path="contacts")
    def get_contacts(self, request, pk):
        customer = self.get_object()
        contacts = customer.contacts.all().order_by("-id")

        # Add filtering
        name = request.query_params.get('name')
        email = request.query_params.get('email')
        is_primary = request.query_params.get('is_primary')
        position = request.query_params.get('position')

        if name:
            contacts = contacts.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if email:
            contacts = contacts.filter(email__icontains=email)
        if is_primary:
            contacts = contacts.filter(is_primary=is_primary.lower() == 'true')
        if position:
            contacts = contacts.filter(position__icontains=position)

        serializer = ContactPersonSerializer(contacts, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=True, url_path="create-contact")
    def create_contact(self, request, pk):
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email = request.data.get('email')
        phone = request.data.get('phone')
        gender = request.data.get('gender')
        position = request.data.get('position')
        date_of_birth = request.data.get('date_of_birth')
        is_primary = request.data.get('is_primary')

        gender = gender if gender is not None else ContactPerson.OTHER
        is_primary = is_primary.lower() == 'true' if is_primary is not None else False

        if first_name and last_name and email and phone and position:
            contact = ContactPerson.objects.create(first_name=first_name, last_name=last_name, email=email, phone=phone,
                                                   gender=gender, date_of_birth=date_of_birth, is_primary=is_primary,
                                                   customer=self.get_object())
            return Response(ContactPersonSerializer(contact).data,
                            status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['post'], detail=True, url_path="create-opportunity")
    def create_opportunity(self, request, pk):
        name = request.data.get('name')
        description = request.data.get('description')
        amount = request.data.get('amount')
        stage = request.data.get('stage')
        probability = request.data.get('probability')
        expected_close_date = request.data.get('expected_close_date')

        stage = stage if stage is not None else Opportunity.PROSPECT
        probability = probability if probability is not None else 0

        if name and amount and expected_close_date:
            opportunity = Opportunity.objects.create(name=name, description=description, amount=amount, stage=stage,
                                                     probability=probability, customer=self.get_object(),
                                                     created_by=request.user)
            return Response(OpportunitySerializer(opportunity).data,
                            status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['post'], detail=True, url_path="create-contract")
    def create_contract(self, request, pk):
        name = request.data.get('name')
        start_date = request.data.get('start_date')
        end_date = request.data.get('end_date')
        value = request.data.get('value')
        renewal_reminder_date = request.data.get('renewal_reminder_date')
        document = request.data.get('document')
        notes = request.data.get('notes')

        if name and start_date and end_date and value:
            contract = Contract.objects.create(name=name, start_date=start_date, end_date=end_date, value=value,
                                               renewal_reminder_date=renewal_reminder_date, document=document,
                                               notes=notes, customer=self.get_object())
            return Response(ContractSerializer(contract).data,
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
