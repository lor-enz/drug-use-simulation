import unittest


class TestSimulation(unittest.TestCase):

    def test_basics(self):
        from simulation import Simulation
        from agent_factory import AgentFactory
        import evaluation as evaluation
        agents = AgentFactory(10).agents
        sim = Simulation(agents, 50)
        sim.run()
        df = evaluation.convert_agents_to_df(sim.agents)
        result = evaluation.how_many_are_alive(df)

        print(f'Percentage Dead:  {result[False]}')
        print(f'Percentage Alive: {result[True]}')

        result = evaluation.how_many_are_addicted(df)

        print(f'Percentage not addicted:  {result[False]}')
        # print(f'Percentage addicted: {result[True]}')


if __name__ == "__main__":
    unittest.main()
