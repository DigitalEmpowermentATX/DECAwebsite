# Generated by Django 2.0.3 on 2018-04-04 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization_management', '0009_auto_20180404_1147'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='address',
            field=models.CharField(default='No Address', max_length=512),
            preserve_default=False,
        ),
    ]