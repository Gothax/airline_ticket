from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from .serializers import SignupUserSerializer, UserSerializer
from django.http import JsonResponse
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import User

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    serializer = SignupUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({"message": "회원가입 성공"}, status=status.HTTP_201_CREATED)
    return JsonResponse({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(email=email, password=password)
    if user is None:
        return JsonResponse({"error": "이메일 또는 비밀번가 일치하지 않습니다."}, status=status.HTTP_401_UNAUTHORIZED)
    refresh = RefreshToken.for_user(user)
    return JsonResponse({
        "message" : "로그인 성공",
        "token" : str(refresh.access_token),
        "user" : UserSerializer(user, many=False).data
    }, status=status.HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def delete_user(request, pk):
    if User.objects.get(pk=pk) == request.user:
        user = request.user
        user.delete()
        return JsonResponse({"message": "User deleted successfully"}, status=status.HTTP_200_OK)
    return JsonResponse({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)


