# Generated by Django 2.0.3 on 2018-03-30 13:14

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization_management', '0003_auto_20180330_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='key_employees',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=512), size=None),
        ),
    ]
