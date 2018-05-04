# Generated by Django 2.0.3 on 2018-04-30 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0006_auto_20180430_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='security_answer',
            field=models.CharField(default=' ', help_text='The answer to Security question, without this, you cannot reset your password', max_length=512),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='security_question',
            field=models.CharField(default=' ', help_text='A security question asked when resetting the password', max_length=512),
            preserve_default=False,
        ),
    ]
