from Robots import Robots
from Switch import Switch
from Scale import Scale
from Vault import Vault
import random
class Alliance():
    def __init__(self, field, is_red_alliance):
        self.points = 0
        self.robots = []
        self.is_red_alliance = is_red_alliance
        self.field = field
        self.make_alliance(3)
        self.parked = 0
        self.climbed = 0

    def get_random_skill(self):
        return random.randint(1, 10)

    def make_robot(self, num):
        prefix = "B"
        if self.is_red_alliance:
            prefix = "R"
        temp_robot = Robots(self.field, self.is_red_alliance,f"{prefix}{num}", self.get_random_skill())
        self.robots.append(temp_robot)

    def make_alliance(self, num_robots):
        for i in range(1, num_robots + 1, 1):
            self.make_robot(i)

    # add in a queuing to track powerup alliances
    def queue(self, power_active, is_red_alliance):
        if self.is_red_alliance and power_active:
            self.can_use_power = False
        elif self.is_red_alliance == False and power_active:
            self.can_use_power = False

    
    

