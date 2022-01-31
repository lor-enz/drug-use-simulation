import unittest


class TestSimulation(unittest.TestCase):

    def test_basics(self):
        from simulation import Simulation
        from agent_factory import AgentFactory
        agents = AgentFactory(10).agents
        sim = Simulation(agents, 10)
        len(sim.agents)
        self.assertEqual(10, len(sim.agents))




if __name__ == "__main__":
    unittest.main()