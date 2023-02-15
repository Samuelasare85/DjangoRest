from ..models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed

class VerifyOTPView(APIView):
    
    def post(self, request):
        email = request.data['email'].strip().lower()
        otp = request.data['otp']

        try:
            user = User.objects.get(email=email)
            if not user:
                return Response({'status:': 'error', 'data': {f'message': 'User with email {email} does not exist'}}, status=status.HTTP_400_BAD_REQUEST)
            elif user.otp == otp:
                user.is_verified = True
                user.save()
                return Response({'status': 'success', 'data': {'message': 'OTP verified and account is created'}}, status=status.HTTP_200_OK)
        except Exception as error:
           raise  AuthenticationFailed(str(error))