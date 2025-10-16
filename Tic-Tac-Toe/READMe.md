# Tic-Tac-Toe Game

A simple command-line implementation of the classic Tic-Tac-Toe game in Python. This game allows two players to play against each other, taking turns to mark spaces on a 3x3 grid.

## Features

- Random selection of first player
- Interactive command-line interface
- Visual representation of the game board
- Input validation and error handling
- Win and draw detection
- Easy-to-understand game flow

## Requirements

- Python 3.x
- No additional packages required

## How to Play

1. Run the game:

   ```bash
   python src/main.py
   ```

2. The game will randomly select which player ('X' or 'O') goes first.

3. When prompted, enter a number between 1-9 to place your mark on the board:

   ```
   1 2 3
   4 5 6
   7 8 9
   ```

4. Players take turns until one wins or the game ends in a draw.

## Game Rules

- Players take turns placing their marks ('X' or 'O') on empty spaces
- The first player to get three of their marks in a row (horizontally, vertically, or diagonally) wins
- If all spaces are filled and no player has won, the game ends in a draw

## Implementation Details

The game is implemented using a `TicTacToe` class that manages:

- Game board representation
- Player turn management
- Move validation
- Win condition checking
- Board visualization

### Board Representation

The game board is represented as a list of 10 elements (index 0 is ignored for easier input mapping):

- Empty spaces are represented by ' ' (space)
- Player marks are represented by 'X' and 'O'
- Board positions are numbered 1-9, corresponding to:
  ```
  [1] [2] [3]
  [4] [5] [6]
  [7] [8] [9]
  ```

## Error Handling

The game includes error handling for:

- Invalid input types (non-numeric values)
- Out-of-range inputs (numbers not between 1-9)
- Already occupied positions

## Contributing

Feel free to fork this repository and submit pull requests for any improvements you'd like to make.
