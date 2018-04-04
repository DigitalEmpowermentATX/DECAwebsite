from django.db import models
from django.contrib.postgres.fields import ArrayField
from phonenumber_field.modelfields import PhoneNumberField
from user_management.models import User



class Service(models.Model):
    type = models.CharField(max_length=256)
    description = models.TextField(max_length=512)    
    def __str__(self):
        return str(self.type)

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=512)
    description = models.TextField(max_length=2048)
    website = models.URLField(max_length=512)
    contact_name = models.CharField(max_length=128)
    contact_phone = PhoneNumberField()
    contact_email = models.EmailField()
    key_employees = ArrayField(models.CharField(max_length=512), null=True)
    logo_file = models.ImageField(null=True)
    services = models.ManyToManyField(Service, related_name="organizations")
    def __str__(self):
        return str(self.name)
