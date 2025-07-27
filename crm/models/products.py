from django.db import models

from crm.models.customer import Customer


class Product(models.Model):
    """
    Catalog of products/services offered.
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.name

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

    def __str__(self):
        return "Contract ID %s - Created date: %s" % (str(self.id), self.created_at.strftime("%Y-%m-%d"))