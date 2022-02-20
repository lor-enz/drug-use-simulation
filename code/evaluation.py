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
    clean, alive, dead = 0, 0, 0
    add_amph, add_cann, add_coca, add_opio = 0, 0, 0, 0
    reg_amph, reg_cann, reg_coca, reg_opio = 0, 0, 0, 0

    for agent in agents:
        if not agent.alive:
            dead += 1
            continue
        alive += 1
        is_clean = True
        if agent.addicted["amphetamines"]:
            add_amph += 1
            is_clean = False
        if agent.addicted["cannabis"]:
            add_cann += 1
            is_clean = False
        if agent.addicted["cocaine"]:
            add_coca += 1
            is_clean = False
        if agent.addicted["opioid"]:
            add_opio += 1
            is_clean = False

        if agent.is_regular_user["amphetamines"]:
            reg_amph += 1
            is_clean = False
        if agent.is_regular_user["cannabis"]:
            reg_cann += 1
            is_clean = False
        if agent.is_regular_user["cocaine"]:
            reg_coca += 1
            is_clean = False
        if agent.is_regular_user["opioid"]:
            reg_opio += 1
            is_clean = False

        if is_clean:
            clean += 1
    return {"alive": alive, "dead": dead,
            "addicted": {"amph": add_amph, "cann": add_cann, "coca": add_coca, "opio": add_opio},
            "regular": {"amph": reg_amph, "cann": reg_cann, "coca": reg_coca, "opio": reg_opio},
            "clean": clean}
