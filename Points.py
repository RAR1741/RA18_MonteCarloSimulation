from Switch import Switch
from Scale import Scale 
from Vault import Vault
class Points:
    def __init__(self, is_red_alliance):
        self.is_red_alliance = is_red_alliance
        self.points = 0
        self.total_scale_points = 0
        self.red_switch_points = 0
        self.blue_switch_points = 0
    
    