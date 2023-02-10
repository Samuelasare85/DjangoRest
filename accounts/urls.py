from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views.register import RegisterView
from .views.verifyotp import VerifyOTPView

urlpatterns = [
   path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   path('register/', RegisterView.as_view(), name='register'),
   path('verifyotp/', VerifyOTPView.as_view(), name='verifyotp')
]
