from django.db.migrations.serializer import OperationSerializer
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from oauth2_provider.contrib.rest_framework import TokenHasScope
from rest_framework import viewsets
from rest_framework import viewsets, permissions, status, generics

from crm.api.v1.sales.serializers import ActivitySerializer, ContractSerializer
from crm.models.sales import Opportunity, Activity, Contract


class OpportunityViewSet(viewsets.ViewSet, generics.ListAPIView, generics.CreateAPIView):
    queryset = Opportunity.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OperationSerializer

class ActivityViewSet(viewsets.ViewSet, generics.ListAPIView, generics.CreateAPIView):
    queryset = Activity.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ActivitySerializer

class ContractViewSet(viewsets.ViewSet, generics.ListAPIView, generics.CreateAPIView):
    queryset = Contract.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ContractSerializer

class ActivityBaseOnOpportunityViewSet(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Activity.objects.filter(
            opportunity_id=self.kwargs['opportunity_pk']
        )

class ActivityBaseOnCustomerViewSet(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Activity.objects.filter(
            customer_id=self.kwargs['customer_pk']
        )