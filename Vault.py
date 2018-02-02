import random
class Vault:
    def __init__(self, is_red_alliance):
        self.boost_cubes = 0
        self.force_cubes = 0
        self.lev_cubes = 0
        self.overflow_cubes = 0
        self.is_red_alliance = is_red_alliance
        self.lev = False
        self.lev_counter = 0
        self.boost = False
        self.boost_counter = 0
        self.force = False 
        self.force_counter = 0
        self.power_time = 0
        self.power_active = False
        
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

    def tick(self, time):
        self.lev_check()
        if self.power_time > 0:
            self.power_time -= 1
        else:
            if random.randint(1,60) > 59:
                self.powerup()

    def lev_check(self):
        if self.lev_cubes == 3:
            self.lev = True

    def powerup(self):
        power_pick = random.randint(0,1)
        self.power_time = 10
        if power_pick == 0 and self.boost_counter < 1 and self.power_active == False:
                if self.power_time > 0:
                    self.power_active = True
                    self.boost = True
                self.boost = False
                self.power_active = False
        elif power_pick == 1 and self.force_counter < 1 and self.power_active == False:
                if self.power_time > 0:
                    self.force = True
                    self.power_active == True
                self.force = False
                self.power_active = False

