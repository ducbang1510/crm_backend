from rest_framework.serializers import ModelSerializer

from crm.models import SupportTicket


class SupportTicketSerializer(ModelSerializer):
    class Meta:
        model = SupportTicket
        fields = ['id', 'subject', 'description', 'status', 'assigned_to', 'priority', 'resolved_at']