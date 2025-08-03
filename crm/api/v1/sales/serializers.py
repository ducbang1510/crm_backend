from rest_framework.serializers import ModelSerializer

from crm.models.sales import Opportunity, Activity, Contract


class OpportunitySerializer(ModelSerializer):
    class Meta:
        model = Opportunity
        fields = ['id', 'name', 'description', 'amount', 'stage', 'probability', 'expected_close_date']

class ActivitySerializer(ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'subject', 'notes', 'type', 'due_date', 'completed', 'completed_at', 'assigned_to', 'customer', 'opportunity']

class ContractSerializer(ModelSerializer):
    class Meta:
        model = Contract
        fields = ['id', 'name', 'start_date', 'end_date', 'value', 'renewal_reminder_date', 'document', 'notes', 'customer']