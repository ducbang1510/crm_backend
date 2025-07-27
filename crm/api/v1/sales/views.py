from django.db.migrations.serializer import OperationSerializer
from django.shortcuts import render
from django.http import HttpResponse
from oauth2_provider.contrib.rest_framework import TokenHasScope
from rest_framework import viewsets
from rest_framework import viewsets, permissions, status, generics

from crm.models import Opportunity


class OpportunityViewSet(viewsets.ViewSet, generics.ListAPIView, generics.CreateAPIView):
    queryset = Opportunity.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OperationSerializer