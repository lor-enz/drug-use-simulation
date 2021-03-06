from datetime import datetime
import pandas as pd
import plotly.express as px

our_plot_width = 600
our_plot_height = 400


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
        # deprecated results_df = results_df.append(append_df)
        results_df = pd.concat([results_df, append_df])

    # Unified save path without fileending
    path = f"{datetime.now().strftime('images/%Y%m%d_%H%M')}-{label}"

    # Save to pickle file
    results_df.to_pickle(f"{path.replace('images', 'pickles' )}.pickle")
    # Create plot
    fig = px.line(results_df, y=['alive', 'dead', 'clean'])
    fig.update_layout(width=our_plot_width,
                      height=our_plot_height,
                      xaxis_title="Simulation Cycles",
                      yaxis_title="Agents"
    )

    # Save base plot to file
    fig.write_image(f"{path}-base.png", engine="kaleido")

    # Create more plots. One for each substance
    plot_substance_helper_function(results_df, "amph", path)
    plot_substance_helper_function(results_df, "cann", path)
    plot_substance_helper_function(results_df, "coca", path)
    plot_substance_helper_function(results_df, "opio", path)


def plot_substance_helper_function(results_df, substance, pathname):
    fig = px.line(results_df, y=[f'reg_{substance}', f'add_{substance}'])
    fig.update_layout(width=our_plot_width,
                      height=our_plot_height,
                      xaxis_title="Simulation Cycles",
                      yaxis_title="Agents"
                      )
    path = f"{pathname}-{substance}.png"
    fig.write_image(path, engine="kaleido")
