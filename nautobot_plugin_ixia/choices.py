"""choices.py"""
# ---------------------------------
# __author__: Upendra Thapa
# __modified__:02/24/2023
# __version__ ="0.1.0"
# __status__ = "development"
# __credits__ = "Network To Code"
# ----------------------------------

from nautobot.utilities.choices import ChoiceSet

class SpeedChoices(ChoiceSet):

    # speed drop down
    CHOICES = (
        ("1G", "1G"),
        ("10G", "10G"),
        ("25G", "25G"),
        ("100G", "100G"),
    )
