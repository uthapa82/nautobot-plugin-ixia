"""forms.py"""
#----------------------------------
# __author__: Upendra Thapa
# __modified__:02/20/2023
# __version__ ="0.1.0"
# __status__ = "development"
# __credits__ = "Network To Code"
#----------------------------------

from nautobot.extras.forms import NautobotModelForm, NautobotFilterForm
from .models import IxiaRow24, IxiaRow14, IxiaAppServer
from django import forms

    
#Ixia Row 24 
class IxiaRow24Form(NautobotModelForm):
    
    class Meta:
        model = IxiaRow24
        fields = [
            "module",
            "speed",
            "port",
            "status",
            "tenant",
            "description",
        ]

#Ixia Row 14 
class IxiaRow14Form(NautobotModelForm):
    
    class Meta:
        model = IxiaRow14
        fields = [
            "module",
            "speed",
            "port",
            "status",
            "tenant",
            "description",
        ]

#Ixia App server 
class IxiaAppServerForm(NautobotModelForm):
    
    class Meta:
        model = IxiaAppServer
        fields = [
            "username",
            "password",
            "tenant",
            "description",
        ]

# Ixia Row 24 Filter form 
class IxiaRow24FilterForm(NautobotFilterForm):
    """Filtering/search form for 'IxiaRow24Form' objects"""
    
    model = IxiaRow24
    q = forms.CharField(required=False, label="Search")
    module = forms.CharField(required=False)
    port = forms.IntegerField(required=False, max_value=13, min_value=0)
    
# Ixia Row 14 Filter form 
class IxiaRow14FilterForm(NautobotFilterForm):
    """Filtering/search form for 'IxiaRow14Form' objects"""
    
    model = IxiaRow14
    q = forms.CharField(required=False, label="Search")
    module = forms.CharField(required=False)
    port = forms.IntegerField(required=False, max_value=13, min_value=0)

# Ixia AppServer Filter 
class IxiaAppServerFilterForm(NautobotFilterForm):
    """Filtering/search form for 'IxiaAppServerForm' objects"""
    
    model = IxiaAppServer
    q = forms.CharField(required=False, label="Search")
    tenant = forms.CharField(required=False, label="Name")
    username = forms.CharField(required=False)
