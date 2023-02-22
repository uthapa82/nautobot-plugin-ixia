"""models.py"""
#-----------------------------
# __author__: Upendra Thapa
# __modified__:02/20/2023
# __version__ ="0.1.0"
# __status__ = "development"
#------------------------------

from nautobot.core.models.generics import PrimaryModel
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.db import models
from nautobot.core.fields import AutoSlugField
from nautobot.core.models.generics import PrimaryModel
from django.urls import reverse

# Ixia row 24 Models
class IxiaRow24(PrimaryModel):
    """Model representing Ixia devices and other information"""
    module = models.CharField(max_length=200, help_text ="Module Name eg Module1")
    speed = models.CharField(max_length=200, default="10G", help_text ="Speed of Module eg 10G")
    slug = AutoSlugField(populate_from="module")
    port = models.IntegerField(help_text="Port number in the Module")
    status = models.CharField(max_length=200, help_text="Status of the Port Available/Reserved")
    tenant = models.CharField(max_length=200, help_text="Tenant the port is reserved to")
    description = models.CharField(max_length=200, help_text="Any additional Information")
    
    # method to calculate the canonical URL for an object
    # string to refer object over HTTP
    def get_absolute_url(self):
        return reverse("plugins:nautobot_plugin_ixia:ixiarow24", args=[self.slug])

    # __str__ representation of object, to view in shell_plus
    def __str__(self):
        return self.module
    
# Ixia Row 14 Model 
class IxiaRow14(PrimaryModel):
    """Model representing Ixia devices and other information"""
    module = models.CharField(max_length=200, help_text ="Module Name eg Module1")
    speed = models.CharField(max_length=200, default="10G", help_text ="Speed of Module eg 10G")
    slug = AutoSlugField(populate_from="module")
    port = models.IntegerField(help_text="Port number in the Module")
    status = models.CharField(max_length=200, help_text="Status of the Port Available/Reserved")
    tenant = models.CharField(max_length=200, help_text="Tenant the port is reserved to")
    description = models.CharField(max_length=200, help_text="Any additional Information")
    
    # method to calculate the canonical URL for an object
    # string to refer object over HTTP
    def get_absolute_url(self):
        return reverse("plugins:nautobot_plugin_ixia:ixiarow14", args=[self.slug])
    
    # __str__ representation of object, to view in shell_plus
    def __str__(self):
        return self.module

# Ixia App Server Credentials 
class IxiaAppServer(PrimaryModel):
    """Model representing Ixia App server Credentials and user"""
    username = models.CharField(max_length=200, help_text ="@username")
    slug = AutoSlugField(populate_from="username")
    password = models.CharField(max_length=200, help_text="@password")
    tenant = models.CharField(max_length=200, help_text="@user using it")
    description = models.CharField(max_length=200, null=True, help_text="Any additional Information/Project")
    
    # method to calculate the canonical URL for an object
    # string to refer object over HTTP
    def get_absolute_url(self):
        return reverse("plugins:nautobot_plugin_ixia:ixiaappserver", args=[self.slug])

    # __str__ representation of object, to view in shell_plus
    def __str__(self):
        return self.username