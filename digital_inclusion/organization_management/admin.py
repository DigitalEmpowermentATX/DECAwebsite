from django.contrib import admin
from organization_management import models
# Register your models here.
admin.site.register(models.Organization)
admin.site.register(models.Service)