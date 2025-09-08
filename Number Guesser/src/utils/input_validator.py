
def valid_user_input(current_attempt):
    """
    Prompts the user to input a number within a specified range (0 to 100) 
    and validates the input. The user has a maximum of 10 attempts to provide 
    valid input. If the user enters "q" (case-insensitive), the function exits 
    early.
    Args:
        current_attempt (int): The current attempt number
    Returns:
        int: A valid integer input from the user within the range 0 to 100.
    Raises:
        ValueError: If the input is not an integer or is outside the valid range.
    Notes:
        - If the user enters "q", the function will terminate without returning a value.
        - Invalid inputs will display an error message and prompt the user again.
    """
    MAX_ATTEMPTS = 10
    # Get user-input (user guess)
    while current_attempt <= MAX_ATTEMPTS:
        user_input = input(f"Attempts {current_attempt}/{MAX_ATTEMPTS}. Enter your guess: ")

        # check if user asks to quit from game
        if isinstance(user_input, str) and user_input.lower() == "q":
            break
        
        try:
            # convert to int
            num = int(user_input)
            
            # check range
            if num < 0 or num > 100:
                raise ValueError("Number must be between 0 and 100.")
            
            return num
        except ValueError:
            print("Invalid input, please enter valid integer between 0 to 100")