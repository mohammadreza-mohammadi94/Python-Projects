import random

def generate_random_number(start, end):
    """Generate a random integer number within a specified range.

    Args:
        start (int): The lower bound of the range (inclusive).
        end (int): The upper bound of the range (inclusive).

    Returns:
        int: A random integer between start and end (inclusive).
    """
    return random.randint(start, end)