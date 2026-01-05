from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

def send_mail_view(requeste,mail,verify_url):
    send_mail(
        'Verify  Email',
        f'Click to verify the email\n{verify_url}',
        settings.EMAIL_HOST_USER,
        [mail]


    )
    return HttpResponse("email sended success fully")