# Generated by Django 2.0.3 on 2018-05-01 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0007_auto_20180430_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='security_answer',
            field=models.CharField(blank=True, help_text='The answer to Security question, without this, you cannot reset your password', max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='security_question',
            field=models.CharField(blank=True, help_text='A security question asked when resetting the password', max_length=512, null=True),
        ),
    ]
