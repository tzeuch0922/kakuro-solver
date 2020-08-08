from Kakuro_Square import Kakuro_Square
import sys

class Kakuro_Board:
	
	# Instantiate board
	def __init__(self, board):
		
		# Check to see if board is correct length
		if len(board) != 336:
			print("Board length error:")
			print("Board should be 336 in length, but it is currently " + str(len(board)) + " in length.")
			
		board = [0 if x == '' else int(x) if x.find('/') == -1 else x for x in board]
		
		self.board = []
		
		for val in board:
			self.board.append(Kakuro_Square(val))
			
	# Print Kakuro_Board
	def print_board(self):
		print(" _____________________________________________________________________")
		for y in range(0, 24):
			values = [self.get_square(x, y).get_value() for x in range(0, 14)]
			horizontal = [self.get_square(x, y).get_horizontal_sum() for x in range(0, 14)]
			vertical = [self.get_square(x, y).get_vertical_sum() for x in range(0, 14)]
			top = ['    ' if values[i] >= 0 else '\\  /' if values[i] == -1 else '\\   ' for i in range(0, 14)]
			mid = [' {:2d} '.format(values[i]) if values[i] > 0 else '    ' if values[i] == 0 else ' >< ' if values[i] == -1 else ' \\{:2d}'.format(horizontal[i]) for i in range(0, 14)]
			bot = ['____' if values[i] >= 0 else '/  \\' if values[i] == -1 else '{:2d}\\ '.format(vertical[i]) for i in range(0, 14)]
			print("|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|".format(*top))
			print("|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|".format(*mid).replace(' 0', '  '))
			print("|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|".format(*bot).replace(' 0', '  ').replace(' ', '_'))
		
	# Return list of relevant squares in row
	def squares_in_row(self, x, y):
		row = []
		if self.get_square(x, y).get_value() < 0:
			for i in range(1, x):
				if self.get_square(x - i, y).get_value() < 0:
					row.append(self.get_square(x - i, y))
				else:
					break
		for i in range(1, 14 - x):
			if self.get_square(x + i, y).get_value() < 0:
				row.append(self.get_square(x + i, y))
			else:
				break
		return row
	
	# Return list of relevant squares in column
	def squares_in_col(self, x, y):
		col = []
		if self.get_square(x, y).get_value() < 0:
			for i in range(1, y):
				if self.get_square(x, y - i).get_value() < 0:
					col.append(self.get_square(x, y - i))
				else:
					break
		for i in range(1, 24 - y):
			if self.get_square(x, y + i).get_value() < 0:
				col.append(self.get_square(x, y + i))
			else:
				break
		return col
		
	# Return kakuro square
	def get_square(self, x, y):
		#print("x: "+str(x)+", y: "+str(y)+")")
		return self.board[(y * 14) + x]
		
	# Function to check to see if current board is legal
	def is_legal(self):
		pass
		#implement later
		
	# Function to check to see if current board is legal
	def is_finished(self):
		pass
		#implement later