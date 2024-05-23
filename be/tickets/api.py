from django.http import JsonResponse
from rest_framework import status

def tickets(request):
    return JsonResponse({"message": "Tickets"}, status=status.HTTP_200_OK)

