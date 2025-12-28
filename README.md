# TIC TAC TOE using Minimax algorithm

    GUI built with Tkinter.
    Python implementation.
    AI opponent using the Minimax algorithm.

## Logic Overview

### The Minimax Algorithm

    The AI (O) is the Maximizer, wanting a score of +1.
    The Human (X) is the Minimizer, wanting a score of -1.
    A Draw will be counted as 0.

### The difficulty can be adjusted

    Easy: more chance the AI moves randomly, less chance it uses Minimax.

    Medium: less chance the AI moves randomly, more chance it uses Minimax.

    Hard : 100% chance it uses Minimax.


## Code Structure

TicTacToePro (Class): Handles the GUI lifecycle and event loop.

human_move(): Captures button click events and validates available moves.

ai_move(): toggles between random and Minimax logic.

minimax(): simulates game states.

check_win_logic(): to verify 8 possible win conditions.

# How to run

### 1.Clone the repo

git clone https://github.com/aswathy1807/tictactoe.git

### 2. Go to directory

cd tictactoe

### 3. execute

python game.py


