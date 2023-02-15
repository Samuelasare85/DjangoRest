from ..models import User
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView
from ..helpers.validations import validate_input
from ..helpers.notifications import email_notification
from rest_framework import status
from django.contrib.auth.hashers import make_password

class RegisterView(APIView):
    
    def post(self, request):
        name = request.data['name'].title()
        email = request.data['email'].strip().lower()
        password = request.data['password']
        phone_number = request.data['phone_number']
        
        input = {
            'name': name.title(),
            'email': email,
            'password': password,
            'phone_number': phone_number
        }
        
        validate_input(input)
        
        try:
            if User.objects.filter(email=email).exists():
                return Response({'status:': 'error', 'data': {'message': 'User already exists'}}, status=status.HTTP_400_BAD_REQUEST)
            elif User.objects.filter(name=name).exists():
                 return Response({'status:': 'error', 'data': {'message': 'Name already exists'}}, status=status.HTTP_400_BAD_REQUEST)
            elif User.objects.filter(phone_number=phone_number).exists():
                return Response({'status:': 'error', 'data': {'message': 'User phone number already exists'}}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            raise AuthenticationFailed(str(error))
        
        data = {
            'name': name,
            'email': email,
            'password': make_password(password),
            'phone_number': phone_number
        }
        
        user = User.objects.create(**data)
        
        try:
            new_data = {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'phone_number': user.phone_number
            }
            
            email_notification(email)
            new_data.update({'message':'Check your email and verify your account'})
        except Exception as error:
            raise AuthenticationFailed(str(error))
        
        return Response({
            "status":"success",
            "data": new_data},
            status=status.HTTP_201_CREATED
            )
    
        
        