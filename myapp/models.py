import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone_number = models.CharField(max_length=12, unique=True, null=True, blank=True)
    id_number = models.CharField(max_length=13, unique=True, null=True, blank=True)
    bank_account_number = models.CharField(max_length=20, unique=True, null=True, blank=True)


class ProductTypes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50, null=True, blank=True)
    discount = models.CharField(max_length=50, null=True, blank=True)
