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
        self.force = False 
        self.force_counter = 0
        self.power_time = 0
        self.power_active = False
        self.can_use_power = False
        
        
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
    # $ is Blue Alliance Force
    def powerup(self, is_red_alliance):
        power_pick = random.randint(0,1)
        if self.can_use_power == True:
            self.power_time = 10
            if power_pick == 0 and self.boost_counter < 1 and self.power_active == False:
                    if self.power_time > 0:
                        self.power_active = True
                        if is_red_alliance:
                            self.field.queue.append(1)
                        else:
                            self.field.queue.append(3)
                    self.boost = False
                    self.power_active = False
                    self.boost_counter += 1
            elif power_pick == 1 and self.force_counter < 1 and self.power_active == False:
                    if self.power_time > 0:
                        self.power_active == True
                        if is_red_alliance:
                            self.field.queue.append(2)
                        else:
                            self.field.queue.append(4)
                    self.force = False
                    self.power_active = False
                    self.force_counter += 1


    def lev_check(self):
        if self.lev_cubes == 3 or self.lev_cubes == 3 :
            self.lev = True

    def power_tick(self, time):
        self.lev_check()
        if self.power_time > 0:
            self.power_time -= 1
        elif self.power_time == 0:
            if len(self.field.queue) > 0:
                self.field.queue.remove(self.field.queue[0])
            if random.randint(1,60) > 59:
                self.powerup(self.is_red_alliance)
        else:
            if random.randint(1,60) > 59:
                self.powerup(self.is_red_alliance)

