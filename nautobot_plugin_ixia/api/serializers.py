#nautobot_plugin_ixia/api/serializers.py

from nautobot.extras.api.serializers import NautobotModelSerializer

from nautobot_plugin_ixia.models import IxiaRow24

class IxiaRow24Serializer(NautobotModelSerializer):
    class Meta:
        model = IxiaRow24
        fields = "__all__"