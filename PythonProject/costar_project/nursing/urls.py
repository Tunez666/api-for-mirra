from django.urls import path
from .views import buy_ticket_view, ticket_pdf

urlpatterns = [
    path('buy/', buy_ticket_view, name='buy-ticket'),
    path('ticket/<int:ticket_id>/pdf/', ticket_pdf, name='ticket-pdf'),
]