import unittest


class TestSimulation(unittest.TestCase):

    def setUp(self) -> None:
        from simulation import Simulation
        from agent_factory import AgentFactory
        agents = AgentFactory(1000).agents
        self.sim1000 = Simulation(agents, 50)
        self.sim1000.run()

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
        import evaluation
        result = evaluation.evaluate(self.sim1000.agents)
        print(result)
        self.assertGreater(result['dead'], 1)
        self.assertGreater(result['alive'], 1)


if __name__ == "__main__":
    unittest.main()
