"""tables.py"""
#-----------------------------
# __author__: Upendra Thapa
# __modified__:02/20/2023
# __version__ ="0.1.0"
# __status__ = "development"
#------------------------------

from nautobot.utilities.tables import BaseTable

from .models import IxiaRowModel24, IxiaRowModel14

#table definition using Nautobot base template
class IxiaRowModel24Table(BaseTable):
    
    class Meta(BaseTable.Meta):
        model = IxiaRowModel24

class IxiaRowModel14Table(BaseTable):
    
    class Meta(BaseTable.Meta):
        model = IxiaRowModel14
    
