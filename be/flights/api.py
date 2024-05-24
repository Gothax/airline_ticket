from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.pagination import PageNumberPagination
from .models import Flight
from .serializers import FlightSerializer

class FlightPagination(PageNumberPagination):
    page_size = 6

@api_view(['GET'])
@permission_classes([AllowAny])
@authentication_classes([])  # Ensure no authentication is required

def flights(request):
    queryset = Flight.objects.all().order_by('id')
    
    departures = request.query_params.get('departures')
    arrivals = request.query_params.get('arrivals')
    departure_date = request.query_params.get('departure_date')
    arrival_date = request.query_params.get('arrival_date')
    flight_class = request.query_params.get('flightClass')
    airline = request.query_params.get('airline')

    if departures and arrivals:
        queryset = queryset.filter(departure__name=departures, destination__name=arrivals)
    if departure_date and arrival_date:
        queryset = queryset.filter(departure_datetime__date=departure_date, destination_datetime__date=arrival_date)
    if flight_class:
        queryset = queryset.filter(flight_class__name=flight_class)
    if airline:
        queryset = queryset.filter(airline__name=airline)

    paginator = FlightPagination()
    paginated_queryset = paginator.paginate_queryset(queryset, request)
    serializer = FlightSerializer(paginated_queryset, many=True)
    
    response_data = {
        "totalItems": paginator.page.paginator.count,
        "totalPages": paginator.page.paginator.num_pages,
        "currentPage": paginator.page.number,
        "flights": serializer.data,
    }
    return JsonResponse(response_data)


