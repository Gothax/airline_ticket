from django.db import models

# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Airport(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city_code = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.name

class Airline(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class FlightClass(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Flight(models.Model):
    departure = models.ForeignKey(Country, related_name='departure_country', on_delete=models.CASCADE)
    departure_airport = models.ForeignKey(Airport, related_name='departure_airport', on_delete=models.CASCADE)
    destination = models.ForeignKey(Country, related_name='destination_country', on_delete=models.CASCADE)
    destination_airport = models.ForeignKey(Airport, related_name='destination_airport', on_delete=models.CASCADE)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    flight_class = models.ForeignKey(FlightClass, on_delete=models.CASCADE)
    
    # departure date + departure time <-> departure datetime
    departure_datetime = models.DateTimeField()
    destination_datetime = models.DateTimeField()
    
    # EX) 6.5 시간
    duration = models.FloatField(default=0, editable=False, blank=True)
    price = models.IntegerField()
    
    def save(self, *args, **kwargs):
        self.duration = (self.destination_datetime - self.departure_datetime).total_seconds() / 3600
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.airline.name} flight from {self.departure_airport.name} to {self.destination_airport.name}"
