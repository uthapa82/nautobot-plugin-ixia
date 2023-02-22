#nautobot_plugin_ixia/api/views.py

from nautobot.extras.api.views import NautobotModelViewSet

from nautobot_plugin_ixia.models import IxiaRow24
from . import serializers


class IxiaRow24ViewSet(NautobotModelViewSet):
    queryset = IxiaRow24.objects.all()
    serializer_class = serializers.IxiaRow24Serializer
    