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
        agents = AgentFactory(10, germany).agents
        agents[0].alive = False
        import evaluation
        result = evaluation.evaluate(agents)
        print(result)
        self.assertEqual(result['alive'], 9)
        self.assertEqual(result['dead'], 1)

    def test_small_pop(self):
        from agent_factory import AgentFactory
        from country import Country
        germany = Country("germany")
        agents = AgentFactory(100,germany).agents
        agents[0].alive = False
        import evaluation
        result = evaluation.evaluate(agents)
        print(result)

    def test_small_simu(self):
        import random
        random.seed(10)
        import evaluation
        sim = self.create_sim(300)
        previous = evaluation.evaluate(sim.agents)
        print(f"previous: {previous}")
        for i in range(50):
            sim.run(1)
            result = evaluation.evaluate(sim.agents)
            print(f"after: {result}")


    def test_small_simu2(self):
        import random
        random.seed(10)
        import evaluation
        sim = self.create_sim(300)
        previous = evaluation.evaluate(sim.agents)
        print(f"previous: {previous}")
        sim.run(50)
        result = evaluation.evaluate(sim.agents)
        print(f"after: {result}")

    def test_with_simu(self):
        import evaluation
        sim1000 = self.create_sim(10000)
        previous = evaluation.evaluate(sim1000.agents)
        print(f"previous: {previous}")
        for i in range(1):
            sim1000.run(100)
            result = evaluation.evaluate(sim1000.agents)
            print(f"after: {result}")

    def test_simulation(self):
        sim = self.create_sim(1000)
        sim.run(100)


if __name__ == "__main__":
    unittest.main()
