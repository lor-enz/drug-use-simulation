import random ,copy
import settings
import country
import simulation
from enums import Gender
import agent
import numpy as np


class AgentFactory():

    def __init__(self, how_many_agents, country):
        self.agents = []
        self.country = country
        self.how_many_agents = how_many_agents
        self.create_agents()
        print("AgentFactory created agents")

    def create_agents(self):
        while len(self.agents) < self.how_many_agents:
            self.agents.append(self.create_random_agent())

    def create_random_agent(self):
        gender = Gender.Female if (random.random() <= settings.set.init_population_percentage_female) else Gender.Male
        addicted_amphetamine = False
        addicted_cannabis = False
        addicted_cocaine = False
        addicted_opioid = False
        if Gender.Female:
            addicted_amphetamin = True if (
                    random.random() <= self.country.amphetamines_addict_rate_f) else False
            addicted_cannabis = True if (
                    random.random() <= self.country.cannabis_addict_rate_f) else False
            addicted_cocaine = True if (
                    random.random() <= self.country.cocaine_addict_rate_f) else False
            addicted_opioid = True if (
                    random.random() <= self.country.opioids_addict_rate_f) else False
        else:
            addicted_amphetamin = True if (
                    random.random() <= self.country.amphetamines_addict_rate_m) else False
            addicted_cannabis = True if (
                    random.random() <= self.country.cannabis_addict_rate_m) else False
            addicted_cocaine = True if (
                    random.random() <= self.country.cocaine_addict_rate_m) else False
            addicted_opioid = True if (
                    random.random() <= self.country.opioids_addict_rate_m) else False
        addicted = {"amphetamines":addicted_amphetamin,"cannabis":addicted_cannabis,"cocaine":addicted_cocaine,"opioid":addicted_opioid}
        #using = addicted when init
        using = copy.deepcopy(addicted)
        genetic_risk_factor = np.random.normal(0, 0.1, 1)*settings.set.genetic_risk_factor_parameter
        new_agent = agent.Agent(gender, using, addicted, genetic_risk_factor[0],self.country)
        new_agent.usage_history = self.create_usage_history(new_agent.is_regular_user, new_agent.addicted)
        return new_agent

    def create_usage_history(self, is_regular_user, is_addicted):
        usage_history = {"amphetamines": [], "cannabis": [], "cocaine": [], "opioid": []}
        for substance in settings.set.drugs:
            range_reg = settings.set.lookback_to_determine_regular_use
            thres_reg = settings.set.threshold_to_determine_regular_use
            range_add = settings.set.lookback_to_determine_addiction
            thres_add = settings.set.threshold_to_determine_addiction

            is_regular = is_regular_user[substance.name]
            if is_regular and not is_addicted[substance.name]:
                usage_history[substance.name] = random.sample(range(-range_reg, -1), int(thres_reg * random.uniform(1, 1.5)))
            if is_addicted[substance.name]:
                usage_history[substance.name] = random.sample(range(-range_add, -1), int(thres_add * random.uniform(1, 1.25)))

            usage_history[substance.name].sort()
        # print(f"HISTORY for reg: {is_regular_user} add: {is_addicted}: {len(usage_history)}    {usage_history}")
        return usage_history

