from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Flight)
admin.site.register(Airport)
admin.site.register(Region)
admin.site.register(Country)
admin.site.register(Airline)
admin.site.register(FlightClass)

