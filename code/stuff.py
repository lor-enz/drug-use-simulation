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
    return random() < probability


