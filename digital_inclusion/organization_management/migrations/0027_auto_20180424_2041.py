# Generated by Django 2.0.3 on 2018-04-25 01:41

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('organization_management', '0026_auto_20180424_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='contact_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='branch',
            name='contact_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True),
        ),
    ]