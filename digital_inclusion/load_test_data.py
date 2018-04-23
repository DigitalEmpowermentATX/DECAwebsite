import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "digital_inclusion.settings")
import django
django.setup()


from organization_management.models import Organization
from events.models import Event

print(Organization.objects.filter(name__istartswith="a"))
print(Event.objects.filter(name__istartswith="a"))

