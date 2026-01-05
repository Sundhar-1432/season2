from django.db import models
import uuid

class Account(models.Model):
    first_name=models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=False)

class EmailToken(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, unique=True)