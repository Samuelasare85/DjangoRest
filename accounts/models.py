from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import RegexValidator

phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")

class User(AbstractBaseUser):
    name =  models.CharField(max_length=255, verbose_name="Full name")
    email = models.EmailField(max_length=255, unique=True)
    otp = models.CharField(max_length=4)
    phone_number = models.CharField(max_length=16, unique=True, validators=[phoneNumberRegex])
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=None, null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'password']
    
    def __str__(self) -> str:
        return self.name
