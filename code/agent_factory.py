import random
import settings
from enums import Gender
import agent
import numpy as np


class AgentFactory():

    def __init__(self, how_many_agents):
        self.agents = []
        self.how_many_agents = how_many_agents
        #self.create_agents()

    def create_agents(self):
        while len(self.agents) < self.how_many_agents:
            self.agents.append(self.create_random_agent())

    def create_random_agent(self):
        gender = Gender.Female if (random() <= settings.set.init_population_percentage_female) else Gender.Male
        using = True if (random() <= settings.set.init_population_percentage_using) else False
        addicted = True if (
                    random() <= settings.set.init_population_percentage_using * settings.set.init_users_percentage_addicted) else False
        genetic_risk_factor = np.random.normal(0, 0.1, 1)
        new_agent = agent.Agent(gender, using, addicted, genetic_risk_factor[0])
        new_agent.usage_history = self.create_usage_history(new_agent.is_regular_user, new_agent.addicted)
        return new_agent

    def create_usage_history(self, is_regular_user, is_addicted):
        range_reg = settings.set.lookback_to_determine_regular_use
        thres_reg = settings.set.threshold_to_determine_regular_use
        range_add = settings.set.lookback_to_determine_addiction
        thres_add = settings.set.threshold_to_determine_addiction

        usage_history = []

        if is_regular_user and not is_addicted:
            usage_history = random.sample(range(-range_reg, -1), int(thres_reg * random.uniform(1, 1.5)))
        if is_addicted:
            usage_history = random.sample(range(-range_add, -1), int(thres_add * random.uniform(1, 1.25)))

        usage_history.sort()
        print(f"HISTORY for reg: {is_regular_user} add: {is_addicted}: {len(usage_history)}    {usage_history}")
        return usage_history

