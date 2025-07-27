from rest_framework.pagination import PageNumberPagination

class TicketPagination(PageNumberPagination):
    page_size = 20

class CustomerPagination(PageNumberPagination):
    page_size = 20
