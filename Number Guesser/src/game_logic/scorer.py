class Scorer:
    """A class to manage the scoring system for the number guessing game.
    
    The scorer starts with an initial score and can be decremented with penalties.
    The score will never go below zero.
    
    Attributes:
        score (int): The current score of the player.
    """
    
    def __init__(self, initial_score=100):
        """Initialize the Scorer with a starting score.
        
        Args:
            initial_score (int, optional): The starting score for the player. 
                Defaults to 100.
        """
        # Set the initial score for the game
        self.score = initial_score
        
    def decrement_score(self, penalty=3):
        """Decrease the current score by the penalty amount.
        
        The score will not go below zero, even if the penalty would make it negative.
        
        Args:
            penalty (int, optional): The amount to decrease the score by. 
                Defaults to 3.
        """
        # Subtract the penalty from the current score
        self.score -= penalty
        # Ensure score doesn't go below zero
        self.score = max(self.score, 0)
    
    def get_score(self):
        """Get the current score.
        
        Returns:
            int: The current score value.
        """
        return self.score
        