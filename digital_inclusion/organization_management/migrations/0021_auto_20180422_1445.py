# Generated by Django 2.0.3 on 2018-04-22 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization_management', '0020_auto_20180422_1427'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpeningHours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekday', models.IntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')])),
                ('from_hour', models.TimeField()),
                ('to_hour', models.TimeField()),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hours', to='organization_management.Branch')),
            ],
            options={
                'ordering': ('branch__name', 'weekday', 'from_hour'),
            },
        ),
        migrations.AlterUniqueTogether(
            name='openinghours',
            unique_together={('weekday', 'from_hour', 'to_hour')},
        ),
    ]
