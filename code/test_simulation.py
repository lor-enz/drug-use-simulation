import unittest


class TestSimAndEva(unittest.TestCase):

    def create_sim(self, how_many_agents, country, label):
        from simulation import Simulation
        from agent_factory import AgentFactory
        agents = AgentFactory(how_many_agents, country).agents
        sim = Simulation(agents, label=f"{how_many_agents} Agents in germany")
        return sim

    def test_almost_nothing(self):
        from agent_factory import AgentFactory
        import country
        agents = AgentFactory(10, country.germany).agents

    def test_basics(self):
        from agent_factory import AgentFactory
        import country
        agents = AgentFactory(10, country.germany).agents
        agents[0].alive = False
        import evaluation
        result = evaluation.evaluate(agents)
        print(result)
        self.assertEqual(result['alive'], 9)
        self.assertEqual(result['dead'], 1)

    def test_simulation_all_countries(self):
        from country import all_country_dicts, Country
        from simulation import Simulation
        from agent_factory import AgentFactory
        # 20 000 for germany, portugal, italy takes 15 minuten on Lorenz' machine
        number_of_agents = 2_000
        sims = []
        for country_dict in all_country_dicts:
            country = Country(country_dict)
            agents = AgentFactory(number_of_agents, country).agents
            sim = Simulation(agents, label=f"{country.name} with {number_of_agents} Agents")
            sims.append(sim)
        # Maybe parallelize this
        for sim in sims:
            sim.run(52)

    def test_small_simulation_two_countries(self):
        from country import all_country_dicts, Country
        from simulation import Simulation
        from agent_factory import AgentFactory
        # 20 000 for germany, portugal, italy takes 15 minuten on Lorenz' machine
        number_of_agents = 2000
        sims = []
        for country_dict in all_country_dicts[:2]:
            country = Country(country_dict)
            agents = AgentFactory(number_of_agents, country).agents
            sim = Simulation(agents, label=f"{country.name} with {number_of_agents} Agents")
            sims.append(sim)
        # Maybe parallelize this
        for sim in sims:
            sim.run(6)

    def test_all_200000_agents(self):
        from country import all_country_dicts, Country
        from simulation import Simulation
        from agent_factory import AgentFactory
        number_of_agents = 200000
        sims = []
        for country_dict in all_country_dicts[0:5]:
            country = Country(country_dict)
            agents = AgentFactory(number_of_agents, country).agents
            sim = Simulation(agents, label=f"{country.name} with {number_of_agents} Agents")
            sims.append(sim)
        # Maybe parallelize this
        for sim in sims:
            sim.run(52)

    def test_kaleido(self):
        import plotly.express as px
        import numpy as np

        # RGB Data as numpy array
        img_rgb = np.array([[[255, 0, 0], [0, 255, 0], [0, 0, 255]], ], dtype=np.uint8)

        fig = px.imshow(img_rgb)

        fig.write_image('fig.png', engine='kaleido')

if __name__ == "__main__":
    unittest.main()
