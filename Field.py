import random
import array
from Vault import Vault
from Robots import Robots
from Scale import Scale
from Switch import Switch
from Alliance import Alliance
from Points import Points
from Output import Output


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

        #output
        self.output = Output()
        self.red_own_switch_control = 0
        self.red_opposite_switch_control = 0
        self.blue_own_switch_control = 0
        self.blue_opposite_switch_control = 0
        self.red_scale_control = 0
        self.blue_scale_control = 0
        self.red_vault_cubes = 0
        self.blue_vault_cubes = 0
        self.red_baseline = 0
        self.blue_baseline = 0
        
        # Robots
        self.red_alliance  = Alliance(self, True)#self.red_alliance.points to edits
        self.blue_alliance = Alliance(self, False)
        self.alliances = [self.blue_alliance.robots, self.red_alliance.robots]
        self.set_output_skills()
    
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
        self.blue_vault.power_tick(time)

    def auto_tick(self, time):
        self.time = time
        for alliance in self.alliances:
            for team in alliance:
                team.tick(time)
        self.auto_my_switch_points()
        self.auto_their_switch_points()
        self.auto_scale_points()
    

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
            self.red_own_switch_control += 1
            if self.red_vault.boost and (self.red_vault.boost_cubes == 1 or self.red_vault.boost_cubes == 3):
                self.red_alliance.points += 2
            else:
                self.red_alliance.points += 1
        elif self.red_vault.force and (self.red_vault.force_cubes == 1 or self.red_vault.force_cubes == 3):
            self.red_own_switch_control += 1
            self.red_alliance.points += 1
        elif self.my_switch.blue_cubes > self.my_switch.red_cubes:
            self.blue_opposite_switch_control += 1       

    def their_switch_points(self):
        if self.their_switch.blue_cubes > self.their_switch.red_cubes:
            if self.blue_vault.boost and (self.blue_vault.boost_cubes == 1 or self.blue_vault.boost_cubes == 3):
                self.blue_alliance.points += 2
                self.blue_own_switch_control += 1
            else:
                self.blue_alliance.points += 1
                self.blue_own_switch_control += 1
        elif self.blue_vault. force and (self.blue_vault.force_cubes == 1 or self.blue_vault.force_cubes == 3):
            self.blue_alliance.points += 1
            self.blue_own_switch_control += 1
        elif self.their_switch.red_cubes > self.their_switch.blue_cubes:
            self.red_opposite_switch_control += 1
    
    def scale_points(self):
        if self.red_vault.force and (self.red_vault.force_cubes == 2 and self.red_vault.force_cubes == 3):
            self.red_alliance.points += 1
            self.red_scale_control += 1
        elif self.blue_vault.force and (self.blue_vault.force_cubes == 2 and self.blue_vault.force_cubes == 3):
            self.blue_alliance.points += 1
            self.blue_scale_control += 1
        elif self.scale.red_cubes1 > self.scale.blue_cubes1:
            if self.red_vault.boost and (self.red_vault.boost_cubes == 2 and self.red_vault.boost_cubes == 3):
                self.red_alliance.points += 2
                self.red_scale_control += 1
            else:
                self.red_alliance.points += 1
                self.red_scale_control += 1
        elif self.scale.blue_cubes1 > self.scale.red_cubes1:
            if self.blue_vault.boost and (self.blue_vault.boost_cubes == 2 and self.blue_vault.boost_cubes == 3):
                self.blue_alliance.points += 1
                self.blue_scale_control += 1
            else:
                self.red_alliance.points += 1
                self.blue_scale_control += 1
        
    def endgame_scoring(self):
        self.red_park_counter = 0
        self.red_climb_counter = 0
        self.blue_park_counter = 0
        self.blue_climb_counter = 0
        for alliance in self.alliances:
            for team in alliance:
                print(f"{team.name} {team.climb} {team.platform}")
                if team.climb == True and team.is_red_alliance:
                    self.red_alliance.points += 30
                    self.red_climb_counter += 1
                elif team.climb == True and team.is_red_alliance == False:
                    self.blue_alliance.points += 30
                    self.blue_climb_counter += 1
                elif team.platform == True and team.is_red_alliance:
                    self.red_alliance.points += 5
                    self.red_park_counter += 1
                elif team.platform == True and team.is_red_alliance == False:
                    self.blue_alliance.points += 5
                    self.blue_park_counter += 1
        if self.red_vault.lev and self.red_climb_counter < 3:
            if self.red_climb_counter + self.red_park_counter < 3:
                self.red_alliance.points += 30
            else:
                self.red_alliance.points += 25
        elif self.blue_vault.lev and self.blue_climb_counter < 3:
            if self.blue_climb_counter + self.blue_park_counter < 3:
                self.blue_alliance.points += 30
            else:
                self.blue_alliance.points += 25

    def auto_my_switch_points(self):
        if self.my_switch.red_cubes > self.my_switch.blue_cubes:
            self.red_alliance.points += 2
            self.red_own_switch_control += 1
        elif self.my_switch.blue_cubes > self.my_switch.red_cubes:
            self.blue_alliance.points += 2
            self.blue_opposite_switch_control += 1

    def auto_their_switch_points(self):
        if self.their_switch.red_cubes > self.their_switch.blue_cubes:
            self.red_alliance.points += 2
            self.red_opposite_switch_control += 1
        elif self.their_switch.blue_cubes > self.their_switch.red_cubes:
            self.blue_alliance.points += 2
            self.blue_own_switch_control += 1

    def auto_scale_points(self):
        if self.scale.red_cubes1 > self.scale.blue_cubes1:
            self.red_alliance.points += 2
            self.red_scale_control += 1
        elif self.scale.blue_cubes1 > self.scale.red_cubes1:
            self.blue_alliance.points += 2
            self.blue_scale_control += 1

    def baseline_points(self):
        for alliance in self.alliances:
            for team in alliance:
                if team.is_red_alliance and team.auto_run == True:
                    self.red_alliance.points += 5
                    self.red_baseline += 1
                elif team.is_red_alliance == False and team.auto_run == True:
                    self.blue_alliance.points += 5
                    self.blue_baseline += 1

    
    def power_queue(self):
        if self.queue[0] == 1:
            self.red_vault.boost == True
            self.red_vault.boost_used = self.time
            self.red_vault.boost_used_cubes = self.red_vault.boost_cubes
        if self.queue[0] == 2:
            self.red_vault.force == True
            self.red_vault.force_used = self.time
            self.red_vault.force_used_cubes = self.red_vault.force_cubes
        if self.queue[0] == 3:
            self.blue_vault.boost = True
            self.blue_vault.boost_used = self.time
            self.blue_vault.boost_used_cubes = self.blue_vault.boost_cubes
        if self.queue[0] == 4:
            self.blue_vault.force = True
            self.blue_vault.force_used = self.time
            self.blue_vault.force_used_cubes = self.blue_vault.force_cubes

        else:
            pass

