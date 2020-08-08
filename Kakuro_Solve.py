from Kakuro_Board import Kakuro_Board
import csv
import argparse

# Return csv items in a list
def read_csv_to_list(file_name):
	list = []
	with open(file_name, newline = '') as csvfile:
		reader = csv.reader(csvfile, quotechar = '|')
		for row in reader:
			for item in row:
				list.append(item)
	return list

if __name__ == "__main__":
	# Command-line arguments
	parser = argparse.ArgumentParser("Solves a sudoku problem indicated in a csv file.")
	parser.add_argument("-f", "--file_name", action = "store", help = "Name of csv file for input.", required = True)
	options = parser.parse_args()
	
	Kakuro_Problem = Kakuro_Board(read_csv_to_list(options.file_name))
	Kakuro_Problem.print_board()