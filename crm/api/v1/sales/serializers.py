from rest_framework.serializers import ModelSerializer

from crm.models import Opportunity


class OpportunitySerializer(ModelSerializer):
    class Meta:
        model = Opportunity
        fields = ['id', 'name', 'description', 'amount', 'stage', 'probability', 'expected_close_date']