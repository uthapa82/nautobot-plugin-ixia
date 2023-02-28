"""models.py"""
#-----------------------------
# __author__: Upendra Thapa
# __modified__:02/20/2023
# __version__ ="0.1.0"
# __status__ = "development"
# __credits__ = "Network To Code"
#------------------------------

from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse

from nautobot.core.fields import AutoSlugField
from nautobot.core.models.generics import PrimaryModel
from nautobot.extras.models import StatusModel
from nautobot.extras.utils import extras_features

from nautobot_plugin_ixia.choices import ModuleNumberChoices, SpeedChoices

import logging


__all__ = (
    "IxiaRow24",
    "IxiaRow14",
    "IxiaAppServer",
)


logger = logging.getLogger(__name__)

@extras_features(
    "statuses",
)
# Ixia row 24 Models
class IxiaRow24(PrimaryModel, StatusModel):
    """Model representing Ixia devices and other information"""
    module = models.CharField(max_length=200, choices=ModuleNumberChoices)
    speed = models.CharField(max_length=200, choices=SpeedChoices, default="10G", help_text ="Speed of Module deafult 10G")
    slug = AutoSlugField(populate_from="module")
    port = models.PositiveIntegerField(help_text="Port number in the Module")
    description = models.CharField(max_length=200, blank=True, help_text="Any additional Information/Project")
    
    ntm = models.CharField(
        max_length=200, 
        blank=True, 
        verbose_name="NTM Connection",
        help_text="Format eg.NTM1 M2 P36",
        )
    
    tenant = models.ForeignKey(
        to="tenancy.Tenant",
        on_delete=models.PROTECT,
        related_name="ixiarow24s",
        null=True,
        blank=True,
        help_text="Tenant the port is reserved to",
        )  
    
    csv_headers = ["Module", "Speed", "Port", "NTM", "Status", "Tenant", "Description"]
    
    # method to calculate the canonical URL for an object
    # string to refer object over HTTP
    def get_absolute_url(self):
        return reverse("plugins:nautobot_plugin_ixia:ixiarow24", args=[self.slug])

    # __str__ representation of object, to view in shell_plus
    def __str__(self):
        return self.module
    
    class Meta:
        verbose_name = "IXIA Row 24 Port"
        verbose_name_plural = "IXIA Row 24 Ports"
    
    #export to csv
    def to_csv(self):
        return(
            
            self.module,
            self.speed,
            self.port,
            self.ntm if self.ntm else None,
            self.status,
            self.tenant if self.tenant else None,
            self.description if self.tenant else None,
        )
        
@extras_features(
    "statuses",
)     
# Ixia Row 14 Model 
class IxiaRow14(PrimaryModel, StatusModel):
    """Model representing Ixia devices and other information"""
    module = models.CharField(max_length=200, choices=ModuleNumberChoices)
    speed = models.CharField(max_length=200, choices=SpeedChoices, default="10G", help_text ="Speed of Module eg 10G")
    slug = AutoSlugField(populate_from="module")
    port = models.PositiveIntegerField(help_text="Port number in the Module")
    description = models.CharField(max_length=200, blank=True, help_text="Any additional Information/Project")

    ntm = models.CharField(
        max_length=200, 
        blank=True, 
        verbose_name="NTM Connection",
        help_text="Format eg.NTM1 M2 P36",
        )

    tenant = models.ForeignKey(
        to="tenancy.Tenant",
        on_delete=models.PROTECT,
        related_name="ixiarow14s",
        null=True,
        blank=True,
        verbose_name="tenant",
        help_text="Tenant the port is reserved to",
        ) 
     
    csv_headers = ["Module", "Speed", "Port", "NTM", "Status", "Tenant", "Description"]
    
    class Meta:
        verbose_name = "IXIA Row 14 Port"
        verbose_name_plural = "IXIA Row 14 Ports"   
        
    # method to calculate the canonical URL for an object
    # string to refer object over HTTP
    def get_absolute_url(self):
        return reverse("plugins:nautobot_plugin_ixia:ixiarow14", args=[self.slug])
    
    # __str__ representation of object, to view in shell_plus
    def __str__(self):
        return self.module
    
    #export to csv
    def to_csv(self):
        return(
            
            self.module,
            self.speed,
            self.port,
            self.ntm if self.ntm else None,
            self.status,
            self.tenant if self.tenant else None,
            self.description if self.tenant else None,
        )

@extras_features(
    "statuses",
)  
# Ixia App Server Credentials 
class IxiaAppServer(PrimaryModel, StatusModel):
    """Model representing Ixia App server Credentials and user"""
    username = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from="username")
    password = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True, help_text="Any additional Information/Project Name")

    tenant = models.ForeignKey(
        to="tenancy.Tenant",
        on_delete=models.PROTECT,
        related_name="ixiaappservers",
        null=True,
        blank=True,
        help_text="Tenant the port is reserved to",
        )
      
    # method to calculate the canonical URL for an object
    # string to refer object over HTTP
    def get_absolute_url(self):
        return reverse("plugins:nautobot_plugin_ixia:ixiaappserver", args=[self.slug])

    # __str__ representation of object, to view in shell_plus
    def __str__(self):
        return self.username