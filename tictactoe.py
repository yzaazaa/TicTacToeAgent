import sys
from minimax import MiniMax

EMPTY = 0
X = 1
O = -1

class TicTacToe:
	def __init__(self):
		self.map = [EMPTY] * 9
		self.minimax = MiniMax(actions=self.actions, result=self.results, terminal=self.terminal, utility=self.utility)
	
	def actions(self, state):
		possible_actions = list()
		for i, cell in enumerate(state):
			if cell == EMPTY:
				possible_actions.append(i)
		return possible_actions

	def results(self, state, action):
		new_state = state.copy()
		new_state[action] = X
		return new_state
	
	def checkWin(self, state):
		x_pattern = sum(1 << i for i, val in enumerate(state) if val == X)
		o_pattern = sum(1 << i for i, val in enumerate(state) if val == O)

		winning_patterns = (
			0b111000000, # Top row
			0b000111000, # Middle row
			0b000000111, # Bottom row
			0b100100100, # Left column
			0b010010010, # Middle column
			0b001001001, # Right column
			0b100010001, # Diagonal
			0b001010100, # Anti-diagonal
		)

		for pattern in winning_patterns:
			if pattern & x_pattern == pattern:
				return X
			if pattern & o_pattern == pattern:
				return O
		return None

	
	def terminal(self, state):
		return EMPTY not in state or self.checkWin(state)
	
	def utility(self, state):
		return self.checkWin(state)

	def putX(self, state):
		self.map[state] = X
	
	def putO(self, state):
		self.map[state] = O
	
	def printMap(self, first=False):
		if first:
			for i in range(3):
				row = [str(i*3 + j) for j in range(3)]
				sys.stdout.write(f" {row[0]} | {row[1]} | {row[2]} \n")
				if i < 2:
					sys.stdout.write("---+---+---\n")
		else:
			symbols = {EMPTY: ' ', X: 'X', O: 'O'}
			for i in range(3):
				row = self.map[i*3:(i+1)*3]
				sys.stdout.write(f" {symbols[row[0]]} | {symbols[row[1]]} | {symbols[row[2]]} \n")
				if i < 2:
					sys.stdout.write("---+---+---\n")

	def run(self):
		self.printMap(first=True)
		while not self.terminal(self.map):
			sys.stdout.write("Enter position from 0 to 8: \n")
			pos = int(sys.stdin.readline())
			self.putO(pos)
			self.printMap()
			self.putX(self.minimax.solve(self.map))
			self.printMap()


if len(sys.argv) != 1:
	sys.exit("Usage: python tictactoe.py")

tictactoe = TicTacToe()
tictactoe.run()