# Generated by Django 3.2.18 on 2023-03-01 05:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nautobot_plugin_ixia', '0003_ixiaappserver_tenant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ixiarow14',
            name='ntm',
            field=models.CharField(blank=True, max_length=200, unique=True, validators=[django.core.validators.RegexValidator(code='invalid', message='Invalid Format, NTM[1-3]<space>M[0-10]<space>P[1-96]', regex='NTM[1-3]\\sM([0-9]|10)\\sP([0-9][0-6]|[0-9])')]),
        ),
        migrations.AlterField(
            model_name='ixiarow24',
            name='ntm',
            field=models.CharField(blank=True, max_length=200, unique=True, validators=[django.core.validators.RegexValidator(code='invalid', message='Invalid Format, NTM[1-3]<space>M[0-10]<space>P[1-96]', regex='NTM[1-3]\\sM([0-9]|10)\\sP([0-9][0-6]|[0-9])')]),
        ),
    ]
