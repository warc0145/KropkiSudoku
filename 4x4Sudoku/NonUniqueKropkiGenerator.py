'''
Name: Dylan Warcholik

File Name: NonUniqueKropkiGenerator.py

Date Started: 5/20/25 

Description:
These functions allow me to produce a Kropki Arrangement for all 4x4 Sudoku boards and answer several counting questions, including 
how many 4x4 solutions have a unique Kropki Arrangement, what is the highest and lowest number of circles in a Kropkri Arrangement,
and how many puzzles have a given number of circles in a Kropki Arrangement.

This version is a copy of KropkiGenerator4x4.py, but it marks the space between cells with a 1,2 with a white dot instead of a black dot.
This leads to 8 arrangements being non-unique, and this version is used for the NonUniqueGenerator4x4.py
I removed the max and min functions from this version because they are not needed.
'''
from SudokuPuzzleGenerator4x4 import solutions, print_board

# print(solutions)

def find_horizontal_kropki_dots(board):
    '''
    Searches a given board and returns a 4x3 array representing horizontal kropki dot placements (1 for black, -1 for white, 0 for no dot)
    Note, currently the circles between 1 and 2 are always white.
    '''
    horizontal_dots = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

    for r in range(len(board)):
        for c in range(len(board[r]) - 1): # This will compare 0,1 1,2 and 2,3 without exceeding array bounds
            if (abs(board[r][c] - board[r][c+1]) == 1): # If the absolute difference of adjacent cells is 1...
                horizontal_dots[r][c] = -1
            elif (board[r][c] / board[r][c+1] == 2 or board[r][c+1] / board[r][c] == 2): # If adjacent cells are a scale factor of 2...
                horizontal_dots[r][c] = 1
    return horizontal_dots

def find_vertical_kropki_dots(board):
    '''
    Searches a given board and returns a 3x4 array representing vertical kropki dot placements (1 for black, -1 for white, 0 for no dot)
    Note, currently the circles between 1 and 2 are always white.
    '''
    vertical_dots = [[0, 0, 0, 0], [0, 0, 0, 0,], [0, 0, 0, 0]]
    for r in range(len(board) - 1):
        for c in range(len(board[r])):
            if (abs(board[r][c] - board[r+1][c]) == 1): # If the absolute difference of adjacent cells is 1...
                vertical_dots[r][c] = -1
            elif (board[r][c] / board[r+1][c] == 2 or board[r+1][c] / board[r][c] == 2): # If adjacent cells are a scale factor of 2...
                vertical_dots[r][c] = 1
        
    return vertical_dots

def all_kropki_numbers(board_list):
    """
    Returns a dictionary counting all Kropki arrangements, where the key is the number of dots and the value is the number of puzzles with that many dots
    """
    kropki_numbers = dict()

    for board in board_list:
        vert_num_temp = 0
        horiz_num_temp = 0
        horiz_kropki_temp = find_horizontal_kropki_dots(board)
        vert_kropki_temp = find_vertical_kropki_dots(board)
        
        # Count the number of horizontal kropki dots:
        for row in horiz_kropki_temp:
            for col in row:
                if col != 0:
                    horiz_num_temp += 1
        # Count the number of vertical kropki dots:
        for row in vert_kropki_temp:
            for col in row:
                if col != 0:
                    vert_num_temp += 1
        
        temp_total = horiz_num_temp + vert_num_temp

        # If the total is already in the dictionary, increment the count by one, otherwise, add a count of 1 for that value
        if temp_total in kropki_numbers:
            kropki_numbers[temp_total] += 1
        else:
            kropki_numbers[temp_total] = 1

    print(kropki_numbers)

# all_kropki_numbers(solutions)

non_unique_kropki_solutions = []
def all_kropki_solutions(board_list):
    """
    This function will append to the existing list, non_unique_kropki_solutions, a tuple of horizontal dots and vertical dots (which are each two dimensional arrays)
    Then, we will examine non_unique_kropki_solutions to check for uniqueness by counting repeating arrangements
    """
    non_unique_count = 0
    for board in board_list:
        non_unique_kropki_solutions.append((find_horizontal_kropki_dots(board), find_vertical_kropki_dots(board)))
    
    for i in range(len(non_unique_kropki_solutions)):
        if non_unique_kropki_solutions.count(non_unique_kropki_solutions[i]) > 1:
            non_unique_count +=1
            # print("The arrangement:")
            # print(non_unique_kropki_solutions[i])
            # print("Appears", non_unique_kropki_solutions.count(non_unique_kropki_solutions[i]), "times. Here is the current board with the arrangement:")
            # print_board(board_list[i])
    print("Total non-unique arrangements:", non_unique_count)

all_kropki_solutions(solutions)
# print(non_unique_kropki_solutions[3])
