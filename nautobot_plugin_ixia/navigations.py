"""nautobot/extras/navigation.py"""

# modified for ixia plugin
# --------------------------------
# __author__: Upendra Thapa
# __modified__:02/20/2023
# __version__ ="0.1.0"
# __status__ = "development"
# __credits__ = "Network To Code"
# ---------------------------------


from nautobot.core.apps import (
    NavMenuAddButton,
    NavMenuGroup,
    NavMenuItem,
    NavMenuImportButton,
    NavMenuTab,
)

menu_items = (
    NavMenuTab(
        name="IXIA Chassis",
        groups=(
            NavMenuGroup(
                name="Ixia Chassis",
                weight=150,
                items=(
                    NavMenuItem(
                        link="plugins:nautobot_plugin_ixia:ixiarow24_list",
                        name="Ixia Row 24",
                        permissions=[],
                        buttons=(
                            NavMenuAddButton(
                                link="plugins:nautobot_plugin_ixia:ixiarow24_add",
                                permissions=[],
                            ),
                        ),
                    ),
                    NavMenuItem(
                        link="plugins:nautobot_plugin_ixia:ixiarow14_list",
                        name="Ixia Row 14",
                        permissions=[],
                        buttons=(
                            NavMenuAddButton(
                                link="plugins:nautobot_plugin_ixia:ixiarow14_add",
                                permissions=[],
                            ),
                        ),
                    ),
                    NavMenuItem(
                        link="plugins:nautobot_plugin_ixia:ixiaappserver_list",
                        name="Ixia App Server",
                        permissions=[],
                        buttons=(
                            NavMenuAddButton(
                                link="plugins:nautobot_plugin_ixia:ixiaappserver_add",
                                permissions=[],
                            ),
                        ),
                    ),
                ),
            ),
        ),
    ),
)
