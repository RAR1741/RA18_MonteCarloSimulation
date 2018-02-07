
class Output:
    def __init__(self):
        # TOTALS
        self.red_alliance_total = 0
        self.blue_alliance_total = 0

        #robot skills
        self.red_one_skill = 0
        self.red_two_skill = 0
        self.red_three_skill = 0
        self.blue_one_skill = 0
        self.blue_two_skill = 0
        self.blue_three_skill = 0

        # Autonomous
        # - Baseline
        self.red_baseline = 0
        self.blue_baseline = 0
        # - Vault
        self.auto_red_lev_cubes = 0
        self.auto_red_boost_cubes = 0
        self.auto_red_force_cubes = 0
        self.auto_red_overflow_cubes = 0 
        self.auto_blue_lev_cubes = 0
        self.auto_blue_boost_cubes = 0
        self.auto_blue_force_cubes = 0
        self.auto_blue_overflow_cubes = 0
        # - Switch/scale time
        self.auto_red_own_switch_control = 0
        self.auto_red_opposite_switch_control = 0
        self.auto_blue_own_switch_control = 0
        self.auto_blue_opposite_switch_control = 0
        self.auto_red_scale_control = 0
        self.auto_blue_scale_control = 0
        # - Switch/scale cubes
        self.auto_red_own_switch_cubes = 0
        self.auto_red_opposite_switch_cubes = 0
        self.auto_blue_own_switch_cubes = 0
        self.auto_red_opposite_switch_cubes = 0
        self.auto_red_scale_cubes = 0
        self.auto_blue_scale_cubes = 0
        # - Auto end
        self.red_alliance_auto_total = 0
        self.blue_alliance_auto_total = 0

        # Endgame
        # - Challenges
        self.red_num_climbed = 0
        self.blue_num_climbed = 0
        self.red_num_parked = 0
        self.blue_num_parked = 0
        # - Vault cubes
        self.red_lev_cubes = 0
        self.blue_lev_cubes = 0
        self.red_boost_cubes = 0
        self.blue_boost_cubes = 0
        self.red_force_cubes = 0
        self.blue_force_cubes = 0
        self.red_overflow_cubes = 0
        self.blue_overflow_cubes = 0
        # - Powerups Red
        self.red_boost_time = 0
        self.red_force_time = 0
        self.red_boost_cubes_used = 0
        self.red_force_cubes_used = 0
        self.red_lev_time = 0
        self.red_lev_used = False
        # - Powerups Blue
        self.blue_boost_time = 0
        self.blue_force_time = 0
        self.blue_boost_cubes_used = 0
        self.blue_force_cubes_used = 0
        self.blue_lev_time = 0
        self.blue_lev_used = False

        # time that each zone is controlled
        self.red_own_switch_control = 0
        self.red_opposite_switch_control = 0
        self.blue_own_switch_control = 0
        self.blue_opposite_switch_control = 0
        self.red_scale_control = 0
        self.blue_scale_control = 0
        
        #number of cubes in each zone
        self.red_own_switch_cubes = 0
        self.red_opposite_switch_cubes = 0
        self.blue_own_switch_cubes = 0
        self.red_opposite_switch_cubes = 0
        self.red_scale_cubes = 0
        self.blue_scale_cubes = 0

    def final_print(self):
        print(f"{self.red_one_skill},{self.red_two_skill},{self.red_three_skill},{self.blue_one_skill},{self.blue_two_skill},{self.blue_three_skill}")
        print(f"{self.red_own_switch_control}, {self.red_opposite_switch_control}, {self.blue_own_switch_control}, {self.blue_opposite_switch_control}, {self.red_scale_control}, {self.blue_scale_control}")
        print(f"{self.red_lev_cubes}, {self.blue_lev_cubes}, {self.red_boost_cubes}, {self.blue_boost_cubes}, {self.red_force_cubes}, {self.blue_force_cubes}, {self.red_overflow_cubes}, {self.blue_overflow_cubes}")

    def write_file(self):
        # red_alliance_total,blue_alliance_total,red_one_skill,red_two_skill,red_three_skill,blue_one_skill,blue_two_skill,blue_three_skill,red_baseline,blue_baseline,auto_red_lev_cubes,auto_red_boost_cubes,auto_red_force_cubes,auto_red_overflow_cubes,auto_blue_lev_cubes,auto_blue_boost_cubes,auto_blue_force_cubes,auto_blue_overflow_cubes,auto_red_own_switch_control,auto_red_opposite_switch_control,auto_blue_own_switch_control,auto_blue_opposite_switch_control,auto_red_scale_control,auto_blue_scale_control,auto_red_own_switch_cubes,auto_red_opposite_switch_cubes,auto_blue_own_switch_cubes,auto_red_opposite_switch_cubes,auto_red_scale_cubes,auto_blue_scale_cubes,red_alliance_auto_total,blue_alliance_auto_total,red_num_climbed,blue_num_climbed,red_num_parked,blue_num_parked,red_lev_cubes,blue_lev_cubes,red_boost_cubes,blue_boost_cubes,red_force_cubes,blue_force_cubes,red_overflow_cubes,blue_overflow_cubes,red_boost_time,red_force_time,red_boost_cubes_used,red_force_cubes_used,red_lev_time,red_lev_used,blue_boost_time,blue_force_time,blue_boost_cubes_used,blue_force_cubes_used,blue_lev_time,blue_lev_used,red_own_switch_control,red_opposite_switch_control,blue_own_switch_control,blue_opposite_switch_control,red_scale_control,blue_scale_control,red_own_switch_cubes,red_opposite_switch_cubes,blue_own_switch_cubes,red_opposite_switch_cubes,red_scale_cubes,blue_scale_cubes
        with open(f'output/output.csv', 'a') as file:
            file.write(f"{self.red_baseline},{self.blue_baseline}")
            # file.write(f"{self.red_alliance_total},{self.blue_alliance_total},{self.red_one_skill},{self.red_two_skill},{self.red_three_skill},{self.blue_one_skill},{self.blue_two_skill},{self.blue_three_skill},{self.red_baseline},{self.blue_baseline},{self.auto_red_lev_cubes},{self.auto_red_boost_cubes},{self.auto_red_force_cubes},{self.auto_red_overflow_cubes},{self.auto_blue_lev_cubes},{self.auto_blue_boost_cubes},{self.auto_blue_force_cubes},{self.auto_blue_overflow_cubes},{self.auto_red_own_switch_control},{self.auto_red_opposite_switch_control},{self.auto_blue_own_switch_control},{self.auto_blue_opposite_switch_control},{self.auto_red_scale_control},{self.auto_blue_scale_control},{self.auto_red_own_switch_cubes},{self.auto_red_opposite_switch_cubes},{self.auto_blue_own_switch_cubes},{self.auto_red_opposite_switch_cubes},{self.auto_red_scale_cubes},{self.auto_blue_scale_cubes},{self.red_alliance_auto_total},{self.blue_alliance_auto_total},{self.red_num_climbed},{self.blue_num_climbed},{self.red_num_parked},{self.blue_num_parked},{self.red_lev_cubes},{self.blue_lev_cubes},{self.red_boost_cubes},{self.blue_boost_cubes},{self.red_force_cubes},{self.blue_force_cubes},{self.red_overflow_cubes},{self.blue_overflow_cubes},{self.red_boost_time},{self.red_force_time},{self.red_boost_cubes_used},{self.red_force_cubes_used},{self.red_lev_time},{self.red_lev_used},{self.blue_boost_time},{self.blue_force_time},{self.blue_boost_cubes_used},{self.blue_force_cubes_used},{self.blue_lev_time},{self.blue_lev_used},{self.red_own_switch_control},{self.red_opposite_switch_control},{self.blue_own_switch_control},{self.blue_opposite_switch_control},{self.red_scale_control},{self.blue_scale_control},{self.red_own_switch_cubes},{self.red_opposite_switch_cubes},{self.blue_own_switch_cubes},{self.red_opposite_switch_cubes},{self.red_scale_cubes},{self.blue_scale_cubes}")
            file.write("\n")