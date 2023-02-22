#nautobot_plugin_ixia/api/urls.py

from nautobot.core.api import OrderedDefaultRouter

from . import views

router = OrderedDefaultRouter()
router.register("ixiarow24", views.IxiaRow24ViewSet)
router.register("ixiarow14", views.IxiaRow14ViewSet)
router.register("ixia-app-server", views.IxiaAppServerViewSet)

urlpatterns = router.urls