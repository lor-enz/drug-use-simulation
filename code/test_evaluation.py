import unittest


class TestSimulation(unittest.TestCase):

    def sim1000(self):
        from simulation import Simulation
        from agent_factory import AgentFactory
        agents = AgentFactory(1000).agents
        sim1000 = Simulation(agents, 50)
        sim1000.run()
        print("SETUP done")
        return sim1000

    def test_basics(self):
        from agent_factory import AgentFactory
        agents = AgentFactory(10).agents
        agents[0].alive = False
        import evaluation
        result = evaluation.evaluate(agents)
        print(result)
        self.assertEqual(result['alive'], 9)
        self.assertEqual(result['dead'], 1)

    def test_with_simu(self):
        sim1000 = self.sim1000()
        import evaluation
        result = evaluation.evaluate(sim1000.agents)
        print(result)
        self.assertGreater(result['dead'], 1)
        self.assertGreater(result['alive'], 1)


if __name__ == "__main__":
    unittest.main()
