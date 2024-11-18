EMPTY = 0
X = 1
O = -1

class MiniMax():
	def __init__(self, actions, result, terminal, utility):
		self.actions = actions
		self.result = result
		self.terminal = terminal
		self.utility = utility
	
	def minValue(self, state):
		v = float("inf")
		if self.terminal(state):
			self.printMap(state)
			return self.utility(state)
		for action in self.actions(state):
			v = min(v, self.maxValue(self.result(state, action)))
		return v
	
	def maxValue(self, state):
		v = float("-inf")
		if self.terminal(state):
			self.printMap(state)
			return self.utility(state)
		for action in self.actions(state):
			v = max(v, self.minValue(self.result(state, action)))
		return v

	def printMap(self, state, first=False):
		if first:
			for i in range(3):
				row = [str(i*3 + j) for j in range(3)]
				print(f" {row[0]} | {row[1]} | {row[2]} ")
				if i < 2:
					print("---+---+---")
		else:
			symbols = {EMPTY: ' ', X: 'X', O: 'O'}
			for i in range(3):
				row = state[i*3:(i+1)*3]
				print(f" {symbols[row[0]]} | {symbols[row[1]]} | {symbols[row[2]]} ")
				if i < 2:
					print("---+---+---")

	def solve(self, state):
		v = float("-inf")
		ret = None
		for action in self.actions(state):
			result = self.result(state, action)
			min_value = self.minValue(result)
			if min_value > v:
				v = min_value
				ret = action
		return ret