"""forms.py"""
#----------------------------------
# __author__: Upendra Thapa
# __modified__:02/20/2023
# __version__ ="0.1.0"
# __status__ = "development"
# __credits__ = "Network To Code"
#----------------------------------

from django import forms

from nautobot.extras.forms import NautobotModelForm, NautobotFilterForm
from nautobot.tenancy.forms import TenancyForm

from .models import IxiaRow24, IxiaRow14, IxiaAppServer
   
#Ixia Row 24 
class IxiaRow24Form(NautobotModelForm, TenancyForm):
    
    class Meta:
        model = IxiaRow24
        fields = [
            "module",
            "speed",
            "port",
            #"status",
            "tenant_group",
            "tenant",
            "description",
        ]

#Ixia Row 14 
class IxiaRow14Form(NautobotModelForm, TenancyForm):
    
    class Meta:
        model = IxiaRow14
        fields = [
            "module",
            "speed",
            "port",
            #"status",
            "tenant_group",
            "tenant",
            "description",
        ]

#Ixia App server 
class IxiaAppServerForm(NautobotModelForm, TenancyForm):
    
    class Meta:
        model = IxiaAppServer
        fields = [
            "username",
            "password",
            "tenant_group",
            #"tenant",
            "description",
        ]

# Ixia Row 24 Filter form 
class IxiaRow24FilterForm(NautobotFilterForm):
    """Filtering/search form for 'IxiaRow24Form' objects"""
    
    model = IxiaRow24
    q = forms.CharField(required=False, label="Search")
    module = forms.CharField(required=False)
    port = forms.IntegerField(required=False, max_value=13, min_value=0)
    ntm = forms.CharField(required=False, label= "NTM# M# P#", help_text="eg. NTM1 M2 P34")
    
    
# Ixia Row 14 Filter form 
class IxiaRow14FilterForm(NautobotFilterForm):
    """Filtering/search form for 'IxiaRow14Form' objects"""
    
    model = IxiaRow14
    q = forms.CharField(required=False, label="Search")
    module = forms.CharField(required=False)
    port = forms.IntegerField(required=False, max_value=13, min_value=0)
    ntm = forms.CharField(required=False, label= "NTM# M# P#", help_text="eg. NTM1 M2 P34")
    
    
# Ixia AppServer Filter 
class IxiaAppServerFilterForm(NautobotFilterForm):
    """Filtering/search form for 'IxiaAppServerForm' objects"""
    
    model = IxiaAppServer
    q = forms.CharField(required=False, label="Search")
    #tenant = forms.CharField(required=False, label="Name")
    username = forms.CharField(required=False)
