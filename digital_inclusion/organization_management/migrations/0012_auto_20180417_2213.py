# Generated by Django 2.0.3 on 2018-04-17 22:13

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('organization_management', '0011_auto_20180412_0501'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=128)),
                ('contact_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('contact_email', models.EmailField(max_length=254)),
                ('key_employees', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=512), null=True, size=None)),
                ('address', models.CharField(max_length=512)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='organization',
            name='address',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='contact_email',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='contact_name',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='contact_phone',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='key_employees',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='longitude',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='services',
        ),
        migrations.AddField(
            model_name='branch',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branches', to='organization_management.Organization'),
        ),
        migrations.AddField(
            model_name='branch',
            name='services',
            field=models.ManyToManyField(related_name='organizations', to='organization_management.Service'),
        ),
    ]
