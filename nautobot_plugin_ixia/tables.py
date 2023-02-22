"""tables.py"""
#-----------------------------
# __author__: Upendra Thapa
# __modified__:02/20/2023
# __version__ ="0.1.0"
# __status__ = "development"
#------------------------------

from nautobot.utilities.tables import BaseTable

from .models import IxiaRow24, IxiaRow14, IxiaAppServer

#table definition using Nautobot base template
class IxiaRow24Table(BaseTable):
    
    class Meta(BaseTable.Meta):
        model = IxiaRow24

class IxiaRow14Table(BaseTable):
    
    class Meta(BaseTable.Meta):
        model = IxiaRow14

class IxiaAppServerTable(BaseTable):
    
    class Meta(BaseTable.Meta):
        model = IxiaAppServer
    
