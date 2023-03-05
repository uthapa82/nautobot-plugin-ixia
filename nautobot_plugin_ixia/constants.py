from django.db.models import Q 

IXIA_INTERFACE_MODELS = Q(
    Q(app_label="dcim", model="interface")
)