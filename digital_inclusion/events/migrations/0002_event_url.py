# Generated by Django 2.0.3 on 2018-04-22 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='url',
            field=models.URLField(null=True),
        ),
    ]