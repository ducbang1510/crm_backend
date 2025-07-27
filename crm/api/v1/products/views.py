from django.shortcuts import render
from django.http import HttpResponse
from oauth2_provider.contrib.rest_framework import TokenHasScope
from rest_framework import viewsets
from rest_framework import viewsets, permissions, status, generics

from crm.api.v1.products.serializers import ProductSerializer
from crm.models import Product


class ProductViewSet(viewsets.ViewSet, generics.ListAPIView, generics.CreateAPIView):
    queryset = Product.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProductSerializer