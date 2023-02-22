"""views.py"""
#-----------------------------
# __author__: Upendra Thapa
# __modified__:02/20/2023
# __version__ ="0.1.0"
# __status__ = "development"
#------------------------------

from nautobot.core.views import mixins as view_mixins

from .models import IxiaRow24, IxiaRow14, IxiaAppServer
from .tables import IxiaRow24Table, IxiaRow14Table, IxiaAppServerTable


#Ixia Row 24
class IxiaRow24UIViewSet(view_mixins.ObjectListViewMixin, 
                            view_mixins.ObjectDetailViewMixin,
                            view_mixins.ObjectEditViewMixin,
                            view_mixins.ObjectDestroyViewMixin,
                            view_mixins.ObjectBulkDestroyViewMixin,
):
    queryset = IxiaRow24.objects.all()
    table_class = IxiaRow24Table
    
#Ixia Row 14  
class IxiaRow14UIViewSet(view_mixins.ObjectListViewMixin, 
                            view_mixins.ObjectDetailViewMixin,
                            view_mixins.ObjectEditViewMixin,
                            view_mixins.ObjectDestroyViewMixin,
                            view_mixins.ObjectBulkDestroyViewMixin,
):
    queryset = IxiaRow14.objects.all()
    table_class = IxiaRow14Table

#Ixia AppServer Info
class IxiaAppServerUIViewSet(view_mixins.ObjectListViewMixin, 
                            view_mixins.ObjectDetailViewMixin,
                            view_mixins.ObjectEditViewMixin,
                            view_mixins.ObjectDestroyViewMixin,
                            view_mixins.ObjectBulkDestroyViewMixin,
):
    queryset = IxiaAppServer.objects.all()
    table_class = IxiaAppServerTable