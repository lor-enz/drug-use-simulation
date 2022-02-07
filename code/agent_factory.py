from random import random, choice
import stuff
from stuff import Gender
from agent import Agent
import numpy as np


class AgentFactory():

    def __init__(self, how_many_agents):
        self.agents = []
        self.how_many_agents = how_many_agents
        self.create_agents()

    def create_agents(self):
        while len(self.agents) < self.how_many_agents:
            self.agents.append(self.create_random_agent())

    def create_random_agent(self):
        gender = stuff.Gender.Female if (random() <= stuff.init_population_percentage_female) else stuff.Gender.Male
        using = True if (random() <= stuff.init_population_percentage_using) else False
        addicted = True if (
                    random() <= stuff.init_population_percentage_using * stuff.init_users_percentage_addicted) else False
        genetic_risk_factor = np.random.normal(0, 0.1, 1)
        return Agent(gender, using, addicted,genetic_risk_factor[0])

