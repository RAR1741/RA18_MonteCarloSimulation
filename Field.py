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
        self.red_vault = Vault(True, self)
        self.blue_vault = Vault(False, self)
        self.my_switch = Switch(True)
        self.their_switch = Switch(False)
        self.scale = Scale(True)
        self.time = 0
        self.queue = []

       
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
        self.red_vault.power_tick(time)

    def auto_tick(self, time):
        self.time = time
        for alliance in self.alliances:
            for team in alliance:
                team.tick(time)
        self.auto_my_switch_points()
        self.auto_their_switch_points()
        self.auto_scale_points()
    #     self.time = time
    #     self.auto_my_switch_points()
    #     self.auto_their_switch_points()
    #     self.auto_scale_points()
    #     print(f"Red Alliance Score : {self.red_alliance.points}")
    #     print(f"Blue Alliance Score : {self.blue_alliance.points}")
    #     #need to add in platform for auto


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
        print(f"Red Alliance Score : {self.red_alliance.points}")
        print(f"Blue Alliance Score : {self.blue_alliance.points}")
        if self.red_alliance.points > self.blue_alliance.points:
            print(f"The Red Alliance won!")
        elif self.blue_alliance.points > self.red_alliance.points:
            print(f"The Blue Alliance won!")
        else:
            print("Its a tie!")
        
    def my_switch_points(self):
        if self.my_switch.red_cubes > self.my_switch.blue_cubes:
            if self.red_vault.boost and (self.red_vault.boost_cubes == 1 or self.red_vault.boost_cubes == 3):
                self.red_alliance.points += 2
            else:
                self.red_alliance.points += 1
        elif self.red_vault.force and (self.red_vault.force_cubes == 1 or self.red_vault.force_cubes == 3):
                self.red_alliance.points += 1        

    def their_switch_points(self):
        if self.their_switch.blue_cubes > self.their_switch.red_cubes:
            if self.blue_vault.boost and (self.blue_vault.boost_cubes == 1 or self.blue_vault.boost_cubes == 3):
                self.blue_alliance.points += 2
            else:
                self.blue_alliance.points += 1
        elif self.blue_vault. force and (self.blue_vault.force_cubes == 1 or self.blue_vault.force_cubes == 3):
            self.blue_alliance.points += 1 
    
    def scale_points(self):
        if self.red_vault.force and (self.red_vault.force_cubes == 2 and self.red_vault.force_cubes == 3):
            self.red_alliance.points += 1
        elif self.blue_vault.force and (self.blue_vault.force_cubes == 2 and self.blue_vault.force_cubes == 3):
            self.blue_alliance.points += 1
        elif self.scale.red_cubes1 > self.scale.blue_cubes1:
            if self.red_vault.boost and (self.red_vault.boost_cubes == 2 and self.red_vault.boost_cubes == 3):
                self.red_alliance.points += 2
            else:
                self.red_alliance.points += 1
        elif self.scale.blue_cubes1 > self.scale.red_cubes1:
            if self.blue_vault.boost and (self.blue_vault.boost_cubes == 2 and self.blue_vault.boost_cubes == 3):
                self.blue_alliance.points += 1
            else:
                self.red_alliance.points += 1
        
    def endgame_scoring(self):
        red_park_counter = 0
        red_climb_counter = 0
        blue_park_counter = 0
        blue_climb_counter = 0
        for alliance in self.alliances:
            for team in alliance:
                print(f"{team.name} {team.climb} {team.platform}")
                if team.climb == True and team.is_red_alliance:
                    self.red_alliance.points += 30
                    red_climb_counter += 1
                elif team.climb == True and team.is_red_alliance == False:
                    self.blue_alliance.points += 30
                    blue_climb_counter += 1
                elif team.platform == True and team.is_red_alliance:
                    self.red_alliance.points += 5
                    red_park_counter += 1
                elif team.platform == True and team.is_red_alliance == False:
                    self.blue_alliance.points += 5
                    blue_park_counter += 1
        if self.red_vault.lev and red_climb_counter < 3:
            if red_climb_counter + red_park_counter < 3:
                self.red_alliance.points += 30
            else:
                self.red_alliance.points += 25
        elif self.blue_vault.lev and blue_climb_counter < 3:
            if blue_climb_counter + blue_park_counter < 3:
                self.blue_alliance.points += 30
            else:
                self.blue_alliance.points += 25

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

    def baseline_points(self):
        for alliance in self.alliances:
            for team in alliance:
                if team.is_red_alliance and team.auto_run == True:
                    self.red_alliance.points += 5
                elif team.is_red_alliance == False and team.auto_run == True:
                    self.blue_alliance.points += 5

    
    def power_queue(self):
        if self.queue[0] == 1:
            self.red_vault.boost == True
            
        if self.queue[0] == 2:
            self.red_vault.force == True
        if self.queue[0] == 3:
            self.blue_vault.boost = True
        if self.queue[0] == 4:
            self.blue_vault.force = True
        else:
            pass

