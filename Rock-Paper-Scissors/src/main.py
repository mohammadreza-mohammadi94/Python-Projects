import random
from typing import List

# Define class for game
class RockPaperScissors:
    """Class to represent a Rock-Paper-Scissors game."""
    def __init__(self):
        self.choices: List[str] = ["rock", "paper", "scissors"]
    
    def get_user_choice(self) -> str:
        """
        Method to get user's choice.
        
        returns:
            - user's chpoice as a string
        """
        user_choice: str = input("Enter Rock, Paper, or Scissors: ").lower()
        if user_choice not in self.choices:
            print("Invalid choice! Please choose Rock, Paper, or Scissors.")
            return self.get_user_choice()
        return user_choice

    def get_computer_choice(self) -> str:
        """
        Method to get computer's choice.
        
        returns:
            - computer's choice as a string
        """
        return random.choice(self.choices)
    
    def decide_winner(self, user_choice: str, computer_choice: str) -> str:
        """
        Method to decide the winner.
        
        returns:
            - winner as a string
        """
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
                 return "Congrats, You won!"
        else:
            return "Computer won! Better luck next time."
        
    def play(self):
        """method to play the game."""
        user_choice: str = self.get_user_choice()
        computer_choice: str = self.get_computer_choice()
        print(f"User choice: {user_choice}\t Computer choice: {computer_choice}")
        print(self.decide_winner(user_choice, computer_choice))

if __name__ == "__main__":
    game = RockPaperScissors()  
    while True:
        game.play()
        continue_game = input("Do you want to play again? (Enter any key to contunue and 'q' to quit): ").lower()
        if continue_game == 'q':
            print("Thanks for playing! Goodbye!")
            break