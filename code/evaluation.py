
def evaluate_aliveness(agents):
    alive = 0
    dead = 0
    for agent in agents:
        if agent.alive:
            alive += 1
        else:
            dead += 1
    return {"alive": alive, "dead": dead}


def evaluate(agents):
    reg, add, clean, alive, dead = 0, 0, 0, 0, 0
    for agent in agents:
        if not agent.alive:
            dead += 1
            continue
        alive += 1
        if agent.addicted:
            add += 1
        elif agent.is_regular_user:
            reg += 1
        elif not agent.is_regular_user and not agent.addicted:
            clean += 1
    return {"alive": alive, "dead": dead, "addicted": add, "regular_use": reg,"clean": clean}







