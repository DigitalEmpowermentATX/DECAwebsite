# Generated by Django 2.0.3 on 2018-04-22 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization_management', '0021_auto_20180422_1445'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='openinghours',
            options={'ordering': ('branch__organization__name', 'branch__address', 'weekday', 'from_hour')},
        ),
    ]
