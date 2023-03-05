"""models.py"""
# -----------------------------
# __author__: Upendra Thapa
# __modified__:02/20/2023
# __version__ ="0.1.0"
# __status__ = "development"
# __credits__ = "Network To Code"
# ------------------------------

from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from nautobot.core.fields import AutoSlugField
from nautobot.core.models.generics import PrimaryModel
from nautobot.extras.models import StatusModel
from nautobot.extras.utils import extras_features
from nautobot.dcim.models import Interface

from nautobot_plugin_ixia.choices import SpeedChoices
from nautobot_plugin_ixia.constants import IXIA_INTERFACE_MODELS
import logging


logger = logging.getLogger(__name__)

#Ixia row 24 models 
@extras_features(
    "statuses",
    "relationships",
)
class IxiaRow24(PrimaryModel, StatusModel):
    """Model representing Ixia devices and other information""" 
    #Port 
    assigned_object_type = models.ForeignKey(
        to=ContentType,
        limit_choices_to=IXIA_INTERFACE_MODELS,
        on_delete=models.PROTECT,
        related_name="ixiarow24s",
        blank=True,
        null=True,
    )
    assigned_object_id = models.UUIDField(blank=True, null=True, db_index=True)
    assigned_object = GenericForeignKey(ct_field="assigned_object_type", fk_field="assigned_object_id")
    slug = AutoSlugField(populate_from="assigned_object_type")
    
    #Speed 
    speed = models.CharField(
        max_length=200, choices=SpeedChoices, default="10G", help_text="Speed of Port, deafult 10G"
    )
    
    #status 
    
    #tenant 
    tenant = models.ForeignKey(
        to="tenancy.Tenant",
        on_delete=models.PROTECT,
        related_name="ixiarow24s",
        null=True,
        blank=True,
        help_text="Tenant the Port is Reserved to",
    )
    
    #Description
    description = models.CharField(max_length=200, blank=True, help_text="Any additional Information/Project")

    csv_header = [
        "assigned_object_type",
        "speed",
        "status",
        "tenant",
        "description"
    ]
    
    class Meta:
        verbose_name = "IXIA Row 24 Port"
        verbose_name_plural = "IXIA Row 24 Ports"  

    # method to calculate the canonical URL for an object
    # string to refer object over HTTP
    def get_absolute_url(self):
        return reverse("plugins:nautobot_plugin_ixia:ixiarow24", args=[self.slug])
    
    # __str__ representation of object, to view in shell_plus
    def __str__(self):
        return self.speed
    
    def clean(self):
        return super().clean()
  
    # export to csv
    def to_csv(self):
        
        return (
            self.assigned_object_type.name,
            self.speed,
            self.status,
            self.tenant if self.tenant else None,
            self.description if self.tenant else None,
        )
        
            
#Ixia row 14 models 
@extras_features(
    "statuses",
    "relationships",
)
class IxiaRow14(PrimaryModel, StatusModel):
    """Model representing Ixia devices and other information""" 
    #Port 
    assigned_object_type = models.ForeignKey(
        to=ContentType,
        limit_choices_to=IXIA_INTERFACE_MODELS,
        on_delete=models.PROTECT,
        related_name="ixiarow14s",
        blank=True,
        null=True,
    )
    assigned_object_id = models.UUIDField(blank=True, null=True, db_index=True)
    assigned_object = GenericForeignKey(ct_field="assigned_object_type", fk_field="assigned_object_id")
    slug = AutoSlugField(populate_from="assigned_object_type")
    
    #Speed 
    speed = models.CharField(
        max_length=200, choices=SpeedChoices, default="10G", help_text="Speed of Port, deafult 10G"
    )
    
    #status
    #tenant 
    tenant = models.ForeignKey(
        to="tenancy.Tenant",
        on_delete=models.PROTECT,
        related_name="ixiarow14s",
        null=True,
        blank=True,
        help_text="Tenant the Port is Reserved to",
    )
    
    #Description
    description = models.CharField(max_length=200, blank=True, help_text="Any additional Information/Project")

    csv_header = [
        "assigned_object_type",
        "speed",
        "status",
        "tenant",
        "description"
    ]
    
    class Meta:
        verbose_name = "IXIA Row 14 Port"
        verbose_name_plural = "IXIA Row 14 Ports" 


    # method to calculate the canonical URL for an object
    # string to refer object over HTTP
    def get_absolute_url(self):
        return reverse("plugins:nautobot_plugin_ixia:ixiarow14", args=[self.slug])
    
    # __str__ representation of object, to view in shell_plus
    def __str__(self):
        return self.speed
    
    def clean(self):
        return super().clean()
  
    # export to csv
    def to_csv(self):
        
        return (
            self.assigned_object_type.name,
            self.speed,
            self.status,
            self.tenant if self.tenant else None,
            self.description if self.tenant else None,
        )
        

#Ixia App Server Models 
@extras_features(
    "statuses",
    "relationships",
)
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
