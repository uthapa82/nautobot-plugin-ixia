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
from nautobot.tenancy.filters  import TenancyFilterSet


from nautobot_plugin_ixia.models import IxiaRow24, IxiaRow14, IxiaAppServer


# Ixia Row 24
class IxiaRow24FilterSet(NautobotFilterSet, TenancyFilterSet, StatusModelFilterSetMixin):
    """Filter for filtering IxiaRow24 Objects."""
    
    q = SearchFilter(
        filter_predicates={
            "module": "icontains",
            "port": "icontains",
            "ntm": "icontains",
        }
    )

    #generate filter fields for all
    class Meta:
        model = IxiaRow24
        fields = "__all__"
    

# Ixia Row 14
class IxiaRow14FilterSet(NautobotFilterSet, TenancyFilterSet, StatusModelFilterSetMixin):
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
class IxiaAppServerFilterSet(NautobotFilterSet, TenancyFilterSet, StatusModelFilterSetMixin):
    """Filter for filtering IxiaRow24 Objects."""
    
    q = SearchFilter(
        filter_predicates={
            "username": "icontains",
        }
    )
 
    class Meta:
        model = IxiaAppServer
        fields = "__all__"