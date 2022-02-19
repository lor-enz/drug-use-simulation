import unittest


class TestSimAndEva(unittest.TestCase):

    def create_sim(self, how_many_agents):
        from simulation import Simulation
        from agent_factory import AgentFactory
        from country import Country
        germany = Country("germany")
        agents = AgentFactory(how_many_agents,germany).agents
        sim = Simulation(agents)
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
        agents = AgentFactory(10,germany).agents
        agents[0].alive = False
        import evaluation
        result = evaluation.evaluate(agents)
        print(result)
        self.assertEqual(result['alive'], 9)
        self.assertEqual(result['dead'], 1)

    def test_with_simu(self):
        import evaluation
        sim1000 = self.create_sim(1000)
        previous = evaluation.evaluate(sim1000.agents)
        print(f"previous: {previous}")
        for i in range(10):
            sim1000.run(20, False)
            result = evaluation.evaluate(sim1000.agents)
            print(f"after: {result}")
        self.assertGreater(result['dead'], 1)
        self.assertGreater(result['alive'], 1)

    def test_simulation(self):
        sim = self.create_sim(1000)
        sim.run(100)


if __name__ == "__main__":
    unittest.main()
