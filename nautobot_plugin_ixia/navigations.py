"""Nautobot Ixia Plugin"""
#--------------------------------
# __author__: Upendra Thapa
# __modified__:02/20/2023
# __version__ ="0.1.0"
# __status__ = "development"
# __credits__ = "Network To Code"
#---------------------------------

from nautobot.core.apps import NavMenuAddButton, NavMenuGroup, NavMenuItem, NavMenuImportButton, NavMenuTab

menu_items = (
    NavMenuTab(
        name="IXIA Chassis",
        groups=(
            NavMenuGroup(
                name="Ixia Chassis",
                weight=100,
                items=(
                    NavMenuItem(
                        link="plugins:nautobot_plugin_ixia:ixiarow24_list",
                        name="Ixia Row 24",
                        weight=100,
                        permissions=["nautobot_plugin_ixia.view_ixiarow24"],
                        buttons=(
                            NavMenuAddButton(
                                link="plugins:nautobot_plugin_ixia:ixiarow24_add",
                                permissions=["nautobot_plugin_ixia.add_ixiarow24"],
                            ),
                        ), 
                    ),
                    NavMenuItem(
                        link="plugins:nautobot_plugin_ixia:ixiarow14_list",
                        name="Ixia Row 14",
                        weight=200,
                        permissions=["nautobot_plugin_ixia.view_ixiarow14"],
                        buttons=(
                            NavMenuAddButton(
                                link="plugins:nautobot_plugin_ixia:ixiarow14_add",
                                permissions=["nautobot_plugin_ixia.add_ixiarow24"],
                            ),
                        ),
                    ),
                    NavMenuItem(
                        link="plugins:nautobot_plugin_ixia:ixiaappserver_list",
                        name="Ixia App Server",
                        weight=300,
                        permissions=["nautobot_plugin_ixia:view_ixiaappserver"],
                        buttons=(
                            NavMenuAddButton(
                                link="plugins:nautobot_plugin_ixia:ixiaappserver_add",
                                permissions=["nautobot_plugin_ixia:add_ixiaappserver"],
                            ),
                        ),
                    ),
                    
                ),
            ),
        ),
    ),
)
   
