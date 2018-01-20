from Vault import Vault
from Robots import Robots
import random
import array

class Field:
    def __init__(self):
        print("init")
        # Game things
        self.red_vault = Vault(True)
        self.blue_vault = Vault(True)

        # Robots
        self.red1Robot = Robots(self, True, "R1", self.get_random_skill())
        self.alliances = [[],[self.red1Robot]]
        
    def tick(self, time):
        print(f"Red boost cubes: {self.red_vault.boost_cubes}")
        for alliance in self.alliances:
            for team in alliance:
                team.tick(time)

    def add_boost_cube(self, is_red_alliance):
        if is_red_alliance:
            self.red_vault.add_random_cube()
        else:
            self.blue_vault.add_random_cube()
            
    def get_random_skill(self):
        return random.randint(1, 10)