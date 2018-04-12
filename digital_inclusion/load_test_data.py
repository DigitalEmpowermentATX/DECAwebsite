import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "digital_inclusion.settings")
import django
django.setup()


from organization_management import models


print(models)