from django.db import models

from crm.models.customer import Customer
from crm.models.user import User


class SupportTicket(models.Model):
    """
    Manages customer support requests.
    """
    OPEN, IN_PROGRESS, ON_HOLD, RESOLVED, CLOSED = range(5)
    STATUS_CHOICES = [
        (OPEN, 'Open'),
        (IN_PROGRESS, 'In Progress'),
        (ON_HOLD, 'On Hold'),
        (RESOLVED, 'Resolved'),
        (CLOSED, 'Closed'),
    ]

    LOW, MEDIUM, HIGH, CRITICAL = range(4)
    PRIORITY_CHOICES = [
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
        (CRITICAL, 'Critical'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='tickets')
    subject = models.CharField(max_length=200)
    description = models.TextField()
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=OPEN)
    priority = models.PositiveSmallIntegerField(choices=PRIORITY_CHOICES, default=MEDIUM)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.subject