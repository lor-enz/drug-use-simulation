import unittest


class TestSimAndEva(unittest.TestCase):

    def create_sim(self, how_many_agents):
        from simulation import Simulation
        from agent_factory import AgentFactory
        from country import Country
        germany = Country("germany")
        agents = AgentFactory(how_many_agents,germany).agents
        sim = Simulation(agents, label=f"{how_many_agents} Agents in germany")
        print("SETUP done")
        return sim

    def test_almost_nothing(self):
        from agent_factory import AgentFactory
        from country import Country
        germany = Country("germany")
        print("HI")
        agents = AgentFactory(10,germany).agents

    def test_basics(self):
        from agent_factory import AgentFactory
        from country import Country
        germany = Country("germany")
        agents = AgentFactory(10, germany).agents
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
