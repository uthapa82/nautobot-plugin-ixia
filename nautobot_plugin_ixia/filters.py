"""filters.py"""
#---------------------------------
# __author__: Upendra Thapa
# __modified__:02/23/2023
# __version__ ="0.1.0"
# __status__ = "development"
# __credits__ = "Network To Code"
#---------------------------------

import django_filters
from nautobot.extras.filters import NautobotFilterSet
from nautobot.utilities.filters import SearchFilter

from nautobot_plugin_ixia.models import IxiaRow24, IxiaRow14, IxiaAppServer

# Ixia Row 24
class IxiaRow24FilterSet(NautobotFilterSet):
    """Filter for filtering IxiaRow24 Objects."""
    
    q = SearchFilter(
        filter_predicates={
            "module": "icontains",
            "port": "icontains",
            "tenant": "icontains",
        }
    )
    #ttl_gte = django_filters.NumberFilter(field_name="ttl", lookup_expr="gte")
    #ttl_lte = django_filters.NumberFilter(field_name="ttl", lookup_expr="lte")
    
    class Meta:
        model = IxiaRow24
        fields = "__all__"

# Ixia Row 14
class IxiaRow14FilterSet(NautobotFilterSet):
    """Filter for filtering IxiaRow14 Objects."""
    
    q = SearchFilter(
        filter_predicates={
            "module": "icontains",
            "port": "icontains",
            "tenant": "icontains",
        }
    )
    #ttl_gte = django_filters.NumberFilter(field_name="ttl", lookup_expr="gte")
    #ttl_lte = django_filters.NumberFilter(field_name="ttl", lookup_expr="lte")
    
    class Meta:
        model = IxiaRow14
        fields = "__all__"

# Ixia Row 14
class IxiaAppServerFilterSet(NautobotFilterSet):
    """Filter for filtering IxiaRow24 Objects."""
    
    q = SearchFilter(
        filter_predicates={
            "tenant": "icontains",
            "username": "icontains",
        }
    )
    ttl_gte = django_filters.NumberFilter(field_name="ttl", lookup_expr="gte")
    ttl_lte = django_filters.NumberFilter(field_name="ttl", lookup_expr="lte")
    
    class Meta:
        model = IxiaAppServer
        fields = "__all__"