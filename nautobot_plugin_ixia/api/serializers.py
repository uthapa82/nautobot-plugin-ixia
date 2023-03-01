# nautobot_plugin_ixia/api/serializers.py

from nautobot.extras.api.serializers import NautobotModelSerializer

from nautobot_plugin_ixia.models import IxiaRow24, IxiaRow14, IxiaAppServer

# ixia row 24
class IxiaRow24Serializer(NautobotModelSerializer):
    class Meta:
        model = IxiaRow24
        fields = "__all__"


# ixia row 14
class IxiaRow14Serializer(NautobotModelSerializer):
    class Meta:
        model = IxiaRow14
        fields = "__all__"


# ixia app server
class IxiaAppServerSerializer(NautobotModelSerializer):
    class Meta:
        model = IxiaAppServer
        fields = "__all__"
