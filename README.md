# TicTacToe AI with Minimax and Alpha-Beta Pruning

An unbeatable Tic-Tac-Toe AI agent implemented using the Minimax algorithm with Alpha-Beta pruning optimization. The game features a graphical user interface built with Pygame, allowing players to compete against a perfect AI opponent.

## Features

- Unbeatable AI opponent using Minimax algorithm
- Alpha-Beta pruning optimization for faster decision making
- Interactive GUI with Pygame
- Real-time game state visualization
- Performance metrics tracking

## Performance Benchmarks

### Without Alpha-Beta Pruning:
- Initial move: 443.6ms
- Mid-game: 7.9ms
- Late game: 0.4ms
- Final moves: 0.1ms

### With Alpha-Beta Pruning:
- Initial move: 26.1ms (94% performance improvement)
- Mid-game: 3.0ms
- Late game: 0.3ms
- Final moves: 0.1ms

## Requirements

- Python 3.6+
- Pygame

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yzaazaa/TicTacToeAgent
cd TicTacToeAgent
python3 -m venv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate`
```

2. Install Dependencies

```bash
pip install -r requirements.txt
```
3. Run the script:
```bash
python tictactoe.py
```

## Project Structure

```
tictactoe-ai/
├── tictactoe.py      # Main game logic and GUI
├── minimax.py        # Minimax implementation with Alpha-Beta pruning
└── README.md
```

## How It Works

### Minimax Algorithm
The AI uses the Minimax algorithm to determine the best possible move by:
1. Exploring all possible game states
2. Evaluating each terminal state
3. Backing up values through the game tree
4. Choosing the move that leads to the best guaranteed outcome

### Alpha-Beta Pruning
Optimizes the Minimax algorithm by:
- Maintaining upper (beta) and lower (alpha) bounds for each node
- Pruning branches that cannot affect the final decision
- Significantly reducing the number of nodes explored

### GUI
The Pygame interface provides:
- Clear visualization of the game board
- Mouse-based move selection
- Game state information display
- New Game option after completion

## Controls

- Mouse Click: Make a move
- Click "New Game" button to restart after game ends

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Acknowledgments

- Pygame community for the excellent gaming library
- CS50's AI course for inspiration on game theory implementation