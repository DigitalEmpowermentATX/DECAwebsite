from django.db import models
from organization_management.models import Organization
# Create your models here.

class Flag(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name="flags")
    issue = models.CharField(max_length=100)
    other = models.TextField(max_length=2048, null=True)
    timestamp = models.DateTimeField(auto_now=True)
    def __str__(self):
        return '%s <> %s' % (self.organization, self.issue)
