from rest_framework import serializers
from .models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='pk')
    departure_airport = serializers.StringRelatedField(source='flight.departure_airport.name', read_only=True)
    departure_airport_code = serializers.StringRelatedField(source='flight.departure_airport.city_code', read_only=True)
    destination_airport = serializers.StringRelatedField(source='flight.destination_airport.name', read_only=True)
    destination_airport_code = serializers.StringRelatedField(source='flight.destination_airport.city_code', read_only=True)
    departure_date = serializers.SerializerMethodField()
    destination_date = serializers.SerializerMethodField()
    departure_time = serializers.SerializerMethodField()
    destination_time = serializers.SerializerMethodField()
    duration_time = serializers.FloatField(source='flight.duration', read_only=True)
    airline = serializers.StringRelatedField(source='flight.airline.name', read_only=True)
    flightClass = serializers.StringRelatedField(source='flight.flight_class.name', read_only=True)
    price = serializers.IntegerField(source='flight.price', read_only=True)

    class Meta:
        model = Ticket
        fields = ('id', 'departure_airport', 'departure_airport_code', 'destination_airport', 'destination_airport_code',
                  'departure_date', 'destination_date', 'departure_time', 'destination_time',
                  'duration_time', 'airline', 'flightClass', 'price')

    def get_departure_date(self, obj):
        return obj.flight.departure_datetime.date()

    def get_destination_date(self, obj):
        return obj.flight.destination_datetime.date()

    def get_departure_time(self, obj):
        return obj.flight.departure_datetime.time()

    def get_destination_time(self, obj):
        return obj.flight.destination_datetime.time()