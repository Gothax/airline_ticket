from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .models import Flight
from .serializers import FlightSerializer

class FlightPagination(PageNumberPagination):
    page_size = 6

@api_view(['GET'])
@permission_classes([AllowAny])
def flights(request):
    queryset = Flight.objects.all().order_by('id')
    paginator = FlightPagination()
    paginated_queryset = paginator.paginate_queryset(queryset, request)
    serializer = FlightSerializer(paginated_queryset, many=True)
    
    response_data = {
        "totalItems": paginator.page.paginator.count,
        "totalPages": paginator.page.paginator.num_pages,
        "currentPage": paginator.page.number,
        "flights": serializer.data,
    }
    
    return paginator.get_paginated_response(response_data)


