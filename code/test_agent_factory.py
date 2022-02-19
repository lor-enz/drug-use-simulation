import unittest


class TestAgentFactory(unittest.TestCase):

    def test_basics(self):
        from agent_factory import AgentFactory
        from country import Country
        germany = Country("germany")
        agents = AgentFactory(300, germany).agents
        self.assertEqual(300, len(agents))

    def test_usage_history(self):
        from agent_factory import AgentFactory
        from country import Country
        germany = Country("germany")
        factory = AgentFactory(2, germany)
        is_regular_user_false = {"amphetamines": False, "cannabis": False, "cocaine": False, "opioid": False}
        is_regular_user_true = {"amphetamines": True, "cannabis": True, "cocaine": True, "opioid": True}
        is_addicted_false = {"amphetamines": False, "cannabis": False, "cocaine": False, "opioid": False}
        is_addicted_true = {"amphetamines": True, "cannabis": True, "cocaine": True, "opioid": True}

        factory.create_usage_history(is_regular_user_true, is_addicted_false)
        factory.create_usage_history(is_regular_user_true, is_addicted_true)
        factory.create_usage_history(is_regular_user_false, is_addicted_false)


if __name__ == "__main__":
    unittest.main()
