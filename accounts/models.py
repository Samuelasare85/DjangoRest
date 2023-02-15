from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.core.validators import RegexValidator

phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
class UserManager(BaseUserManager):
    def create_user(self, id,email,name,otp,phone_number,is_superuser,is_verified,date_joined,password=None):

        """
        Creates and saves a User with the given user_name and password.
        """

        user = self.model(
            email=email,
            id=id,
            name=name,
            otp=otp,
            phone_number=phone_number,
            is_superuser=is_superuser,
            is_verified=is_verified,
            date_joined=date_joined
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, id,email,name,otp,phone_number,is_superuser,is_verified,date_joined,password=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email=email,
            id=id,
            name=name,
            otp=otp,
            phone_number=phone_number,
            is_superuser=is_superuser,
            is_verified=is_verified,
            date_joined=date_joined
        )
        user.is_superuser = True
        user.save()
        return user
class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    name =  models.CharField(max_length=255, verbose_name="Full name")
    email = models.EmailField(max_length=255, unique=True)
    otp = models.CharField(max_length=4)
    phone_number = models.CharField(max_length=16, unique=True, validators=[phoneNumberRegex])
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=None, null=True)
    is_verified = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'password']
    objects=UserManager()
    
    # def __str__(self) -> str:
    #     return self.name
