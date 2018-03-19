from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    REQUIRED_FIELDS = []
    organization = models.ForeignKey("organization_management.Organization", related_name="users", on_delete=models.CASCADE)
