from django.core.mail import send_mail
from random import randint
from ..models import User
from django.conf import settings
from django.template.loader import render_to_string



def email_notification(email):
    otp = randint(1000, 9999)
    user = User.objects.get(email=email)
    user.otp = otp
    user.save()
    html_message = render_to_string('accounts/verifyotp.html', {'user': user})
    send_mail(
                'Account verification',
                html_message,
                settings.EMAIL_HOST_USER,
                [email, 'samuelasare859@gmail.com'])