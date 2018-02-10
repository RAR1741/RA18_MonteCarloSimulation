import random

class Vault:
    def __init__(self, is_red_alliance, field):
        self.boost_cubes = 0
        self.force_cubes = 0
        self.lev_cubes = 0
        self.overflow_cubes = 0
        self.total_cubes = self.boost_cubes + self.force_cubes + self.lev_cubes + self.overflow_cubes

        self.is_red_alliance = is_red_alliance
        self.field = field
         # for powerups
        self.lev = False
        self.lev_counter = 0
        self.boost = False
        self.boost_counter = 0
        self.can_use_boost = True
        self.force = False 
        self.force_counter = 0
        self.can_use_force = True
        self.power_time = 0
        self.power_active = False
        self.can_use_power = False
        
        #for outputs
        self.force_used = 0
        self.boost_used = 0
        self.force_used_cubes = 0
        self.boost_used_cubes = 0
        self.lev_used = 0
        #used the below variable to make sure the variable was set to time ony once
        self.lev_method_used = 0


        
    def add_random_cube(self):
        if self.boost_cubes == 3 and self.force_cubes == 3 and self.lev_cubes == 3:
            self.overflow_cubes += 1
        else:
            random_pick = random.randint(0, 2)
            if random_pick == 0:
                if self.boost_cubes < 3:
                    self.boost_cubes += 1
                else:
                    self.add_random_cube()
            if random_pick == 1:
                if self.force_cubes < 3:
                    self.force_cubes += 1
                else:
                    self.add_random_cube()
            if random_pick == 2:
                if self.lev_cubes < 3:
                    self.lev_cubes += 1
                else:
                    self.add_random_cube()


    # 1 is Red Alliance Boost
    # 2 is Red Alliance Force
    # 3 is Blue Alliance Boost
    # 4 is Blue Alliance Force
    def powerup(self):
        power_pick = random.randint(0,1)
        self.power_time = 10
        if power_pick == 0 and self.boost_counter < 1:
            if self.power_time > 0:
                self.power_active = True
                if self.is_red_alliance:
                    if self.can_use_boost:
                        self.field.queue.append(1)
                else:
                    if self.can_use_boost:
                        self.field.queue.append(3)
            self.boost = False
            self.boost_counter += 1
        elif power_pick == 1 and self.force_counter < 1:
            if self.power_time > 0:
                self.power_active == True
                if self.is_red_alliance:
                    if self.can_use_force:
                        self.field.queue.append(2)
                else:
                    if self.can_use_force:
                        self.field.queue.append(4)
            self.force = False
            self.force_counter += 1


    def lev_check(self):
        if self.lev_cubes == 3 or self.lev_cubes == 3 :
            self.lev = True

    # def power_tick(self, time):
    #     if self.power_time > 0:
    #         self.power_time -= 1
    #     elif self.power_time == 0:
    #         if len(self.field.queue) > 0:
    #             self.field.queue.remove(self.field.queue[0])
    #         if random.randin t(1,60) > 59:
    #             self.powerup(self.is_red_alliance)
    #     else:
    #         if random.randint(1,60) > 59:
    #             self.powerup(self.is_red_alliance)

