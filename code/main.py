from simulation import Simulation
from agent_factory import AgentFactory
import country
import settings


def test_run():
    germany = country.Country("germany")
    agents = AgentFactory(1000,germany).agents
    simulation = Simulation(agents)
    simulation.run(1000)

test_run()