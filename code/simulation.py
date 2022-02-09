import random
import agent_factory
import agent
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt


class Simulation():
    friends_quantity = 137
    friends_innerCircle_quantity = 17

    def __init__(self, agents, total_cycles):
        self.agents = agents
        self.set_friends(self.agents,self.friends_innerCircle_quantity, 0)
        print("Permanent friends initialized")
        self.set_friends(self.agents,self.friends_quantity, self.friends_innerCircle_quantity)
        print("Periodic friends initialized")
        self.cycle = 0
        self.total_cycles = total_cycles

    def run(self):
        assert len(self.agents) > 0

        random.seed(42)
        while self.cycle < self.total_cycles:

            #get new friends
            if(self.cycle>0):
                for agent in self.agents:
                    self.lose_friends(agent)
                self.set_friends(self.agents, self.friends_quantity, self.friends_innerCircle_quantity)

            for agent in self.agents:
                agent.refresh_values(self.cycle)
            for agent in self.agents:
                agent.do_something(self.cycle)
            self.cycle = self.cycle + 1
            # Just for the progress bar:
            if self.cycle % max((int(self.total_cycles / 20)), 1) == 0:
                print(f'{int((self.cycle / self.total_cycles) * 100)}% of Simulation done')
        print("Done")

    """
    Sets 2 agents in friend relationship
    :param agents: list of agents
    :param friends_quantity: Number of max friends of agent
    :param exchangeable_index: Agents in friendlist with index higher than exchangeable_index 
                              will be exchange if deadlock occurs (Should equal permanent friends number)
    """
    def set_friends(self,agents, friends_quantity, exchangeable_index):
        agents_searching_friends = agents.copy()
       # for agent in self.agents:
        while len(agents_searching_friends)>0:
            agent = agents_searching_friends[0]
            rounds_searching = 0
            while friends_quantity>len(agent.friends):
                rounds_searching += 1
                # possible deadlock, change already set friend relationships
                if rounds_searching > len(agents_searching_friends):
                    is_found_friend = False
                    while not is_found_friend:
                        randomFriend = random.choice(agents)
                        #dont take innercircle friends
                        exchangeable_friends = randomFriend.friends[exchangeable_index:]
                        for friend_of_randomFriend in exchangeable_friends:
                            if not (agent in randomFriend.friends or agent in friend_of_randomFriend.friends or agent is randomFriend or agent is friend_of_randomFriend):
                                randomFriend.friends.remove(friend_of_randomFriend)
                                friend_of_randomFriend.friends.remove(randomFriend)
                                randomFriend.friends.append(agent)
                                agent.friends.append(randomFriend)
                                #enough permanent friends?
                                if (exchangeable_index == 0 and len(agent.friends) >= friends_quantity):
                                    agents_searching_friends.append(friend_of_randomFriend)
                                else:
                                    agent.friends.append(friend_of_randomFriend)
                                    friend_of_randomFriend.friends.append(agent)
                                is_found_friend = True
                                break
                else:
                    randomFriend = random.choice(agents_searching_friends)
                    #add if random agent not this agent or not already a friend or random agent friend list not full
                    if not (agent is randomFriend or randomFriend in agent.friends or len(randomFriend.friends) >= friends_quantity):
                        agent.friends.append(randomFriend)
                        randomFriend.friends.append(agent)
                # remove randomfriend with full friends if he was searching friends before
                if friends_quantity <= len(randomFriend.friends) and randomFriend in agents_searching_friends:
                    agents_searching_friends.remove(randomFriend)
                # remove agent with full friends
                if friends_quantity <= len(agent.friends) and agent in agents_searching_friends:
                    agents_searching_friends.remove(agent)

    def beta_distr(self,min_val, max_val, mean, std):
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
        #return scipy.stats.beta(alpha, beta, scale=scale, loc=location)

    def lose_friends(self,agent):
        min_val = 0
        max_val = 120
        mean = 14
        std = 14
        friends_to_lose = round(self.beta_distr(min_val, max_val, mean, std))
        while(friends_to_lose > 0):
            friend=agent.friends[random.randint(self.friends_innerCircle_quantity, len(agent.friends)-1)]
            agent.friends.remove(friend)
            friend.friends.remove(agent)
            friends_to_lose-=1
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