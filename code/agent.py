import stuff
import simulation
from stuff import evaluate

class Agent:
    def __init__(self, gender, is_regular_user, addicted,genetic_risk_factor):
        self.alive = True
        self.addicted = addicted
        self.is_regular_user = is_regular_user
        self.gender = gender
        # first 'friends_innerCircle_quantity' friends are innercircle friends
        self.friends = []
        self.usage_history = []
        self.dead_friends = []

        self.genetic_risk = genetic_risk_factor
        self.social_risk = 0.02

    def do_something(self, current_cycle):
        if not self.alive:
            return
        if self.refresh_is_regular_user(current_cycle):
            self.check_if_will_be_clean()
        else:
            if self.check_if_will_start_using():
                self.use_drugs(current_cycle)
        self.maybe_use_drugs(current_cycle)
        self.maybe_die()

        # Don't perform refresh here.
        # Otherwise the order in which the agents list is sorted changes the outcome.

    def refresh_values(self, current_cycle):
        if not self.alive:
            return
        self.refresh_is_regular_user(current_cycle)
        self.refresh_is_addicted(current_cycle)

    def check_if_will_be_clean(self):
        assert self.is_regular_user
        probability = 0.05  # ToDo calculate this
        return evaluate(probability)

    def check_if_will_start_using(self):
        assert not self.is_regular_user
        probability = 0.06  # ToDo calculate this
        return evaluate(probability)

    def maybe_use_drugs(self, current_cycle):
        probability = 0.008
        if evaluate(probability):
            self.use_drugs(current_cycle)
            return True
        else:
            return False

    def use_drugs(self, current_cycle):
        self.usage_history.append(current_cycle)

    def maybe_die(self):
        probability = 0.008
        if evaluate(probability):
            self.alive = False
            for i in range(0, len(self.friends)):
                self.friends[i].dead_friends.append(self)
                if i >= simulation.Simulation.friends_innerCircle_quantity:
                    self.friends[i].dead_friends.remove(self)

        return self.alive

    def refresh_is_regular_user(self, current_cycle):
        sum_of_uses_in_recent_past = 0
        for i in self.usage_history:
            if (current_cycle - i) < stuff.lookback_to_determine_regular_use:
                sum_of_uses_in_recent_past += 1

        if sum_of_uses_in_recent_past >= stuff.threshold_to_determine_regular_use:
            self.is_regular_user = True
        else:
            self.is_regular_user = False
        return self.is_regular_user

    def refresh_is_addicted(self, current_cycle):
        sum_of_uses_in_recent_past = 0
        for i in self.usage_history:
            if (current_cycle - i) < stuff.lookback_to_determine_addiction:
                sum_of_uses_in_recent_past += 1

        if sum_of_uses_in_recent_past >= stuff.threshold_to_determine_addiction:
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
