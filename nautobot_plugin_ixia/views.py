"""views.py"""
#-----------------------------
# __author__: Upendra Thapa
# __modified__:02/20/2023
# __version__ ="0.1.0"
# __status__ = "development"
#------------------------------

from nautobot.core.views import mixins as view_mixins 

from .models import IxiaRowModel24, IxiaRowModel14
from .tables import IxiaRowModel24Table, IxiaRowModel14Table

class IxiaRowModel24UIViewSet(view_mixins.ObjectListViewMixin, 
                            view_mixins.ObjectDetailViewMixin,
                            view_mixins.ObjectEditViewMixin,
                            view_mixins.ObjectDestroyViewMixin,
                            view_mixins.ObjectBulkDestroyViewMixin,
):
    queryset = IxiaRowModel24.objects.all()
    table_class = IxiaRowModel24Table
    
class IxiaRowModel14UIViewSet(view_mixins.ObjectListViewMixin, 
                            view_mixins.ObjectDetailViewMixin,
                            view_mixins.ObjectEditViewMixin,
                            view_mixins.ObjectDestroyViewMixin,
                            view_mixins.ObjectBulkDestroyViewMixin,
):
    queryset = IxiaRowModel14.objects.all()
    table_class = IxiaRowModel14Table