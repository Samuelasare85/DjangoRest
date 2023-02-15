from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenObtainPairView
)
from .views.register import RegisterView
from .views.verifyotp import VerifyOTPView
from .views.login import LoginView
urlpatterns = [
   path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   path('register/', RegisterView.as_view(), name='register'),
   path('verifyotp/', VerifyOTPView.as_view(), name='verifyotp'),
   path('login/', LoginView.as_view(), name='login'),
]
