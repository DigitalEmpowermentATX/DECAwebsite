# Generated by Django 2.0.3 on 2018-04-19 07:13

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization_management', '0015_organization_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='description',
            field=ckeditor.fields.RichTextField(max_length=2048),
        ),
    ]
