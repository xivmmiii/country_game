if answer_state == 'exit':
    missing_states = [states for states in all_states if states not in guessed_states]
    new_data = pandas.DataFrame(missing_states)
    new_data.to_csv("missing_states.csv")
