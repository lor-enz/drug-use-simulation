##
# This file is just a dumping place for global variables and globally used functions.
# It is not intended to remain and should be renamed or deleted and the content moved somewhere else.



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
from random import seed
from random import random

class Gender(Enum):
    Male = "Male"
    Female = "Female"

# Rename this to something easier to understand
def evaluate(probability):
    if random() < probability:
        return True
    else:
        return False


def convert_agents_to_df(agents, size_for_progress_bar):
    import pandas as pd
    column_names = ["is_alive", "gender", "regular_user", "addicted", "usage_history"]
    df = pd.DataFrame(columns = column_names)

    # Inefficient with 100000 this presumably takes over half an hour
    counter = 0
    for agent in agents:
        df = df.append({'is_alive': agent.alive, 'gender': agent.gender, 'regular_user': agent.is_regular_user, 'addicted': agent.addicted, 'usage_history': agent.usage_history}, ignore_index=True)
        # Just for the progess bar:
        counter = counter + 1
        if counter % (int(size_for_progress_bar / 20)) == 0:
            print(f'{int((counter/size_for_progress_bar)*100)}% of df conversion done')
    return df