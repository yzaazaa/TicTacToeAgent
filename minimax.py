class MiniMax():
	def __init__(self, actions, result, terminal, utility, alpha_beta_pruning=True):
		self.actions = actions
		self.result = result
		self.terminal = terminal
		self.utility = utility
		self.alpha_beta_pruning = alpha_beta_pruning
	
	def minValue(self, state, alpha, beta):
		if self.terminal(state):
			return self.utility(state)
		v = float("inf")
		for action in self.actions(state):
			v = min(v, self.maxValue(self.result(state, action), alpha, beta))
			if self.alpha_beta_pruning:
				if v <= alpha:
					return v
				beta = min(beta, v)
		return v
	
	def maxValue(self, state, alpha, beta):
		if self.terminal(state):
			return self.utility(state)
		v = float("-inf")
		for action in self.actions(state):
			v = max(v, self.minValue(self.result(state, action), alpha, beta))
			if self.alpha_beta_pruning:
				if v >= beta:
					return v
				alpha = max(alpha, v)
		return v

	def solve(self, state):
		max_score = float("-inf")
		beta = float("inf")
		alpha = max_score
		best_move = None
		for action in self.actions(state):
			result = self.result(state, action)
			current_score = self.minValue(result, alpha, beta)
			if current_score > max_score:
				max_score = current_score
				best_move = action
			if self.alpha_beta_pruning:
				alpha = max(alpha, current_score)
		return best_move