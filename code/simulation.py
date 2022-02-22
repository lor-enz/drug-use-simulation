import random
import agent_factory
import numpy as np
import scipy.stats
import drug as d

import evaluation as evalua
import pandas as pd

from datetime import datetime


class Simulation:
    friends_quantity = 137
    friends_innerCircle_quantity = 17

    def __init__(self, agents, label="Unnamed"):
        self.label = label
        self.agents = agents
        self.results = []
        self.set_friends(self.agents, self.friends_innerCircle_quantity, 0)
        print("Permanent friends initialized")
        self.set_friends(self.agents, self.friends_quantity, self.friends_innerCircle_quantity)
        print("Periodic friends initialized")
        self.completed_cycles = 0

    def run(self, cycles_todo_this_run):
        assert len(self.agents) > 0
        random.seed(42)
        current_cycle = 0

        while current_cycle < cycles_todo_this_run:

            # get new friends
            if (current_cycle > 0):
                for ag in self.agents:
                    self.lose_friends(ag)
                    ag.refresh_values(self.completed_cycles)
                self.set_friends(self.agents, self.friends_quantity, self.friends_innerCircle_quantity)

            eval_results = evalua.evaluate(self.agents)
            print(f"Cycle: {self.completed_cycles} -> {eval_results}")
            self.add_to_results(self.completed_cycles, eval_results)

            for ag in self.agents:
                ag.do_something(self.completed_cycles)

            current_cycle += 1
            self.completed_cycles += 1
        print(f"completed_cycles: {self.completed_cycles}")
        evalua.create_plot(self.label, self.results)

    def add_to_results(self, current_cycle, obj, skip_early_cycles=True):
        if self.completed_cycles < 3 and skip_early_cycles:
            return
        obj["cycle"] = current_cycle
        self.results.append(obj)

    """
    Sets 2 agents in friend relationship
    :param agents: list of agents
    :param friends_quantity: Number of max friends of agent
    :param exchangeable_index: Agents in friendlist with index higher than exchangeable_index 
                              will be exchange if deadlock occurs (Should equal permanent friends number)
    """

    def set_friends(self, agents, friends_quantity, exchangeable_index):
        agents_searching_friends = agents.copy()
        # for agent in self.agents:
        while len(agents_searching_friends) > 0:
            agent = agents_searching_friends[0]
            rounds_searching = 0
            while friends_quantity > len(agent.friends):
                rounds_searching += 1
                # possible deadlock, change already set friend relationships
                if rounds_searching > len(agents_searching_friends):
                    is_found_friend = False
                    while not is_found_friend:
                        randomFriend = random.choice(agents)
                        if randomFriend.alive:
                            # dont take innercircle friends
                            exchangeable_friends = randomFriend.friends[exchangeable_index:]
                            for friend_of_randomFriend in exchangeable_friends:
                                if not (
                                        agent in randomFriend.friends or agent in friend_of_randomFriend.friends or agent is randomFriend or agent is friend_of_randomFriend):
                                    randomFriend.friends.remove(friend_of_randomFriend)
                                    friend_of_randomFriend.friends.remove(randomFriend)
                                    randomFriend.friends.append(agent)
                                    agent.friends.append(randomFriend)
                                    # enough permanent friends?
                                    if (exchangeable_index == 0 and len(agent.friends) >= friends_quantity):
                                        agents_searching_friends.append(friend_of_randomFriend)
                                    else:
                                        agent.friends.append(friend_of_randomFriend)
                                        friend_of_randomFriend.friends.append(agent)
                                    is_found_friend = True
                                    break
                else:
                    randomFriend = random.choice(agents_searching_friends)
                    if randomFriend.alive:
                        # add if random agent not this agent or not already a friend or random agent friend list not full
                        if not (agent is randomFriend or randomFriend in agent.friends or len(
                                randomFriend.friends) >= friends_quantity):
                            agent.friends.append(randomFriend)
                            randomFriend.friends.append(agent)
                # remove randomfriend with full friends if he was searching friends before
                if friends_quantity <= len(randomFriend.friends) and randomFriend in agents_searching_friends:
                    agents_searching_friends.remove(randomFriend)
                # remove agent with full friends
                if friends_quantity <= len(agent.friends) and agent in agents_searching_friends:
                    agents_searching_friends.remove(agent)

    def beta_distr(self, min_val, max_val, mean, std):
        # https://stackoverflow.com/questions/27831923/python-random-number-generator-with-mean-and-standard-deviation
        scale = max_val - min_val
        location = min_val
        # Mean and standard deviation of the unscaled beta distribution
        unscaled_mean = (mean - min_val) / scale
        unscaled_var = (std / scale) ** 2
        # Computation of alpha and beta can be derived from mean and variance formulas
        t = unscaled_mean / (1 - unscaled_mean)
        beta = ((t / unscaled_var) - (t * t) - (2 * t) - 1) / ((t * t * t) + (3 * t * t) + (3 * t) + 1)
        alpha = beta * t
        # Not all parameters may produce a valid distribution
        if alpha <= 0 or beta <= 0:
            raise ValueError('Cannot create distribution for the given parameters.')
        return scipy.stats.beta.rvs(alpha, beta, scale=scale, loc=location)
        # Make scaled beta distribution with computed parameters for report
        # return scipy.stats.beta(alpha, beta, scale=scale, loc=location)

    def lose_friends(self, agent):
        min_val = 0
        max_val = self.friends_quantity - self.friends_innerCircle_quantity
        mean = 14
        std = 14
        friends_to_lose = round(self.beta_distr(min_val, max_val, mean, std))
        while (friends_to_lose > 0 and self.friends_innerCircle_quantity - len(agent.friends) < 0):
            friend = agent.friends[random.randint(self.friends_innerCircle_quantity, len(agent.friends) - 1)]
            agent.friends.remove(friend)
            friend.friends.remove(agent)
            friends_to_lose -= 1
        '''
        #Plot for report, delete after report done
        x = np.linspace(min_val, max_val, 9999999)
        plt.plot(x, my_dist.pdf(x))
        # Stats
        print('mean:', my_dist.mean(), 'std:', my_dist.std())
        # Get a large sample to check bounds
        sample = my_dist.rvs(size=9999999)
        print('min:', sample.min(), 'max:', sample.max())
        '''
