class MiniMax():
	def __init__(self, actions, result, terminal, utility):
		self.actions = actions
		self.result = result
		self.terminal = terminal
		self.utility = utility
	
	def minValue(self, state, depth=0):
		if self.terminal(state):
			return self.utility(state)
		v = float("inf")
		for action in self.actions(state):
			v = min(v, self.maxValue(self.result(state, action), depth+1))
		return v
	
	def maxValue(self, state, depth=0):
		if self.terminal(state):
			return self.utility(state)
		v = float("-inf")
		for action in self.actions(state):
			v = max(v, self.minValue(self.result(state, action), depth+1))
		return v

	def solve(self, state):
		v = float("-inf")
		ret = None
		for action in self.actions(state):
			result = self.result(state, action)
			min_value = self.minValue(result, 1)
			if min_value > v:
				v = min_value
				ret = action
		return ret