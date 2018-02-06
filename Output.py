
class Output:
    def __init__(self):
        #robot skills
        self.red_one_skill = 0
        self.red_two_skill = 0
        self.red_three_skill = 0
        self.blue_one_skill = 0
        self.blue_two_skill = 0
        self.blue_three_skill = 0

        #endgame and autonomous ONLY
        self.num_crossed_baseline = 0
        self.red_num_climbed = 0
        self.blue_num_climbed = 0
        self.red_num_parked = 0
        self.blue_num_parked = 0

        #vault tracking
        self.auto_red_lev_cubes = 0
        self.auto_red_boost_cubes = 0
        self.auto_red_force_cubes = 0
        self.auto_red_overflow_cubes = 0 
        self.auto_blue_lev_cubes = 0
        self.auto_blue_boost_cubes = 0
        self.auto_blue_force_cubes = 0
        self.auto_blue_overflow_cubes = 0

        self.red_lev_cubes = 0
        self.blue_lev_cubes = 0
        self.red_boost_cubes = 0
        self.blue_boost_cubes = 0
        self.red_force_cubes = 0
        self.blue_force_cubes = 0
        self.red_overflow_cubes = 0
        self.blue_overflow_cubes = 0



        # time that each zone is controlled
        self.red_own_switch_control = 0
        self.red_opposite_switch_control = 0
        self.blue_own_switch_control = 0
        self.blue_opposite_switch_control = 0
        self.red_scale_control = 0
        self.blue_scale_control = 0

        self.auto_red_own_switch_control = 0
        self.auto_red_opposite_switch_control = 0
        self.auto_blue_own_switch_control = 0
        self.auto_blue_opposite_switch_control = 0
        self.auto_red_scale_control = 0
        self.auto_blue_scale_control = 0

        # TOTALS
        self.red_alliance_auto_total = 0
        self.blue_alliance_auto_total = 0
        self.red_alliance_total = 0
        self.blue_alliance_total = 0
        
        #number of cubes in each zone
        self.red_own_switch_cubes = 0
        self.red_opposite_switch_cubes = 0
        self.blue_own_switch_cubes = 0
        self.red_opposite_switch_cubes = 0
        self.red_scale_cubes = 0
        self.blue_scale_cubes = 0

        self.auto_red_own_switch_cubes = 0
        self.auto_red_opposite_switch_cubes = 0
        self.auto_blue_own_switch_cubes = 0
        self.auto_red_opposite_switch_cubes = 0
        self.auto_red_scale_cubes = 0
        self.auto_blue_scale_cubes = 0

    def final_print(self):
        print(f"{self.red_one_skill},{self.red_two_skill},{self.red_three_skill},{self.blue_one_skill},{self.blue_two_skill},{self.blue_three_skill}")
        print(f"{self.red_own_switch_control}, {self.red_opposite_switch_control}, {self.blue_own_switch_control}, {self.blue_opposite_switch_control}, {self.red_scale_control}, {self.blue_scale_control}")
        print(f"{self.red_lev_cubes}, {self.blue_lev_cubes}, {self.red_boost_cubes}, {self.blue_boost_cubes}, {self.red_force_cubes}, {self.blue_force_cubes}, {self.red_overflow_cubes}, {self.blue_overflow_cubes}")