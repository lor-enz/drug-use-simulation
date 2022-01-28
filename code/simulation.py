class Simulation():

    def __init__(self, agents, total_cycles):
        self.agents = agents
        self.cycle = 0
        self.total_cycles = total_cycles

    def run(self):
        assert len(self.agents) > 0

        while self.cycle < self.total_cycles:
            for agent in self.agents:
                agent.do_something(self.cycle)
            self.cycle = self.cycle + 1
            # Just for the progess bar:
            if self.cycle % (int(self.total_cycles / 20)) == 0:
                print(f'{int((self.cycle / self.total_cycles) * 100)}% of Simulation done')
        print("Done")

    def get_cycle_number(self):
        return self.cycle
