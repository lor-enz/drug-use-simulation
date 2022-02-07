

class Settings:
    def __init__(self):

        # How many cycles to look back to determine is the Agent is declared a regular drug user
        self.lookback_to_determine_regular_use = 20
        # How often in that time til they are declared a regular user
        self.threshold_to_determine_regular_use = 6

        # How many cycles to look back to determine is the Agent is declared addicted
        self.lookback_to_determine_addiction = 30
        # How often in that time til they are declared addicted
        self.threshold_to_determine_addiction = 20


        # Init Variables
        self.init_population_percentage_using = 0.10
        self.init_users_percentage_addicted = 0.50
        self.init_population_percentage_female = 0.496

set = Settings()
#set.init_population_percentage_using = 0.05
#set.init_population_percentage_using = 0.03
