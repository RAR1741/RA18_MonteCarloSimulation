from Vault import Vault
from Robots import Robots
from Scale import Scale
from Switch import Switch
from Alliance import Alliance
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
        self.red_alliance  = Alliance(self, True)#self.red_alliance.points to edits
        self.blue_alliance = Alliance(self, False)
        self.alliances = [self.blue_alliance.robots, self.red_alliance.robots]
    def tick(self, time):
        print(f"Boost|Force|Lev : {self.red_vault.boost_cubes}|{self.red_vault.force_cubes}|{self.red_vault.lev_cubes}")
        print(f"My Red Cubes|Blue Cubes : {self.my_switch.red_cubes}|{self.my_switch.blue_cubes}")
        print(f"Their Red Cubes|Blue Cubes : {self.their_switch.red_cubes}|{self.their_switch.blue_cubes}")
        print(f"Red Scale Cubes|Blue Scale Cubes : {self.scale.red_cubes1}|{self.scale.blue_cubes1}")
        print(f"Red Points|Blue Points : {self.red_alliance.points}|{self.blue_alliance.points}")
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
            
    def my_switch_points(self, is_red_alliance):
        if is_red_alliance:
            self.my_switch.switch_tilt_state(is_red_alliance)
        else:
            self.their_switch.switch_tilt_state(is_red_alliance)

    def their_switch_points(self, is_red_alliance):
        if is_red_alliance:
            self.their_switch.switch_tilt_state(is_red_alliance)
        else:
            self.my_switch.switch_tilt_state(is_red_alliance)
    
    def scale_points(self, is_red_alliance):
        if self.scale.scale_tilt_state(is_red_alliance) == 1:
            self.red_alliance.points += 1
        elif self.scale.scale_tilt_state(is_red_alliance) == 2:
            self.blue_alliance.points += 1 
        else:
            pass          
    
    def checkIfWin(self):
        if self.red_alliance.points > self.blue_alliance.points:
            print(f"The Red Alliance won!")
        elif self.blue_alliance.points > self.red_alliance.points:
            print(f"The Blue Alliance won!")
        else:
            print("Its a tie!")
        


