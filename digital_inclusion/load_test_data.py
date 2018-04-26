import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "digital_inclusion.settings")
import django
import csv
from pprint import pprint

django.setup()

from organization_management.models import Organization, Branch, Language
from events.models import Event


def isint(n):
    try:
        int(n)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    lines = list(csv.DictReader(sys.stdin))
    orgs = {org: [] for org in set(line["Program"] for line in lines)}
    for line in lines:
        orgs[line["Program"]].append(line)

    for organization_name, branches in orgs.items():
        parent_org, created = Organization.objects.get_or_create(
            name=organization_name,
            description=None,
            website=None,
        )
        for branch in branches:
            lat, lon = branch["Location 1"].split("(")[-1].replace(")", "").split(", ")
            languages = [language for language in Language.objects.all() if
                                       language.name in "English " + branch["Non-English Speaking Languages"]]
            b = Branch(organization=parent_org,
                        contact_name="n/a",
                        contact_phone=branch["Phone"],
                        contact_email=None,
                        address=branch["Location"],
                        latitude=float(lat),
                        longitude=float(lon),
                        services_other=None,
                        lab_machine_count=branch["# of Machines"].split(" ")[0] if isint(
                            branch["# of Machines"].split(" ")[0]) else None,
                        public_access=branch["Public Access?"],
                        )
            b.save()
            for language in languages:
                b.languages.add(language)
            b.save()
            # b = Branch(organization=parent_org,
            #        contact_name="n/a",
            #        contact_phone=branch["Phone"],
            #        contact_email=None,
            #        address=branch["Location"],
            #        latitude=None,
            #        longitude=None,
            #        services=None,
            #        services_other=None,
            #        lab_machine_count=None,
            #        public_access=None,
            #        training_programs=None,
            #        languages=None,
            #        ).save()
