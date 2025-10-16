import random


class TicTacToe:
    """
    A class representing the Tic-Tac-Toe game.
    Manages the game board, player turns, and game logic.
    """
    
    def __init__(self):
        """
        Initialize the game with an empty board and random first player.
        The board is represented as a list of 10 elements (0 is ignored for easier indexing).
        Each cell contains either 'X', 'O', or ' ' (empty).
        """
        self.board = [' '] * 10  # We use 1-9 for convenience, 0 is ignored
        self.player_turn = self.get_random_first_player()

    def get_random_first_player(self):
        """
        Randomly choose which player goes first ('X' or 'O').
        Returns:
            str: 'X' or 'O' representing the first player
        """
        return 'X' if random.randint(0, 1) == 0 else 'O'

    def fix_spot(self, cell, player):
        """
        Place a player's mark ('X' or 'O') in the specified cell.
        Args:
            cell (int): The cell number (1-9) where the mark should be placed
            player (str): The player's mark ('X' or 'O')
        """
        self.board[cell] = player

    def has_player_won(self, player):
        """
        Check if the specified player has won the game.
        Args:
            player (str): The player to check for win ('X' or 'O')
        Returns:
            bool: True if the player has won, False otherwise
        """
        # All possible winning combinations (rows, columns, and diagonals)
        win_combinations = [(1, 2, 3), (4, 5, 6), (7, 8, 9),  # Rows
                            (1, 4, 7), (2, 5, 8), (3, 6, 9),  # Columns
                            (1, 5, 9), (3, 5, 7)]             # Diagonals
        # Check each winning combination
        for combination in win_combinations:
            if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] == player:
                return True
        return False

    def is_board_filled(self):
        """
        Check if the game board is completely filled.
        Returns:
            bool: True if no empty spaces remain, False otherwise
        """
        return ' ' not in self.board

    def swap_player_turn(self):
        """
        Switch the turn between players.
        Changes player_turn from 'X' to 'O' or vice versa.
        """
        self.player_turn = 'X' if self.player_turn == 'O' else 'O'

    def show_board(self):
        """
        Display the current state of the game board.
        Prints the board as a 3x3 grid with current player marks.
        """
        print("\n")
        # Create rows by grouping board elements into lists of 3
        rows = [[self.board[i+j] for i in range(1, 4)] for j in range(0, 7, 3)]
        for row in rows:
            print(row)
        print("\n")

    def start(self):
        """
        Start and manage the main game loop.
        Handles player input, turn management, and game end conditions.
        The game continues until there's a winner or a draw.
        """
        while True:
            # Display current board state
            self.show_board()
            try:
                # Get player input for cell number (1-9)
                cell = int(input(f"Player {self.player_turn}, Enter the cell number: "))

                # Validate move: cell must be in range 1-9 and empty
                if cell in range(1, 10) and self.board[cell] == ' ':
                    # Place player's mark in the chosen cell
                    self.fix_spot(cell, self.player_turn)

                    # Check for win condition
                    if self.has_player_won(self.player_turn):
                        print(f"Player {self.player_turn} wins!")
                        break

                    # Check for draw condition
                    if self.is_board_filled():
                        print("It's a Draw!")
                        break

                    # Switch to other player's turn
                    self.swap_player_turn()

                else:
                    print("Invalid input, please try again.")
            except ValueError:
                print("Invalid input, please enter a number between 1 and 9.")


if __name__ == "__main__":
    # Create a new instance of the TicTacToe game and start playing
    # The game will continue until there's a winner or a draw
    game = TicTacToe()
    game.start()
