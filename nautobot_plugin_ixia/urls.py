"""urls.py"""
#--------------------------------
# __author__: Upendra Thapa
# __modified__:02/20/2023
# __version__ ="0.1.0"
# __status__ = "development"
# __credits__ = "Network To Code"
#--------------------------------

from nautobot.core.views.routers import NautobotUIViewSetRouter
from . import views

router = NautobotUIViewSetRouter()
router.register("ixia24", views.IxiaRow24UIViewSet)
router.register("ixia14", views.IxiaRow14UIViewSet)
router.register("ixia-app-server", views.IxiaAppServerUIViewSet)


urlpatterns = []

urlpatterns += router.urls
