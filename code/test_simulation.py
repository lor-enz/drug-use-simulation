import unittest


class TestSimulation(unittest.TestCase):

    def test_basics(self):
        from simulation import Simulation
        from agent_factory import AgentFactory
        agents = AgentFactory(20000).agents
        sim = Simulation(agents, 10)

    def test_simulation(self):
        from simulation import Simulation
        from agent_factory import AgentFactory
        agents = AgentFactory(20000).agents
        sim = Simulation(agents, 10)
        sim.run()


if __name__ == "__main__":
    unittest.main()
