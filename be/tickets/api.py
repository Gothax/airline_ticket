from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Ticket
from flights.serializers import FlightSerializer
from flights.models import Flight
from rest_framework.pagination import PageNumberPagination
from .serializers import TicketSerializer

class TicketPagination(PageNumberPagination):
    page_size = 10

    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def tickets(request):
    user = request.user
    tickets = Ticket.objects.filter(user=user).order_by('id')  # Order the queryset by 'id'
    
    paginator = TicketPagination()
    paginated_tickets = paginator.paginate_queryset(tickets, request)
    serializer = TicketSerializer(paginated_tickets, many=True)
    
    response_data = {
        "totalItems": paginator.page.paginator.count,
        "totalPages": paginator.page.paginator.num_pages,
        "currentPage": paginator.page.number,
        "tickets": serializer.data,
    }
    return JsonResponse(response_data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def purchase_ticket(request, flight_id):
    flt_id = request.data['flightId']
    Ticket.objects.create(flight_id=flt_id, user_id=request.user.id)
    flight = Flight.objects.get(pk=flt_id)
    serializer = FlightSerializer(flight)
    
    return JsonResponse({
        "message": "구매 완료",
        "ticket": serializer.data                             
    }, status=status.HTTP_200_OK)
    
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def refund_ticket(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    ticket.delete()
    return JsonResponse({
        "message": "티켓이 환불되었습니다."
    }, status=status.HTTP_200_OK)


