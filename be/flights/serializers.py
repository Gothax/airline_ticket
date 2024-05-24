from rest_framework import serializers
from .models import Flight, Airport


class FlightSerializer(serializers.ModelSerializer):
    departure = serializers.StringRelatedField(source='departure_country', read_only=True)
    departure_airport = serializers.StringRelatedField(source='departure_airport.name', read_only=True)
    departure_airport_code = serializers.StringRelatedField(source='departure_airport.city_code', read_only=True)
    destination = serializers.StringRelatedField(source='destination_country.name', read_only=True)
    destination_airport = serializers.StringRelatedField(source='destination_airport.name', read_only=True)
    destination_airport_code = serializers.StringRelatedField(source='destination_airport.city_code', read_only=True)
    
    departure_date = serializers.SerializerMethodField()
    destination_date = serializers.SerializerMethodField()
    departure_time = serializers.SerializerMethodField()
    destination_time = serializers.SerializerMethodField()
    
    duration_time = serializers.FloatField(source='duration', read_only=True)
    airline = serializers.StringRelatedField(source='airline.name', read_only=True)
    flightClass = serializers.StringRelatedField(source='flight_class.name', read_only=True)
    
    class Meta:
        model = Flight
        fields = ('id', 'departure', 'departure_airport', 'departure_airport_code',
                  'destination', 'destination_airport', 'destination_airport_code',
                  'departure_date', 'destination_date', 
                  'departure_time', 'destination_time',
                  'duration_time', 'airline', 'flightClass', 'price')


    def get_departure_date(self, obj):
        return obj.departure_datetime.date()

    def get_destination_date(self, obj):
        return obj.destination_datetime.date()

    def get_departure_time(self, obj):
        return obj.departure_datetime.time()

    def get_destination_time(self, obj):
        return obj.destination_datetime.time()