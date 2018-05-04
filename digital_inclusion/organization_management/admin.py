from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin
from organization_management import models
# Register your models here.

admin.site.register(models.Service)
class OrganizationResource(resources.ModelResource):
    class Meta:
        model = models.Organization
class OrganizationAdmin(ImportExportActionModelAdmin):
    resource_class = OrganizationResource
class BranchResource(resources.ModelResource):
    class Meta:
        model = models.Branch
class BranchAdmin(ImportExportActionModelAdmin):
    resource_class = BranchResource
admin.site.register(models.Organization, OrganizationAdmin)
admin.site.register(models.Branch, BranchAdmin)
admin.site.register(models.Language)
admin.site.register(models.TrainingProgram)
admin.site.register(models.OpeningHours)