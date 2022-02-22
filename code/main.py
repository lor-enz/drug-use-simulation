from simulation import Simulation
from agent_factory import AgentFactory
import country
import settings


def test_run():
    agents = AgentFactory(100000, country.germany).agents
    simulation = Simulation(agents)
    simulation.run(1000)


test_run()
