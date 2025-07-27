from django.db import models

class Customer(models.Model):
    """
    Stores all customer/client information.
    """
    name = models.CharField(max_length=100)     # name of individual customer or legal business
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    company = models.CharField(max_length=100, blank=True)
    address = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'customer'
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class ContactPerson(models.Model):
    """
    Stores individual contacts within customer organizations.
    """
    MALE, FEMALE, OTHER = range(3)
    GENDER_CHOICE = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(null=False)
    phone = models.CharField(max_length=20, null=False)
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICE, default=OTHER)
    position = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    is_primary = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='contacts')

    class Meta:
        db_table = 'contact_person'
        verbose_name_plural = 'Contact People'

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)




