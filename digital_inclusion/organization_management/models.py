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
    address = models.CharField(max_length=512)
    description = models.TextField(max_length=2048)
    website = models.URLField(max_length=512)
    contact_name = models.CharField(max_length=128)
    contact_phone = PhoneNumberField()
    contact_email = models.EmailField()
    key_employees = ArrayField(models.CharField(max_length=512), null=True)
    logo_file = models.ImageField(null=True)
    services = models.ManyToManyField(Service, related_name="organizations")
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)

    def __str__(self):
        return str(self.name)

    # def __dict__(self):
    #     return {
    #         "name": self.name,
    #         "address": self.address,
    #         "description": self.description,
    #         "website": self.website,
    #         "contact_name": self.contact_name,
    #         "contact_phone": self.contact_phone,
    #         "contact_email": self.contact_email,
    #         "key_employees": self.key_employees,
    #         "logo_file": self.logo_file,
    #         "services": self.services,
    #         "latitude": self.latitude,
    #         "longitude": self.longitude,
    #     }
