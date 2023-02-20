"""urls.py"""
#-----------------------------
# __author__: Upendra Thapa
# __modified__:02/20/2023
# __version__ ="0.1.0"
# __status__ = "development"
#------------------------------

from nautobot.core.views.routers import NautobotUIViewSetRouter
from . import views

router = NautobotUIViewSetRouter()
router.register("ixia24", views.IxiaRowModel24UIViewSet)
router.register("ixia14", views.IxiaRowModel14UIViewSet)

urlpatterns = []

urlpatterns += router.urls
