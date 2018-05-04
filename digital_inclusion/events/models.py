from django.db import models
from organization_management.models import Organization

# Create your models here.
class Event(models.Model):
    organization = models.ForeignKey(Organization, on_delete="CASCADE", related_name="events")
    name = models.CharField(max_length=512)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    description = models.TextField(max_length=5096)
    mask_profile = models.BooleanField(default=False)
    contact_name = models.CharField(max_length=256)
    url = models.URLField(null=True, blank=True)