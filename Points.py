from Switch import Switch
from Scale import Scale 
from Vault import Vault
class Points:
    def __init__(self, is_red_alliance):
        self.is_red_alliance = is_red_alliance
        self.points = 0
        self.scale_points = 0
        self.my_switch_points = 0
        self.their_switch_points = 0
