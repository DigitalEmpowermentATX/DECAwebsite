# Generated by Django 2.0.3 on 2018-03-30 12:43

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='key_employees',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(max_length=512), size=None),
        ),
    ]