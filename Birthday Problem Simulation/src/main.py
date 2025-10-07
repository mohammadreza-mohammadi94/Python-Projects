import random

def birthday_simulation(group_size=23, trials=1_000_000):
    """
    Simulates the birthday problem for a given group size and number of trials.

    Args:
        group_size (int): The number of people in the group.
        trials (int): The number of times to run the simulation.

    Returns:
        float: The probability of at least two people sharing a birthday.
    """
    # Variable to store the number of times a shared birthday is found
    same_birthday = 0
    # Run the simulation for the given number of trials
    for _ in range(trials):
        # Generate a list of random birthdays for the group
        birthdays = [random.randint(1, 365) for _ in range(group_size)]
        # Check if there are any duplicate birthdays in the list
        if len(birthdays) != len(set(birthdays)):
            # If there are duplicates, increment the counter
            same_birthday += 1
    # Calculate the probability of a shared birthday
    return same_birthday / trials


if __name__ == "__main__":
    # List of group sizes to simulate
    for n in [5, 10, 20, 23, 30, 50, 100]:
        # Run the simulation for each group size
        p = birthday_simulation(group_size=n)
        # Print the result
        print(f"Group of {n}: Probability of shared birthday: {p:.4f}")