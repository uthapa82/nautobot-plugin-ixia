"""forms.py"""

from nautobot.extras.forms import NautobotModelForm
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


