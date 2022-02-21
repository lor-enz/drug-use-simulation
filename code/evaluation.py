from datetime import datetime

import matplotlib.pyplot as plt

import pandas as pd
import matplotx

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


def create_plot(label, results):
    our_columns = ['alive', 'dead', 'clean', 'reg_amph', 'reg_cann', 'reg_coca', 'reg_opio', 'add_amph', 'add_cann',
                   'add_coca', 'add_opio']
    results_df = pd.DataFrame([], columns=our_columns)
    for row in results:
        newline = []

        newline.append(row["alive"])
        newline.append(row["dead"])
        newline.append(row["clean"])

        newline.append(row["regular"]["amph"])
        newline.append(row["regular"]["cann"])
        newline.append(row["regular"]["coca"])
        newline.append(row["regular"]["opio"])

        newline.append(row["addicted"]["amph"])
        newline.append(row["addicted"]["cann"])
        newline.append(row["addicted"]["coca"])
        newline.append(row["addicted"]["opio"])

        append_df = pd.DataFrame([newline], columns=our_columns, index=[row["cycle"]])
        results_df = results_df.append(append_df)


    with plt.style.context(matplotx.styles.dufte):
        plot = results_df.plot(figsize=(12, 7), y=['alive', 'clean', 'dead'])
        fig = plot.get_figure()
        fig.savefig(f"{datetime.now().strftime('%Y%m%d_%H%M')}#-base->{label}.png")

    plot_substance_helper_function(label, results_df, "amph")
    plot_substance_helper_function(label, results_df, "cann")
    plot_substance_helper_function(label, results_df, "coca")
    plot_substance_helper_function(label, results_df, "opio")



def plot_substance_helper_function(label, results_df, substance):
    with plt.style.context(matplotx.styles.dufte):
        plot = results_df.plot(figsize=(12, 7), y=[f'reg_{substance}', f'add_{substance}'])
        fig = plot.get_figure()
        fig.savefig(f"{datetime.now().strftime('%Y%m%d_%H%M')}#-{substance}->{label}.png")