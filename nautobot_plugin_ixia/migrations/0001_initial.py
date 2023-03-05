# Generated by Django 3.2.18 on 2023-03-05 18:19

import django.core.serializers.json
from django.db import migrations, models
import django.db.models.deletion
import nautobot.core.fields
import nautobot.extras.models.mixins
import nautobot.extras.models.statuses
import taggit.managers
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("tenancy", "0002_auto_slug"),
        ("extras", "0047_enforce_custom_field_slug"),
    ]

    operations = [
        migrations.CreateModel(
            name="IxiaRow24",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("created", models.DateField(auto_now_add=True, null=True)),
                ("last_updated", models.DateTimeField(auto_now=True, null=True)),
                (
                    "_custom_field_data",
                    models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder),
                ),
                ("assigned_object_id", models.UUIDField(blank=True, db_index=True, null=True)),
                (
                    "slug",
                    nautobot.core.fields.AutoSlugField(
                        blank=True, max_length=100, populate_from="assigned_object_type", unique=True
                    ),
                ),
                ("speed", models.CharField(default="10G", max_length=200)),
                ("description", models.CharField(blank=True, max_length=200)),
                (
                    "assigned_object_type",
                    models.ForeignKey(
                        blank=True,
                        limit_choices_to=models.Q(models.Q(("app_label", "dcim"), ("model", "interface"))),
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="ixiarow24s",
                        to="contenttypes.contenttype",
                    ),
                ),
                (
                    "status",
                    nautobot.extras.models.statuses.StatusField(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="nautobot_plugin_ixia_ixiarow24_related",
                        to="extras.status",
                    ),
                ),
                ("tags", taggit.managers.TaggableManager(through="extras.TaggedItem", to="extras.Tag")),
                (
                    "tenant",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="ixiarow24s",
                        to="tenancy.tenant",
                    ),
                ),
            ],
            options={
                "verbose_name": "IXIA Row 24 Port",
                "verbose_name_plural": "IXIA Row 24 Ports",
            },
            bases=(
                models.Model,
                nautobot.extras.models.mixins.DynamicGroupMixin,
                nautobot.extras.models.mixins.NotesMixin,
            ),
        ),
        migrations.CreateModel(
            name="IxiaRow14",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("created", models.DateField(auto_now_add=True, null=True)),
                ("last_updated", models.DateTimeField(auto_now=True, null=True)),
                (
                    "_custom_field_data",
                    models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder),
                ),
                ("speed", models.CharField(default="10G", max_length=200)),
                ("description", models.CharField(blank=True, max_length=200)),
                (
                    "status",
                    nautobot.extras.models.statuses.StatusField(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="nautobot_plugin_ixia_ixiarow14_related",
                        to="extras.status",
                    ),
                ),
                ("tags", taggit.managers.TaggableManager(through="extras.TaggedItem", to="extras.Tag")),
            ],
            options={
                "verbose_name": "IXIA Row 14 Port",
                "verbose_name_plural": "IXIA Row 14 Ports",
            },
            bases=(
                models.Model,
                nautobot.extras.models.mixins.DynamicGroupMixin,
                nautobot.extras.models.mixins.NotesMixin,
            ),
        ),
        migrations.CreateModel(
            name="IxiaAppServer",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("created", models.DateField(auto_now_add=True, null=True)),
                ("last_updated", models.DateTimeField(auto_now=True, null=True)),
                (
                    "_custom_field_data",
                    models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder),
                ),
                ("username", models.CharField(max_length=200)),
                (
                    "slug",
                    nautobot.core.fields.AutoSlugField(
                        blank=True, max_length=100, populate_from="username", unique=True
                    ),
                ),
                ("password", models.CharField(max_length=200)),
                ("description", models.CharField(blank=True, max_length=200)),
                (
                    "status",
                    nautobot.extras.models.statuses.StatusField(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="nautobot_plugin_ixia_ixiaappserver_related",
                        to="extras.status",
                    ),
                ),
                ("tags", taggit.managers.TaggableManager(through="extras.TaggedItem", to="extras.Tag")),
            ],
            options={
                "abstract": False,
            },
            bases=(
                models.Model,
                nautobot.extras.models.mixins.DynamicGroupMixin,
                nautobot.extras.models.mixins.NotesMixin,
            ),
        ),
    ]
