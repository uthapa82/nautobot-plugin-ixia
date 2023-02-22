"""tables.py"""
#-----------------------------
# __author__: Upendra Thapa
# __modified__:02/20/2023
# __version__ ="0.1.0"
# __status__ = "development"
#------------------------------

import django_tables2 as tables 
from nautobot.utilities.tables import BaseTable, ToggleColumn

from .models import IxiaRow24, IxiaRow14, IxiaAppServer

#table definition using Nautobot base template
class IxiaRow24Table(BaseTable):
    
    #creates alias name 
    pk = ToggleColumn()
    module = tables.LinkColumn(verbose_name="Module Number")
    description = tables.Column(verbose_name="Description/Project")
    
    class Meta(BaseTable.Meta):
        model = IxiaRow24
        
        #determines which field to display
        fields = (
            "pk",
            "module",
            "speed",
            "port",
            "status",
            "tenant",
            "description",
        )
        #determines default columns 
        default_columns = (
            "pk",
            "module",
            "speed",
            "port",
            "status",
            "tenant",
            "description"
        )
# Ixia Row 14
class IxiaRow14Table(BaseTable):
    
    #creates alias name 
    pk = ToggleColumn()
    module = tables.LinkColumn(verbose_name="Module Number")
    description = tables.Column(verbose_name="Description/Project")
    
    class Meta(BaseTable.Meta):
        model = IxiaRow14
        
        #determines which field to display
        fields = (
            "pk",
            "module",
            "speed",
            "port",
            "status",
            "tenant",
            "description",
        )
        #determines default columns 
        default_columns = (
            "pk",
            "module",
            "speed",
            "port",
            "status",
            "tenant",
            "description"
        )

#Ixia App server Table 
class IxiaAppServerTable(BaseTable):
    
    #creates alias name 
    pk = ToggleColumn()
    class Meta(BaseTable.Meta):
        model = IxiaAppServer
        
        #determines which field to display
        fields = (
            "pk",
            "username",
            "password",
            "tenant",
            "description",
        )
        #determines default columns 
        default_columns = (
            "pk",
            "username",
            "password",
            "tenant",
            "description",
        )