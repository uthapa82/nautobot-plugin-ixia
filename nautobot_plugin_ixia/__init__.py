"""Plugin declaration for nautobot_plugin_ixia."""
# Metadata is inherited from Nautobot. If not including Nautobot in the environment, this should be added
try:
    from importlib import metadata
except ImportError:
    # Python version < 3.8
    import importlib_metadata as metadata

__version__ = metadata.version(__name__)

from nautobot.extras.plugins import PluginConfig


class NautobotPluginIxiaConfig(PluginConfig):
    """Plugin configuration for the nautobot_plugin_ixia plugin."""

    name = "nautobot_plugin_ixia"
    verbose_name = "Nautobot Plugin Ixia"
    version = __version__
    author = "Upendra Thapa"
    description = "Nautobot Plugin for Ixia Chassis."
    base_url = "ixia-chassis"
    required_settings = []
    min_version = "1.4.0"
    max_version = "1.9999"
    default_settings = {}
    caching_config = {}


config = NautobotPluginIxiaConfig  # pylint:disable=invalid-name