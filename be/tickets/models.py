from django.db import models
from flights.models import Flight
from account.models import User

class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10, blank=True, null=True)
    booking_date = models.DateTimeField(auto_now_add=True)

