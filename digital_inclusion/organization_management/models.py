from django.db import models
from django.contrib.postgres.fields import ArrayField
from user_management.models import User


class Service(models.Model):
    type = models.TextField(max_length=256)
    description = models.TextField(max_length=512)    


# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=512)
    description = models.TextField(max_length=2048)
    website = models.URLField(max_length=512)
    contact_name = models.CharField(max_length=128)
    contact_phone = models.CharField(max_length=20)
    key_employees = ArrayField(models.CharField(max_length=512))
    logo_url = models.URLField(max_length=512)
    services = models.ManyToManyField(Service, related_name="organizations")
