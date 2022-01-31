import random


class Simulation():

    def __init__(self, agents, total_cycles):
        self.agents = agents
        self.cycle = 0
        self.total_cycles = total_cycles

    def run(self):
        assert len(self.agents) > 0

        random.seed(42)
        while self.cycle < self.total_cycles:
            for agent in self.agents:
                agent.refresh_values(self.cycle)
            for agent in self.agents:
                agent.do_something(self.cycle)
            self.cycle = self.cycle + 1
            # Just for the progress bar:
            if self.cycle % max((int(self.total_cycles / 20)), 1) == 0:
                print(f'{int((self.cycle / self.total_cycles) * 100)}% of Simulation done')
        print("Done")
