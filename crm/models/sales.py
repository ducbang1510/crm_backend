from django.db import models

from crm.models.customer import Customer
from crm.models.user import User


class Opportunity(models.Model):
    """
    Tracks potential sales deals through pipeline stages.
    """
    PROSPECT, QUALIFICATION, PROPOSAL, NEGOTIATION, WON, LOST = range(6)
    STAGE_CHOICES = [
        (PROSPECT, 'Prospect'),
        (QUALIFICATION, 'Qualification'),
        (PROPOSAL, 'Proposal'),
        (NEGOTIATION, 'Negotiation'),
        (WON, 'Won'),
        (LOST, 'Lost'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='opportunities')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    stage = models.PositiveSmallIntegerField(choices=STAGE_CHOICES, default=PROSPECT)
    probability = models.IntegerField(default=0)  # 0-100%
    expected_close_date = models.DateField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'opportunity'
        verbose_name = 'Opportunity'
        verbose_name_plural = 'Opportunities'

    def __str__(self):
        return self.name


class Activity(models.Model):
    """
    Logs all customer interactions and follow-ups.
    """
    CALL, EMAIL, MEETING, TASK = range(4)
    TYPE_CHOICES = [
        (CALL, 'Phone Call'),
        (EMAIL, 'Email'),
        (MEETING, 'Meeting'),
        (TASK, 'Task'),
    ]

    opportunity = models.ForeignKey(Opportunity, on_delete=models.CASCADE, related_name='activities', null=True,
                                    blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='activities')
    type = models.PositiveSmallIntegerField(choices=TYPE_CHOICES)
    subject = models.CharField(max_length=200)
    notes = models.TextField(blank=True)
    due_date = models.DateTimeField()
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'activity'
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'

    def __str__(self):
        return self.subject

class Contract(models.Model):
    """
    Records customer contracts and agreements.
    """
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='contracts')
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    value = models.DecimalField(max_digits=10, decimal_places=2)
    renewal_reminder_date = models.DateField(null=True, blank=True)
    document = models.FileField(upload_to='contracts/', null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'contract'
        verbose_name = 'Contract'
        verbose_name_plural = 'Contracts'

    def __str__(self):
        return "Contract ID %s - Created date: %s" % (str(self.id), self.created_at.strftime("%Y-%m-%d"))