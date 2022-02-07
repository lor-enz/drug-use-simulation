import unittest


class TestAgentFactory(unittest.TestCase):

    def test_basics(self):
        from agent_factory import AgentFactory
        agents = AgentFactory(300).agents
        self.assertEqual(300, len(agents))


    def test_usage_history(self):
        from agent_factory import AgentFactory
        factory = AgentFactory(2)
        factory.create_usage_history(True, False)
        factory.create_usage_history(True, True)
        factory.create_usage_history(False, False)

if __name__ == "__main__":
    unittest.main()