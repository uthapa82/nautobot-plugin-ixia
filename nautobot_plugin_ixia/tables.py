"""tables.py"""
# ---------------------------------
# __author__: Upendra Thapa
# __modified__:02/20/2023
# __version__ ="0.1.0"
# __status__ = "development"
# __credits__ = "Network To Code"
# ----------------------------------
import django_tables2 as tables
from nautobot.utilities.tables import BaseTable, ToggleColumn
from nautobot.tenancy.tables import TenantColumn
from nautobot.extras.tables import StatusTableMixin

from .models import IxiaRow24, IxiaRow14, IxiaAppServer

# table definition using Nautobot base template
class IxiaRow24Table(StatusTableMixin, BaseTable):

    pk = ToggleColumn()
    tenant = TenantColumn()
    assigned_object = tables.Column(linkify=True, orderable=False, verbose_name="Port")
    assigned_object_parent = tables.Column(
        accessor="assigned_object__parent",
        linkify=True,
        orderable=False,
        verbose_name="Interface Parent",
    )
    description = tables.Column(verbose_name="Description/Project")

    class Meta(BaseTable.Meta):
        model = IxiaRow24

        # determines which field to display
        fields = (
            "pk",
            "assigned_object",
            "assigned_object_parent",
            "speed",
            "status",
            "tenant",
            "description",
        )
        default_columns = (
            "pk",
            "assigned_object",
            "speed",
            "status",
            "tenant",
            "description",
        )


# table for Ixia Row 14
class IxiaRow14Table(StatusTableMixin, BaseTable):

    # creates alias name
    pk = ToggleColumn()
    tenant = TenantColumn()
    assigned_object = tables.Column(linkify=True, orderable=False, verbose_name="Port")
    assigned_object_parent = tables.Column(
        accessor="assigned_object__parent",
        linkify=True,
        orderable=False,
        verbose_name="Interface Parent",
    )
    description = tables.Column(verbose_name="Description/Project")


    class Meta(BaseTable.Meta):
        model = IxiaRow14

        # determines which field to display
        fields = (
            "pk",
            "assigned_object",
            "assigned_object_parent",
            "speed",
            "status",
            "tenant",
            "description",
        )
        
        default_columns = (
            "pk",
            "assigned_object",
            "speed",
            "status",
            "tenant",
            "description",
        )


# Ixia App server Table
class IxiaAppServerTable(StatusTableMixin, BaseTable):

    # creates alias name
    pk = ToggleColumn()
    # tenant = TenantColumn()
    username = tables.LinkColumn()

    class Meta(BaseTable.Meta):
        model = IxiaAppServer

        # determines which field to display
        fields = (
            "pk",
            "username",
            "password",
            "status",
            "tenant",
            "description",
        )

        default_columns = (
            "pk",
            "username",
            "password",
            "status",
            "tenant",
            "description",
        )
