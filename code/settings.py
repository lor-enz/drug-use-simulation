import drug as d


class Settings:
    def __init__(self):
        # How many cycles to look back to determine is the Agent is declared a regular drug user
        self.lookback_to_determine_regular_use = 8
        # How often in that time til they are declared a regular user
        self.threshold_to_determine_regular_use = 2

        # How many cycles to look back to determine is the Agent is declared addicted
        self.lookback_to_determine_addiction = 8
        # How often in that time til they are declared addicted
        self.threshold_to_determine_addiction = 4

        # Init Variables
        self.init_population_percentage_using = 0.10
        self.init_users_percentage_addicted = 0.50
        self.init_population_percentage_female = 0.496
        self.genetic_risk_factor_parameter=0.1
        self.addicted_parameter=1.5
        self.friends_influence_parameter=0.5

        # Runtime Variables
        self.rounds_in_year = 52
        self.dependence_potential_normalization = 4

        # drugs
        cannabis = d.Drug("cannabis", d.cannabis_addict_rate_f, d.cannabis_addict_rate_m,
                          d.cannabis_dependence_potential,
                          d.cannabis_mortality_rate)
        cocaine = d.Drug("cocaine", d.cocaine_addict_rate_f, d.cocaine_addict_rate_m, d.cocaine_dependence_potential,
                         d.cocaine_mortality_rate)
        amphetamines = d.Drug("amphetamines", d.amphetamines_addict_rate_f, d.amphetamines_addict_rate_m,
                              d.amphetamine_dependence_potential,
                              d.amphetamine_mortality_rate)
        opioid = d.Drug("opioid", d.opioid_addict_rate_f, d.opioid_addict_rate_m, d.opioid_dependence_potential,
                        d.opioid_mortality_rate)

        self.drugs = [cannabis, cocaine, amphetamines, opioid]

set = Settings()
# set.init_population_percentage_using = 0.05
# set.init_population_percentage_using = 0.03
