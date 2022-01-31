from simulation import Simulation
from agent_factory import AgentFactory


def test_run():
    agents = AgentFactory(100).agents
    simulation = Simulation(agents, 100)
    simulation.run()

test_run()