from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import Account,EmailToken
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.db import transaction

from django.shortcuts import get_object_or_404

# Create your views here.


def login(request):
    return render(request,"html/login.html",{})
def register(request):
    return render(request,"html/register.html",{})
def save(request):
    if request.method=='POST':

        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']

        account = Account.objects.create(
            first_name=name,
            email=email,
            password=make_password(password),
            is_active=False
        )
        token = EmailToken.objects.create(account=account)

        verify_url = request.build_absolute_uri(
            reverse('verify', args=[token.token])
        )

        send_mail_view(request,email,verify_url)

    return HttpResponse("verification mail should be sendedS")

def verify(request,token):
    token_obj = get_object_or_404(EmailToken, token=token)

    account = token_obj.account
    account.is_active = True
    account.save()

    token_obj.delete()
    return HttpResponse("email verified successfully")

def send_mail_view(requeste,mail,verify_url):
    send_mail(
        'Verify  Email',
        f'Click to verify the email\n{verify_url}',
        settings.EMAIL_HOST_USER,
        [mail]


    )
    return HttpResponse("email sended success fully")