from random import random, choice
import stuff
from stuff import Gender
from agent import Agent


class AgentFactory():

    def __init__(self, how_many_agents):
        self.agents = []
        self.how_many_agents = how_many_agents
        self.create_agents()
        self.set_friends(Agent.friends_innerCircle_quantity ,0)
        print("Permanent friends initialized")
        self.set_friends(Agent.friends_quantity, Agent.friends_innerCircle_quantity)
        print("Periodic friends initialized")

    def create_agents(self):
        while len(self.agents) < self.how_many_agents:
            self.agents.append(self.create_random_agent())

    def create_random_agent(self):
        gender = stuff.Gender.Female if (random() <= stuff.init_population_percentage_female) else stuff.Gender.Male
        using = True if (random() <= stuff.init_population_percentage_using) else False
        addicted = True if (
                    random() <= stuff.init_population_percentage_using * stuff.init_users_percentage_addicted) else False

        return Agent(gender, using, addicted)

    """
    Sets 2 agents in friend relationship
    :param friends_quantity: Number of max friends of agent
    :param exchangable_index: Agents in friendlist with index higher than exchangable_index 
                              will be exchange if deadlock occurs (Should equal permanent friends number)
    """
    def set_friends(self, friends_quantity, exchangable_index):
        agents_searching_friends = self.agents.copy()
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
                        randomFriend = choice(self.agents)
                        #dont take innercircle friends
                        exchangable_friends = randomFriend.friends[exchangable_index:]
                        for friend_of_randomFriend in exchangable_friends:
                            if not (agent in randomFriend.friends or agent in friend_of_randomFriend.friends or agent is randomFriend or agent is friend_of_randomFriend):
                                randomFriend.friends.remove(friend_of_randomFriend)
                                friend_of_randomFriend.friends.remove(randomFriend)
                                randomFriend.friends.append(agent)
                                agent.friends.append(randomFriend)
                                #enough permanent friends?
                                if (exchangable_index == 0 and len(agent.friends) >= friends_quantity):
                                    agents_searching_friends.append(friend_of_randomFriend)
                                else:
                                    agent.friends.append(friend_of_randomFriend)
                                    friend_of_randomFriend.friends.append(agent)
                                is_found_friend = True
                                break
                else:
                    randomFriend = choice(agents_searching_friends)
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
