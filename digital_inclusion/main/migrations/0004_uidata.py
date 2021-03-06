# Generated by Django 2.0.3 on 2018-05-01 04:37

import os
from django.db import migrations, models
from django.core import serializers
fixture_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../fixtures'))
fixture_filename = 'initial_data.json'
def load_ui_fixtures(apps, schema_editor):
    fixture_file = os.path.join(fixture_dir, fixture_filename)

    fixture = open(fixture_file, 'rb')
    objects = serializers.deserialize('json', fixture, ignorenonexistent=True)
    for obj in objects:
        obj.save()
    fixture.close()
class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_uicomponent_name'),
    ]

    operations = [
        migrations.RunPython(load_ui_fixtures, reverse_code=migrations.RunPython.noop)
    ]
