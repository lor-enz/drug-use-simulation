from simulation import Simulation
from agent_factory import AgentFactory


def test_run():
    agents = AgentFactory(1000).agents
    simulation = Simulation(agents, 1000)
    simulation.run()

test_run()