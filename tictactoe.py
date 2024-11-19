import sys
from minimax import MiniMax
import pygame
import time

EMPTY = 0
X = 1
O = -1
# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
grey = (128, 128, 128)

class TicTacToe:
	def __init__(self):
		# Pygame init
		pygame.init()
		self.size = self.width, self.height = 600, 400
		self.screen = pygame.display.set_mode(self.size)
		pygame.display.set_caption("Tic Tac Toe")

		# Fonts
		self.medium_font = pygame.font.Font(None, 36)
		self.large_font = pygame.font.Font(None, 48)

		# Game state
		self.reset_game()
		
	def reset_game(self):
		self.map = [EMPTY] * 9
		self.minimax = MiniMax(actions=self.actions, result=self.results, terminal=self.terminal, utility=self.utility)
		self.game_over = False
		self.user_turn = True
		self.winner = None
		self.winner_symbol = 'O'
	
	def player(self, state):
		x_count = sum(1 for cell in state if cell==X)
		o_count = sum(1 for cell in state if cell==O)
		return X if x_count < o_count else O

	def actions(self, state):
		possible_actions = list()
		for i, cell in enumerate(state):
			if cell == EMPTY:
				possible_actions.append(i)
		return possible_actions

	def results(self, state, action):
		new_state = state.copy()
		new_state[action] = self.player(state)
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
		return EMPTY not in state or self.checkWin(state) is not None
	
	def utility(self, state):
		return self.checkWin(state) or 0

	def putX(self, state):
		self.map[state] = X
	
	def putO(self, state):
		self.map[state] = O
	
	def draw_board(self):
		self.screen.fill(BLACK)

		# Draw grid
		tile_size = 80
		tile_origin = (
			self.width / 2 - (1.5 * tile_size),
			self.height / 2 - (1.5 * tile_size)
		)
		self.tiles = []

		for i in range(3):
			row = []
			for j in range(3):
				rect = pygame.Rect(
					tile_origin[0] + j * tile_size,
					tile_origin[1] + i * tile_size,
					tile_size, tile_size
				)
				pygame.draw.rect(self.screen, WHITE, rect, 3)

				# Draw X or O
				index = i * 3 + j
				if self.map[index] == X:
					text = self.large_font.render('X', True, WHITE)
				elif self.map[index] == O:
					text = self.large_font.render('O', True, WHITE)
				else:
					text = None
				
				if text:
					text_rect = text.get_rect(center=rect.center)
					self.screen.blit(text, text_rect)
				
				row.append(rect)
			self.tiles.append(row)
		
		# Draw game status
		if self.game_over:
			status = "Tie" if self.winner is None else f"{self.winner_symbol} Wins!"
		else:
			status = "Your Turn" if self.user_turn else "Computer's Turn"
		
		text = self.medium_font.render(status, True, WHITE)
		text_rect = text.get_rect(center=(self.width/2,50))
		self.screen.blit(text, text_rect)

		if self.game_over:
			self.new_game_button = pygame.Rect(
				self.width/2 - 100,
				self.height - 100,
				200,
				50
			)
			pygame.draw.rect(self.screen, WHITE, self.new_game_button)
			new_game_text = self.medium_font.render("New Game", True, BLACK)
			new_game_text_rect = new_game_text.get_rect(center=self.new_game_button.center)
			self.screen.blit(new_game_text, new_game_text_rect)

		pygame.display.flip()
	
	def handle_click(self, pos):
		for i in range(3):
			for j in range(3):
				if (self.map[i*3+j]==EMPTY and self.tiles[i][j].collidepoint(pos)):
					return i*3 + j
		return None

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
			while True:
				sys.stdout.write("Enter position from 0 to 8: \n")
				pos = int(sys.stdin.readline())
				if 0 <= pos <= 8 and self.map[pos] is EMPTY:
					break
			self.putO(pos)
			self.printMap()
			if self.terminal(self.map):
				break
			self.putX(self.minimax.solve(self.map))
			self.printMap()
	
	def run_game(self):
		clock = pygame.time.Clock()

		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				
				if event.type == pygame.MOUSEBUTTONDOWN:
					pos = pygame.mouse.get_pos()
					
					# Check for new game button
					if self.game_over and hasattr(self, 'new_game_button'):
						if self.new_game_button.collidepoint(pos):
							self.reset_game()
							continue

				if not self.game_over and not self.user_turn:
					# AI turn
					start_time = time.time()
					move = self.minimax.solve(self.map)
					end_time = time.time()
					timelapse = end_time - start_time
					print(f"Found solution in {timelapse:.4f} seconds")
					self.map[move] = X
					self.user_turn = True

					# Check game state after computer move
					if self.terminal(self.map):
						win = self.checkWin(self.map)
						self.game_over = True
						self.winner_symbol = "X" if win == X else "O"
				
				elif event.type == pygame.MOUSEBUTTONDOWN and self.user_turn and not self.game_over:
					# User turn
					pos = pygame.mouse.get_pos()
					move = self.handle_click(pos)
					if move is not None:
						self.map[move] = O
						self.user_turn = False
					
						# Check game state after player move
						if self.terminal(self.map):
							win = self.checkWin(self.map)
							self.game_over = True
							self.winner_symbol = "X" if win == X else "O"
			self.draw_board()
			clock.tick(60)



if len(sys.argv) != 1:
	sys.exit("Usage: python tictactoe.py")

if __name__ == "__main__":
	tictactoe = TicTacToe()
	tictactoe.run_game()