import unittest


class TestSimulation(unittest.TestCase):

    def test_basics(self):
        from agent_factory import AgentFactory
        agents = AgentFactory(10).agents
        self.assertEqual(10, len(agents))




if __name__ == "__main__":
    unittest.main()