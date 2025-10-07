import random

def monty_hall_game(switch_doors):
    """
    Simulates a single round of the Monty Hall game.

    Args:
        switch_doors (bool): True if the player wants to switch doors, False otherwise.

    Returns:
        bool: True if the player wins the car, False otherwise.
    """
    # Initialize the doors with two goats and a car
    doors =['car', 'goat', 'goat']
    # Shuffle the doors to randomize the position of the car
    random.shuffle(doors)
    # Player makes an initial choice
    initial_choice = random.choice(range(3))
    # Host reveals a door with a goat that was not chosen by the player
    doors_revealed = [i for i in range(3) if i != initial_choice and doors[i] != 'car']
    door_revealed = random.choice(doors_revealed)
    
    # Player decides whether to switch doors or not
    if switch_doors:
        # If the player switches, their final choice is the remaining door
        final_choice = [i for i in range(3) if i != initial_choice and i != door_revealed][0]
    else:
        # If the player does not switch, their final choice is their initial choice
        final_choice = initial_choice
    
    # Return True if the final choice is the car, False otherwise
    return doors[final_choice] == 'car'


def simulate_game(trials):
    """
    Simulates the Monty Hall game for a given number of trials.

    Args:
        trials (int): The number of times to simulate the game.

    Returns:
        tuple: A tuple containing the winning percentage without switching and with switching.
    """
    # Calculate the number of wins without switching
    num_wins_without_switching = sum([monty_hall_game(False) for _ in range(trials)])
    # Calculate the number of wins with switching
    num_wins_with_switching = sum([monty_hall_game(True) for _ in range(trials)])
    # Calculate the winning percentage for both cases
    return num_wins_without_switching / trials, num_wins_with_switching / trials


if __name__ == "__main__":
    # Number of trials to simulate
    trials = 10000
    # Simulate the game and get the winning percentages
    win_percentage_no_switch, win_percentage_switch = simulate_game(trials)
    # Print the results
    print(f"Winning percentage without switching doors: {(win_percentage_no_switch):.2%}")
    print(f"Winning percentage with    switching doors: {(win_percentage_switch):.2%}")