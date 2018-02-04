
class Output:
    def __init__(self):
        self.red_one_skill = 0
        self.red_two_skill = 0
        self.red_three_skill = 0
        self.blue_one_skill = 0
        self.blue_two_skill = 0
        self.blue_three_skill = 0

        self.red_own_switch_control = 0
        self.red_opposite_switch_control = 0
        self.blue_own_switch_control = 0
        self.blue_opposite_switch_control = 0
        self.red_scale_control = 0
        self.blue_scale_control = 0

    def final_print(self):
        print(f"{self.red_one_skill},{self.red_two_skill},{self.red_three_skill},{self.blue_one_skill},{self.blue_two_skill},{self.blue_three_skill}")
        print(f"{self.red_own_switch_control}, {self.red_opposite_switch_control}, {self.blue_own_switch_control}, {self.blue_opposite_switch_control}, {self.red_scale_control}, {self.blue_scale_control}")
