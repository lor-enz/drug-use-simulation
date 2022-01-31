from random import random, choice
import stuff
from stuff import Gender
from agent import Agent


class AgentFactory():

    def __init__(self, how_many_agents):
        self.agents = []
        self.how_many_agents = how_many_agents
        self.create_agents()
        self.set_friends()

    def create_agents(self):
        while len(self.agents) < self.how_many_agents:
            self.create_random_agent()

    def create_random_agent(self):
        gender = stuff.Gender.Female if (random() <= stuff.init_population_percentage_female) else stuff.Gender.Male
        using = True if (random() <= stuff.init_population_percentage_using) else False
        addicted = True if (
                    random() <= stuff.init_population_percentage_using * stuff.init_users_percentage_addicted) else False

        self.agents.append(Agent(gender, using, addicted))

    def set_friends(self):
        agents_searching_friends = self.agents.copy()
        for agent in self.agents:
            rounds_searching = 0
            while agent.friends_quantity>len(agent.friends):
                rounds_searching += 1
                # possible deadlock, change already set friend relationships
                if rounds_searching > len(agents_searching_friends):
                    is_found_friend = False
                    while not is_found_friend:
                        randomFriend = choice(self.agents)
                        for friend_of_randomFriend in randomFriend.friends:
                            if not (agent in friend_of_randomFriend.friends and agent in randomFriend.friends and agent is randomFriend and agent is friend_of_randomFriend):
                                friend_of_randomFriend.friends.remove(randomFriend)
                                randomFriend.friends.remove(friend_of_randomFriend)
                                friend_of_randomFriend.friends.append(agent)
                                randomFriend.friends.append(agent)
                                agent.friends.append(friend_of_randomFriend)
                                agent.friends.append(randomFriend)
                                is_found_friend = True
                                break
                else:
                    randomFriend = choice(agents_searching_friends)
                    #add if random agent not this agent or not already a friend or random agent friend list not full
                    if not (agent is randomFriend or randomFriend in agent.friends or len(randomFriend.friends) >= agent.friends_quantity):
                        agent.friends.append(randomFriend)
                        randomFriend.friends.append(agent)
                # remove randomfriend with full friends
                if agent.friends_quantity <= len(randomFriend.friends) and randomFriend in agents_searching_friends:
                     agents_searching_friends.remove(randomFriend)
                # remove agent with full friends
                if agent.friends_quantity <= len(agent.friends) and agent in agents_searching_friends:
                    agents_searching_friends.remove(agent)
        print("Friends initialized")