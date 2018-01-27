import random
import array
from Vault import Vault
from Robots import Robots
from Scale import Scale
from Switch import Switch
from Alliance import Alliance
from Points import Points


class Field:
    def __init__(self):
        print("init")
        # Game things
        self.red_vault = Vault(True)
        self.blue_vault = Vault(False)
        self.my_switch = Switch(True)
        self.their_switch = Switch(False)
        self.scale = Scale(True)
        self.time = 0

        # Robots
        self.red_alliance  = Alliance(self, True)#self.red_alliance.points to edits
        self.blue_alliance = Alliance(self, False)
        self.alliances = [self.blue_alliance.robots, self.red_alliance.robots]
    def tick(self, time):
        self.time = time
        print(f"Boost|Force|Lev : {self.red_vault.boost_cubes}|{self.red_vault.force_cubes}|{self.red_vault.lev_cubes}")
        print(f"My Red Cubes|Blue Cubes : {self.my_switch.red_cubes}|{self.my_switch.blue_cubes}")
        print(f"Their Red Cubes|Blue Cubes : {self.their_switch.red_cubes}|{self.their_switch.blue_cubes}")
        print(f"Red Scale Cubes|Blue Scale Cubes : {self.scale.red_cubes1}|{self.scale.blue_cubes1}")
        for alliance in self.alliances:
            for team in alliance:
                team.tick(time)
        self.my_switch_points()
        self.their_switch_points()
        self.scale_points()
        print(f"Red Alliance Score : {self.red_alliance.points}")
        print(f"Blue Alliance Score : {self.blue_alliance.points}")

    def endgame_tick(self, time):
        self.time = time
        print(f"Red Robots CLimbed|Blue Robots Climbed : {self.red_alliance.climbed} {self.blue_alliance.climbed}")
        print(f"Red Robots Parked|BLue Robots Parked : {self.red_alliance.parked} {self.blue_alliance.parked}")
        self.endgame_points()

    def auto_tick(self, time):
        self.time = time
        self.auto_my_switch_points()
        self.auto_their_switch_points()
        self.auto_scale_points()
        print(f"Red Alliance Score : {self.red_alliance.points}")
        print(f"Blue Alliance Score : {self.blue_alliance.points}")
        #need to ad in platform for auto




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
    
    def checkIfWin(self):
        if self.red_alliance.points > self.blue_alliance.points:
            print(f"The Red Alliance won!")
        elif self.blue_alliance.points > self.red_alliance.points:
            print(f"The Blue Alliance won!")
        else:
            print("Its a tie!")
        
    def my_switch_points(self):
        if self.my_switch.red_cubes > self.my_switch.blue_cubes:
            self.red_alliance.points += 1
        elif self.my_switch.blue_cubes > self.my_switch.red_cubes:
            self.blue_alliance.points += 1

    def their_switch_points(self):
        if self.their_switch.red_cubes > self.their_switch.blue_cubes:
            self.red_alliance.points += 1
        elif self.their_switch.blue_cubes > self.their_switch.red_cubes:
            self.blue_alliance.points += 1
    
    def scale_points(self):
        if self.scale.red_cubes1 > self.scale.blue_cubes1:
            self.red_alliance.points += 1
        elif self.scale.blue_cubes1 > self.scale.red_cubes1:
            self.blue_alliance.points += 1
    
    def endgame_points(self):
        #create loops for allliance add 30 of 5 depending on what is true
        for alliance in self.alliances:
            for x in range(0,2,1):
                self.red_alliance.points += (self.red_alliance.robots[x].climb * 30) + (self.red_alliance.robots[x].platform * 5)
                self.blue_alliance.points += (self.blue_alliance.robots[x].climb * 30) + (self.blue_alliance.robots[x].platform * 5)

    def auto_my_switch_points(self):
        if self.my_switch.red_cubes > self.my_switch.blue_cubes:
            self.red_alliance.points += 2
        elif self.my_switch.blue_cubes > self.my_switch.red_cubes:
            self.blue_alliance.points += 2

    def auto_their_switch_points(self):
        if self.their_switch.red_cubes > self.their_switch.blue_cubes:
            self.red_alliance.points += 2
        elif self.their_switch.blue_cubes > self.their_switch.red_cubes:
            self.blue_alliance.points += 2

    def auto_scale_points(self):
        if self.scale.red_cubes1 > self.scale.blue_cubes1:
            self.red_alliance.points += 2
        elif self.scale.blue_cubes1 > self.scale.red_cubes1:
            self.blue_alliance.points += 2


    