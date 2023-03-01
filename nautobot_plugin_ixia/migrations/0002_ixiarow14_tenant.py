# Generated by Django 3.2.18 on 2023-03-01 03:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tenancy', '0002_auto_slug'),
        ('nautobot_plugin_ixia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ixiarow14',
            name='tenant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ixiarow14s', to='tenancy.tenant'),
        ),
    ]
