import unittest


class TestSimAndEva(unittest.TestCase):

    def create_sim(self, how_many_agents):
        from simulation import Simulation
        from agent_factory import AgentFactory
        import country
        agents = AgentFactory(how_many_agents, country.germany).agents
        sim = Simulation(agents, label=f"{how_many_agents} Agents in germany")
        print("SETUP done")
        return sim

    def test_almost_nothing(self):
        from agent_factory import AgentFactory
        import country
        print("HI")
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

    def test_simulation(self):
        sim = self.create_sim(2000)
        sim.run(52)


if __name__ == "__main__":
    unittest.main()
