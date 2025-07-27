from crm.models.customer import Customer, ContactPerson

def create_customer_with_contacts(customer_data, contacts_data):
    customer = Customer.objects.create(**customer_data)
    for contact_data in contacts_data:
        ContactPerson.objects.create(customer=customer, **contact_data)
    return customer