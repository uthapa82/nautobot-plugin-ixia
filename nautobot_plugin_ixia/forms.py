"""forms.py"""

from nautobot.extras.forms import NautobotModelForm
from .models import IxiaRow24

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