# main.py
from game_logic.num_generator import generate_random_number
from game_logic.hint import generate_hint
from game_logic.scorer import Scorer
from utils.input_validator import valid_user_input

def display_welcome_message():
    """Display the welcome message and game instructions."""
    print("Welcome to the Number Guessing Game! 🎮")
    print("I'm thinking of a number between 0 and 100.")
    print("Try to guess it in as few attempts as possible!")
    print("Your initial score is 100, and you'll lose 3 points for each wrong guess.")
    print("Type 'q' to quit the game at any time.\n")

def play_game():
    """Main game loop that handles the number guessing gameplay."""
    # Initialize game components
    secret_number = generate_random_number(0, 100)
    scorer = Scorer(initial_score=100)
    attempts = 1
    max_attempts = 10
    
    while attempts <= max_attempts:
        # Display current score
        print(f"\nCurrent Score: {scorer.get_score()}")
        
        try:
            # Get valid user input
            guess = valid_user_input(attempts)
            
            # Check if user wants to quit
            if guess is None:
                print("\nThanks for playing! 👋")
                break
            
            # Check if guess is correct
            if guess == secret_number:
                print(f"\n🎉 Congratulations! You've won!")
                print(f"The number was: {secret_number}")
                print(f"Final Score: {scorer.get_score()}")
                break
            
            # Provide hint and update score
            hint = generate_hint(guess, secret_number)
            print(hint)
            scorer.decrement_score()
            attempts += 1
            
            # Check if score is zero or max attempts reached
            if scorer.get_score() == 0 or attempts > max_attempts:
                print("\n😔 Game Over!")
                if scorer.get_score() == 0:
                    print("You've run out of points.")
                else:
                    print("You've run out of attempts.")
                print(f"The number was: {secret_number}")
                break
                
        except ValueError as e:
            print(f"Error: {e}")
            continue

def main():
    """Main function to run the number guessing game."""
    display_welcome_message()
    play_game()
    
    # Ask if player wants to play again
    while True:
        play_again = input("\nWould you like to play again? (y/n): ").lower()
        if play_again == 'y':
            print("\n" + "="*50 + "\n")
            play_game()
        elif play_again == 'n':
            print("\nThanks for playing! See you next time! 👋")
            break
        else:
            print("Please enter 'y' for yes or 'n' for no.")

if __name__ == "__main__":
    main()