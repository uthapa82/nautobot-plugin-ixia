"""Nautobot Example DNS Manager Navigation."""
#-----------------------------
# __author__: Upendra Thapa
# __modified__:02/20/2023
# __version__ ="0.1.0"
# __status__ = "development"
#------------------------------

from nautobot.core.apps import NavMenuAddButton, NavMenuGroup, NavMenuItem, NavMenuImportButton, NavMenuTab

menu_items = (
    NavMenuTab(
        name="IXIA Chassis",
        groups=(
            NavMenuGroup(
                name="Ixia Chassis",
                weight=150,
                items=(
                    NavMenuItem(
                        link="plugins:nautobot_plugin_ixia:ixiarowmodel24_list",
                        name="Ixia Row 24",
                        permissions=[],
                        buttons=(
                            NavMenuAddButton(
                                link="plugins:nautobot_plugin_ixia:ixiarowmodel24_add",
                                permissions=[],
                            ),
                        ), 
                    ),
                    NavMenuItem(
                        link="plugins:nautobot_plugin_ixia:ixiarowmodel14_list",
                        name="Ixia Row 14",
                        permissions=[],
                        buttons=(
                            NavMenuAddButton(
                                link="plugins:nautobot_plugin_ixia:ixiarowmodel14_add",
                                permissions=[],
                            ),
                        ),
                    ),
                ),
            ),
        ),
    ),
)
   
