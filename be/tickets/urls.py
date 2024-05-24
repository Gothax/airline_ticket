from django.urls import path
from . import api

urlpatterns = [
    path('tickets/', api.tickets, name='tickets'),
    path('purchase/<int:flight_id>/', api.purchase_ticket, name='purchase_ticket'),
    path('tickets/<int:ticket_id>/refund/', api.refund_ticket, name='refund_ticket'),
]

