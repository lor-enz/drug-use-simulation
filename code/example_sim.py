# How many cycles to look back to determine is the Agent is declared a regular drug user
lookback_to_determine_regular_use = 20
# How often in that time til they are declared a regular user
threshold_to_determine_regular_use = 6

# How many cycles to look back to determine is the Agent is declared addicted
lookback_to_determine_addiction = 30
# How often in that time til they are declared addicted
threshold_to_determine_addiction = 20

# How often a do_something() is performed on all agents in the simulation run.
number_of_cycles = 50

# Init Variables
init_population_percentage_using = 0.10
init_users_percentage_addicted = 0.50
init_population_percentage_female = 0.496


from enum import Enum
class Gender(Enum):
    Male = "Male"
    Female = "Female"
    

from random import seed
from random import random
custom_seed = 4200
seed(custom_seed)



class Simulation():
        
    def __init__(self, agents):
        self.agents = agents
        self.cycle = 0
    
    def run(self):
        assert len(self.agents) > 0
        
        while self.cycle < number_of_cycles:
            for agent in self.agents:
                agent.do_something()
            self.cycle = self.cycle + 1
            # Just for the progess bar:
            if self.cycle % (int(number_of_cycles / 20)) == 0:
                print(f'{int((self.cycle/number_of_cycles)*100)}% of Simulation done')
        print("Done")
        
    def get_cycle_number(self):
        return self.cycle

# Rename this to something easier to understand
def evaluate(probability):
    if random() < probability:
        return True
    else:
        return False


class Person():
    
    def __init__(self, gender,  is_regular_user, addicted):
        self.alive = True
        self.addicted = addicted
        self.is_regular_user = is_regular_user
        self.gender = gender
        self.friends = []
        self.usage_history = []

        self.genetic_risk = 0.02
        self.social_risk = 0.02

    def do_something(self):
        if not self.alive:
            return
        if self.refresh_is_regular_user():
            self.check_if_will_be_clean()
        else:
            if self.check_if_will_start_using():
                self.use_drugs()
        self.maybe_use_drugs()
        self.maybe_die()
        
        self.refresh_is_regular_user()
        self.refresh_is_addicted()
        
        
    
    def check_if_will_be_clean(self):
        assert self.is_regular_user
        probability = 0.05 # ToDo calculate this
        return evaluate(probability)
        
        
    def check_if_will_start_using(self):
        assert not self.is_regular_user
        probability = 0.06 # ToDo calculate this
        return evaluate(probability)
    
    def maybe_use_drugs(self):
        probability = 0.008
        if evaluate(probability):
            self.use_drugs()
            return True
        else:
            return False
    
    def use_drugs(self):
        self.usage_history.append(simulation.get_cycle_number())
    
    def maybe_die(self):
        probability = 0.008
        if evaluate(probability):
            self.alive = False
        return self.alive
    
    def refresh_is_regular_user(self):
        current_cycle = simulation.get_cycle_number()
        sum_of_uses_in_recent_past = 0
        for i in self.usage_history:
            if (current_cycle - i) < lookback_to_determine_regular_use:
                sum_of_uses_in_recent_past += 1
                
        if sum_of_uses_in_recent_past >= threshold_to_determine_regular_use:
            self.is_regular_user = True
        else: 
            self.is_regular_user = False
        return self.is_regular_user
    
    def refresh_is_addicted(self):
        current_cycle = simulation.get_cycle_number()
        sum_of_uses_in_recent_past = 0
        for i in self.usage_history:
            if (current_cycle - i) < lookback_to_determine_addiction:
                sum_of_uses_in_recent_past += 1
                
        if sum_of_uses_in_recent_past >= threshold_to_determine_addiction:
            self.addicted = True
        else: 
            self.addicted = False
        return self.addicted
        
    def __str__(self):
        return f"""Agent 
     Is Alive     : {self.alive}
     Gender       : {self.gender}
     Regular User : {self.is_regular_user}
     Addicted     : {self.addicted}
     Usage History: {self.usage_history}
     Regular User : {self.is_regular_user}"""
            
simulation = Simulation([])
agent = Person(Gender.Male, False, False)
print(agent)
agent.use_drugs()
simulation.cycle =+ 1
print(agent)
agent.use_drugs()
print(agent)


# seed random number generator

# generate some random numbers
print(random(), random(), random())
# reset the seed
seed(custom_seed)
# generate some random numbers
print(random(), random(), random())


class AgentFactory():
    
    def __init__(self, how_many_agents):
        self.agents = []
        self.how_many_agents = how_many_agents
        self.create_agents()
    
    def create_agents(self):
        while (len(self.agents) < self.how_many_agents):
               self.create_random_agent()
            
    def create_random_agent(self):
    
        gender = Gender.Female if (random() <= init_population_percentage_female) else Gender.Male
        using = True if (random() <= init_population_percentage_using) else False
        addicted = True if (random() <= init_population_percentage_using * init_users_percentage_addicted) else False
        
        self.agents.append(Person(gender, using, addicted))


def convert_agents_to_df(agents):
    import pandas as pd
    column_names = ["is_alive", "gender", "regular_user", "addicted", "usage_history"]
    df = pd.DataFrame(columns = column_names)

    # Inefficient with 100000 this presumably takes over half an hour
    counter = 0
    for agent in agents:
        df = df.append({'is_alive': agent.alive, 'gender': agent.gender, 'regular_user': agent.is_regular_user, 'addicted': agent.addicted, 'usage_history': agent.usage_history}, ignore_index=True)
        # Just for the progess bar:
        counter = counter + 1
        if counter % (int(size / 20)) == 0:
            print(f'{int((counter/size)*100)}% of df conversion done')
    return df

size = 100
agent_factory = AgentFactory(size)
print("Agent Factory done")
df = convert_agents_to_df(agent_factory.agents)


print(df.is_alive.value_counts(normalize=True))
print('..')
print(df.gender.value_counts(normalize=True))
print('..')
print(df.regular_user.value_counts(normalize=True))
print('..')
print(df.addicted.value_counts(normalize=True))



simulation = Simulation(agents=agent_factory.agents)
simulation.run()
df = convert_agents_to_df(simulation.agents)


print(df.is_alive.value_counts(normalize=True))
print('..')
print(df.gender.value_counts(normalize=True))
print('..')
print(df.regular_user.value_counts(normalize=True))
print('..')
print(df.addicted.value_counts(normalize=True))