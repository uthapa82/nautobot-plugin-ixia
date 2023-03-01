# nautobot_plugin_ixia/api/views.py

from nautobot.extras.api.views import NautobotModelViewSet

from nautobot_plugin_ixia.models import IxiaRow24, IxiaRow14, IxiaAppServer
from . import serializers

# ixia row 24
class IxiaRow24ViewSet(NautobotModelViewSet):
    queryset = IxiaRow24.objects.all()
    serializer_class = serializers.IxiaRow24Serializer


# ixia row 14
class IxiaRow14ViewSet(NautobotModelViewSet):
    queryset = IxiaRow14.objects.all()
    serializer_class = serializers.IxiaRow14Serializer


# ixia row 14
class IxiaAppServerViewSet(NautobotModelViewSet):
    queryset = IxiaAppServer.objects.all()
    serializer_class = serializers.IxiaAppServerSerializer
