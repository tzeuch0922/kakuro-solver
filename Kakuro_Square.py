class Kakuro_Square:

	# Instantiate Square
	def __init__(self, value):
		if type(value) is str:
			self.vertical_sum = int(value[:value.find('/')])
			self.horizontal_sum = int(value[value.find('/') + 1:])
			self.value = -2
			self.possible_values = []
		elif value == -1:
			self.vertical_sum = 0
			self.horizontal_sum = 0
			self.value = -1
			self.possible_values = []
		else:
			self.vertical_sum = 0
			self.horizontal_sum = 0
			self.value = 0
			self.possible_values = list(range(1, 10))
			
	# Remove value from possible_values list and set value if only one possible value exists
	def remove_possible_value(self, num):
		self.possible_values.remove(num)
		if len(self.possible_values) == 1:
			self.set_value(self.possible_values[0])
			
	# Set value and replace possible_values
	def set_value(self, num):
		if self.value == 0:
			self.value = num
			self.possible_values.clear()
			self.possible_values.append(num)
		elif self.value < 0:
			print("Can't set value of these spaces.")
		elif self.value > 0:
			print("Changing already set value.")
			self.value = num
			self.possible_values.clear()
			self.possible_values.append(num)
			
	# Get value of square
	def get_value(self):
		return self.value
		
	# Get possible_values of square
	def get_possible_values(self):
		return self.possible_values
		
	# Get horizontal_sum
	def get_horizontal_sum(self):
		return self.horizontal_sum
	
	# Get vertical_sum
	def get_vertical_sum(self):
		return self.vertical_sum