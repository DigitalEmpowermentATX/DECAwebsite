import random
import string

from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator
from django.utils.translation import gettext as _
from phonenumber_field.modelfields import PhoneNumberField
# from user_management.models import User
from ckeditor.fields import RichTextField


class Service(models.Model):
    type = models.CharField(max_length=256)
    description = models.TextField(max_length=512)

    def __str__(self):
        return str(self.type)

# Create your models here.


class Organization(models.Model):
    name = models.CharField(max_length=512)
    description = RichTextField(max_length=2048, null=True, blank=True)
    website = models.URLField(max_length=512, null=True, blank=True)
    logo_file = models.ImageField(
        null=True, help_text="Must be smaller than 4MB.")
    banner = models.ImageField(
        null=True, blank=True, help_text="Must be smaller than 10MB.")

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


class Language(models.Model):
    name = models.CharField(max_length=15, db_index=True)

    def __str__(self):
        return self.name


class TrainingProgram(models.Model):
    name = models.CharField(max_length=512)

    def __str__(self):
        return self.name


class Branch(models.Model):
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, related_name="branches")
    contact_name = models.CharField(max_length=128)
    contact_phone = PhoneNumberField(blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)
    key_employees = ArrayField(models.CharField(
        max_length=512), null=True, blank=True, help_text="Comma seperated list.")
    address = models.CharField(max_length=512)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    services = models.ManyToManyField(
        Service, related_name="organizations", blank=True)
    services_other = ArrayField(models.CharField(
        max_length=256), null=True, blank=True, help_text="Comma seperated list.")
    lab_machine_count = models.IntegerField(
        blank=True, null=True, verbose_name="Number of lab machines", validators=[MinValueValidator(0)])
    public_access = models.CharField(
        max_length=255, default="Yes", blank=True, null=True)
    training_programs = models.ManyToManyField(TrainingProgram, blank=True)
    languages = models.ManyToManyField(Language, blank=True)

    def __str__(self):
        return '%s -- %s' % (self.organization, self.address)


class OpeningHours(models.Model):
    WEEKDAYS = [
        (1, _("Monday")),
        (2, _("Tuesday")),
        (3, _("Wednesday")),
        (4, _("Thursday")),
        (5, _("Friday")),
        (6, _("Saturday")),
        (7, _("Sunday")),
    ]
    branch = models.ForeignKey(
        Branch,
        on_delete=models.CASCADE,
        related_name="hours",
    )
    weekday = models.IntegerField(
        choices=WEEKDAYS,
        null=False,
    )
    from_hour = models.TimeField()
    to_hour = models.TimeField()
    class Meta:
        verbose_name_plural = "Opening Hours"
        ordering = ('branch__organization__name', 'branch__address', 'weekday', 'from_hour')
        unique_together = ('weekday', 'from_hour', 'to_hour')

    def __str__(self):
        return '%s on %s: %s - %s' % (self.branch, self.get_weekday_display(),
                                 self.from_hour, self.to_hour)


class ActivationToken(models.Model):
    token = models.CharField(max_length=256, primary_key=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    valid = models.BooleanField(default=True)
    @classmethod
    def for_organization(cls, organization):
        return cls(organization=organization,
                   token="".join(random.choice(string.ascii_lowercase) for _ in range(256)))