#outputs
    def powerup_output(self):
        #When it was played
        #create a variable that is set equal to the time when powerup is used?
        #Number of cubes when it was played
        #Was lev used Y/N
         # - time 
        pass

    def set_output_skills(self):
        self.output.red_one_skill = self.red_alliance.robots[0].skillRating
        self.output.red_two_skill = self.red_alliance.robots[1].skillRating
        self.output.red_three_skill = self.red_alliance.robots[2].skillRating
        self.output.blue_one_skill = self.blue_alliance.robots[0].skillRating
        self.output.blue_two_skill = self.blue_alliance.robots[1].skillRating
        self.output.blue_three_skill = self.blue_alliance.robots[2].skillRating

    def time_controlled_output(self):
        self.output.red_own_switch_control = self.red_own_switch_control
        self.output.red_opposite_switch_control = self.red_opposite_switch_control
        self.output.blue_own_switch_control = self.blue_own_switch_control
        self.output.blue_opposite_switch_control = self.blue_opposite_switch_control
        self.output.red_scale_control = self.red_scale_control
        self.output.blue_scale_control = self.blue_scale_control
    
    def auto_time_controlled_output(self):
        self.auto_red_own_switch_control = self.red_own_switch_control
        self.auto_red_opposite_switch_control = self.red_opposite_switch_control
        self.auto_blue_own_switch_control = self.blue_own_switch_control
        self.auto_blue_opposite_switch_control = self.blue_opposite_switch_control
        self.auto_red_scale_control = self.red_scale_control
        self.auto_blue_scale_control = self.blue_scale_control         

    def vault_output(self):
       self.output.red_lev_cubes = self.red_vault.lev_cubes
       self.output.red_boost_cubes = self.red_vault.boost_cubes
       self.output.red_force_cubes = self.red_vault.lev_cubes
       self.output.red_overflow_cubes = self.red_vault.overflow_cubes

       self.output.blue_lev_cubes = self.blue_vault.lev_cubes
       self.output.blue_boost_cubes = self.blue_vault.boost_cubes
       self.output.blue_force_cubes = self.blue_vault.force_cubes
       self.output.blue_overflow_cubes = self.blue_vault.overflow_cubes

    def auto_vault_output(self):
       self.output.auto_red_lev_cubes = self.red_vault.lev_cubes
       self.output.auto_red_boost_cubes = self.red_vault.boost_cubes
       self.output.auto_red_force_cubes = self.red_vault.lev_cubes
       self.output.auto_red_overflow_cubes = self.red_vault.overflow_cubes

       self.output.auto_blue_lev_cubes = self.blue_vault.lev_cubes
       self.output.auto_blue_boost_cubes = self.blue_vault.boost_cubes
       self.output.auto_blue_force_cubes = self.blue_vault.force_cubes
       self.output.auto_blue_overflow_cubes = self.blue_vault.overflow_cubes
        
    def endgame_output(self):
        self.output.red_num_parked = self.red_park_counter
        self.output.red_num_climbed = self.red_climb_counter
        self.output.blue_num_climbed = self.blue_climb_counter
        self.output.blue_num_parked = self.blue_park_counter
        
    def total_points(self):
        self.output.red_alliance_total = self.red_alliance.points
        self.output.blue_alliance_total = self.blue_alliance.points

    def cube_tracking_output(self):
        self.output.red_own_switch_cubes = self.my_switch.red_cubes
        self.output.blue_own_switch_cubes = self.their_switch.blue_cubes
        self.output.red_opposite_switch_cubes = self.their_switch.red_cubes
        self.output.blue_opposite_switch_cubes =  self.my_switch.blue_cubes
        self.output.red_scale_cubes = self.scale.red_cubes1
        self.output.blue_scale_cubes = self.scale.blue_cubes1

    def auto_cube_tracking_output(self):
        self.output.auto_red_own_switch_cubes = self.my_switch.red_cubes
        self.output.auto_blue_own_switch_cubes = self.their_switch.blue_cubes
        self.output.auto_red_opposite_switch_cubes = self.their_switch.red_cubes
        self.output.auto_blue_opposite_switch_cubes =  self.my_switch.blue_cubes
        self.output.auto_red_scale_cubes = self.scale.red_cubes1
        self.output.auto_blue_scale_cubes = self.scale.blue_cubes1
        self.output.red_baseline = self.red_baseline
        self.output.blue_baseline = self.blue_baseline

   