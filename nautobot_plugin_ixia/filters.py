"""filters.py"""
#---------------------------------
# __author__: Upendra Thapa
# __modified__:02/23/2023
# __version__ ="0.1.0"
# __status__ = "development"
# __credits__ = "Network To Code"
#---------------------------------

from django.core.exceptions import ValidationError
from nautobot.extras.filters import NautobotFilterSet, StatusModelFilterSetMixin
from nautobot.utilities.filters import SearchFilter
from nautobot.tenancy.filters  import TenancyModelFilterSetMixin


from nautobot_plugin_ixia.models import IxiaRow24, IxiaRow14, IxiaAppServer

__all__ = (
    "IxiaRow24FilterSet",
    "IxiaRow14FilterSet",
    "IxiaAppServerFilterSet",
)
# Ixia Row 24
class IxiaRow24FilterSet(NautobotFilterSet, TenancyModelFilterSetMixin, StatusModelFilterSetMixin):
    """Filter for filtering IxiaRow24 Objects."""
    
    q = SearchFilter(
        filter_predicates={
            "module": "icontains",
            "port": "icontains",
            "ntm": "icontains",
        }
    )

    class Meta:
        model = IxiaRow24
        fields = "__all__"

# Ixia Row 14
class IxiaRow14FilterSet(NautobotFilterSet, TenancyModelFilterSetMixin, StatusModelFilterSetMixin):
    """Filter for filtering IxiaRow14 Objects."""
    
    q = SearchFilter(
        filter_predicates={
            "module": "icontains",
            "port": "icontains",
            "ntm": "icontains",
        }
    )
   
    class Meta:
        model = IxiaRow14
        fields = "__all__"

# Ixia App Server 
class IxiaAppServerFilterSet(NautobotFilterSet, TenancyModelFilterSetMixin, StatusModelFilterSetMixin):
    """Filter for filtering IxiaRow24 Objects."""
    
    q = SearchFilter(
        filter_predicates={
            "username": "icontains",
        }
    )
 
    class Meta:
        model = IxiaAppServer
        fields = "__all__"