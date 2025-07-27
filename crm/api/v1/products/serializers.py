from rest_framework.serializers import ModelSerializer

from crm.models import Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'is_active', 'created_at']