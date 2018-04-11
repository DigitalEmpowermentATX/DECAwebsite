from django.db import models
from organization_management.models import Organization
# Create your models here.

class Flag(models.Model):
    org_id = models.IntegerField(db_index=True)
    issue = models.CharField(max_length=100)
    other = models.TextField(max_length=2048, null=True)
    timestamp = models.DateTimeField(auto_now=True)
