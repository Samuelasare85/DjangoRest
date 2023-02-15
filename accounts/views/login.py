from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from accounts.models import User
from ..tokens.tokens import get_tokens_for_user
from rest_framework_simplejwt.tokens import RefreshToken


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data['email'].strip().lower()
        password = request.data['password']
        
        user = User.objects.get(email=email)
        print(user)
        token = RefreshToken.for_user(user)
        print(token)
        
        # user =  authenticate(email=email, password=password)
        # print(user)
        if not user:
            return Response({'status:': 'error', 'data': {'message': 'Invalid credentials'}}, status=status.HTTP_400_BAD_REQUEST)
        elif user.is_verified == False:
            return Response({'status': 'error', 'data': {'message': 'User is not verified'}}, status=status.HTTP_400_BAD_REQUEST)
        
        token = get_tokens_for_user(user)
        return Response({'status': 'success', 'data': {'token': token}}, status=status.HTTP_200_OK)
        
        