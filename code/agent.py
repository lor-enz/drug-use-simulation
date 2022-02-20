import settings
import simulation
import agent_factory
import drug
from random import random


class Agent:
    def __init__(self, gender, is_regular_user, addicted, genetic_risk_factor, country):
        self.country = country
        self.alive = True
        self.addicted = addicted
        self.is_regular_user = is_regular_user
        self.gender = gender
        # first 'friends_innerCircle_quantity' friends are innercircle friends
        self.friends = []
        self.usage_history = {"amphetamine": [], "cannabis": [], "cocaine": [], "opioid": []}
        self.dead_friends = []

        self.genetic_risk = genetic_risk_factor
        self.social_risk = 0.02

    def do_something(self, current_cycle):
        if not self.alive:
            return
        for substance in settings.set.drugs:
            if self.refresh_is_regular_user(current_cycle, substance):
                self.maybe_use_drugs(current_cycle, substance)
                # self.check_if_will_be_clean()
            else:
                self.maybe_start_using(current_cycle, substance)

        # Don't perform refresh here.
        # Otherwise the order in which the agents list is sorted changes the outcome.

    def refresh_values(self, current_cycle):
        if not self.alive:
            return
        for substance in settings.set.drugs:
            self.refresh_is_regular_user(current_cycle, substance)
            self.refresh_is_addicted(current_cycle, substance)

    def maybe_start_using(self, current_cycle, substance):
        assert not self.is_regular_user[substance.name]
        # per drug
        # sum_friends_using/friends_number+genetic_factor+ country drug_acceptance
        addicted_friends = 0
        for friend in self.friends:
            if friend.addicted.get(substance.name):
                addicted_friends += 1
        friends_number = len(self.friends)
        prob = (addicted_friends / friends_number + self.country.drug_acceptance + self.genetic_risk) / settings.set.rounds_in_year
        if evaluate(prob):
            self.use_drugs(current_cycle, substance)

    def maybe_use_drugs(self, current_cycle, substance):
        # opioid_dependence_potential of addicted drug / 4 +country drug_acceptance+genetic_factor
        if evaluate(
                substance.dependence_potential / settings.set.dependence_potential_normalization + self.country.drug_acceptance + self.genetic_risk):
            self.use_drugs(current_cycle, substance)

    def use_drugs(self, current_cycle, substance):
        self.usage_history[substance.name].append(current_cycle)
        self.maybe_die(substance)

    def maybe_die(self, substance):
        # for each propability in last step of history drug mortality_rate/weeks
        probability = substance.mortality_rate / settings.set.rounds_in_year
        if evaluate(probability):
            self.alive = False
            for i in range(0, len(self.friends)):
                self.friends[i].dead_friends.append(self)
                if i >= simulation.Simulation.friends_innerCircle_quantity:
                    self.friends[i].dead_friends.remove(self)
        return self.alive

    def refresh_is_regular_user(self, current_cycle, substance):
        sum_of_uses_in_recent_past = 0
        for i in self.usage_history[substance.name]:
            if (current_cycle - i) < settings.set.lookback_to_determine_regular_use:
                sum_of_uses_in_recent_past += 1

        if sum_of_uses_in_recent_past >= settings.set.threshold_to_determine_regular_use:
            self.is_regular_user[substance.name] = True
        else:
            self.is_regular_user[substance.name] = False
        return self.is_regular_user[substance.name]

    def refresh_is_addicted(self, current_cycle, substance):
        sum_of_uses_in_recent_past = 0
        for i in self.usage_history[substance.name]:
            if (current_cycle - i) < settings.set.lookback_to_determine_addiction:
                sum_of_uses_in_recent_past += 1

        if sum_of_uses_in_recent_past >= settings.set.threshold_to_determine_addiction:
            self.addicted[substance.name] = True
        else:
            self.addicted[substance.name] = False
        return self.addicted[substance.name]

    def __str__(self):
        return f"""Agent 
     Is Alive     : {self.alive}
     Gender       : {self.gender}
     Regular User : {self.is_regular_user}
     Addicted     : {self.addicted}
     Usage History: {self.usage_history}"""


def evaluate(probability):
    return random() < probability
