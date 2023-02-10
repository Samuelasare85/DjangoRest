from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework import status
import re


def validate_input(input):
    name = input.get('name')
    email = input.get('email')
    phone = input.get('phone')
    password = input.get('password')
    
    
    if not name:
        return Response({'status': 'error', 'data': {'message': 'Invalid name'}}, status=status.HTTP_400_BAD_REQUEST)
    elif len(name) < 8:
        return Response({'status': 'error','data': {'message':'Length of name must be greater than 8 characters'}}, status=status.HTTP_400_BAD_REQUEST)
    elif not email:
        return Response({'status': 'error', 'data':{'message':'Invalid email address'}}, status=status.HTTP_400_BAD_REQUEST)
    elif not phone:
        return Response({'status': 'error', 'data':{'message': 'Invalid name'}}, status=status.HTTP_400_BAD_REQUEST)
    elif not password:
        return Response({'status': 'error', 'data':{'message':'Invalid password'}},status=status.HTTP_400_BAD_REQUEST)
    elif len(password) < 8:
        return Response({'status': 'error', 'data':{'message':'Enter a strong password'}},status=status.HTTP_400_BAD_REQUEST)
    verify_email_address(email)
    
    
def verify_email_address(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    if not (re.fullmatch(regex, email.lower())):
        return Response({'status': 'error', 'data':{'message':'Invalid name'}}, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    