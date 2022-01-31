

def convert_agents_to_df(agents):
    import pandas as pd
    column_names = ["is_alive", "gender", "regular_user", "addicted", "usage_history"]
    df = pd.DataFrame(columns=column_names)
    size_for_progress_bar = len(agents)
    # Inefficient with 100000 this presumably takes over half an hour
    counter = 0
    for agent in agents:
        df = df.append({'is_alive': agent.alive, 'gender': agent.gender, 'regular_user': agent.is_regular_user,
                        'addicted': agent.addicted, 'usage_history': agent.usage_history}, ignore_index=True)
        # Just for the progress bar:
        counter = counter + 1
        if counter % (max(int(size_for_progress_bar / 20), 1)) == 0:
            print(f'{int((counter / size_for_progress_bar) * 100)}% of df conversion done')
    return df


def how_many_are_alive(agents_df):
    result = agents_df.is_alive.value_counts(normalize=True)
    print(f'Result is: {result}')
    return result


def how_many_are_addicted(agents_df):
    result = agents_df.addicted.value_counts(normalize=True)
    print(f'Result is: {result}')
    return result





