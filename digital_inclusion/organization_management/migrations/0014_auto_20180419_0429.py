# Generated by Django 2.0.3 on 2018-04-19 04:29

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization_management', '0013_auto_20180419_0301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='key_employees',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=512), blank=True, help_text='Comma seperated list.', null=True, size=None),
        ),
        migrations.AlterField(
            model_name='branch',
            name='services_other',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=256), blank=True, help_text='Comma seperated list.', null=True, size=None),
        ),
        migrations.AlterField(
            model_name='organization',
            name='logo_file',
            field=models.ImageField(help_text='Must be smaller than 4MB.', null=True, upload_to=''),
        ),
    ]
