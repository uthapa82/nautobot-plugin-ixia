# Generated by Django 3.2.18 on 2023-02-28 06:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nautobot_plugin_ixia', '0005_auto_20230228_0348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ixiarow24',
            name='ntm',
            field=models.CharField(blank=True, max_length=200, validators=[django.core.validators.RegexValidator('\x08NTM[1-3]\\s\x08M([0-9]|10)\\s\x08P([1-9]|[1-8][0-9]|9[0-5])', 'Incorrect Format! NTM#<space>M#<space>P#')]),
        ),
    ]
