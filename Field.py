from Vault import Vault
from Robots import Robots
from Scale import Scale
from Switch import Switch
import random
import array

class Field:
    def __init__(self):
        print("init")
        # Game things
        self.red_vault = Vault(True)
        self.blue_vault = Vault(False)
        self.my_switch = Switch(True)
        self.their_switch = Switch(False)
        self.scale = Scale(True)

        # Robots
        self.red1Robot = Robots(self, True, "R1", self.get_random_skill())
        self.red2Robot = Robots(self, True, "R2", self.get_random_skill())
        self.red3Robot = Robots(self, True, "R3", self.get_random_skill())
        red_alliance  = [self.red1Robot, self.red2Robot, self.red3Robot]
        self.blue1Robot = Robots(self, False, "B1", self.get_random_skill())
        self.blue2Robot = Robots(self, False, "B2", self.get_random_skill())
        self.blue3Robot = Robots(self, False, "B3", self.get_random_skill())
        blue_alliance = [self.blue1Robot, self.blue2Robot, self.blue3Robot]
        self.alliances = [blue_alliance, red_alliance]
    def tick(self, time):
        print(f"Boost|Force|Lev : {self.red_vault.boost_cubes}|{self.red_vault.force_cubes}|{self.red_vault.lev_cubes}")
        print(f"My Red Cubes|Blue Cubes : {self.my_switch.red_cubes}|{self.my_switch.blue_cubes}")
        print(f"Their Red Cubes|Blue Cubes : {self.their_switch.red_cubes}|{self.their_switch.blue_cubes}")
        print(f"Red Scale Cubes|Blue Scale Cubes : {self.scale.red_cubes1}|{self.scale.blue_cubes1}")
        for alliance in self.alliances:
            for team in alliance:
                team.tick(time)

    def add_random_vault_cube(self, is_red_alliance):
        if is_red_alliance:
            self.red_vault.add_random_cube()
        else:
            self.blue_vault.add_random_cube()
    
    def add_my_switch_cube(self, is_red_alliance):
        if is_red_alliance:
            self.my_switch.add_switch_cube(is_red_alliance)
        else:
            self.their_switch.add_switch_cube(is_red_alliance)

    def add_their_switch_cube(self, is_red_alliance):
        if is_red_alliance:
            self.their_switch.add_switch_cube(is_red_alliance)
        else:
            self.my_switch.add_switch_cube(is_red_alliance)
    
    def add_scale_cube(self, is_red_alliance):
        self.scale.add_scale_cube(is_red_alliance)
            
    def get_random_skill(self):
        return random.randint(0, 3)