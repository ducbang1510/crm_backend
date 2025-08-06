from django.shortcuts import render
from django.http import HttpResponse
from oauth2_provider.contrib.rest_framework import TokenHasScope
from rest_framework import viewsets
from rest_framework import viewsets, permissions, status, generics

from crm.api.v1.support.serializers import SupportTicketSerializer
from crm.models import SupportTicket


class SupportTicketViewSet(viewsets.ViewSet, generics.ListAPIView, generics.CreateAPIView, generics.UpdateAPIView):
    queryset = SupportTicket.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SupportTicketSerializer