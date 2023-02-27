# Generated by Django 3.2.18 on 2023-02-27 13:15

from django.db import migrations
import django.db.models.deletion
import nautobot.extras.models.statuses


class Migration(migrations.Migration):

    dependencies = [
        ('extras', '0054_scheduledjob_kwargs_request_user_change'),
        ('nautobot_plugin_ixia', '0003_ixiaappserver_tenant'),
    ]

    operations = [
        migrations.AddField(
            model_name='ixiarow24',
            name='status',
            field=nautobot.extras.models.statuses.StatusField(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='nautobot_plugin_ixia_ixiarow24_related', to='extras.status'),
        ),
    ]
