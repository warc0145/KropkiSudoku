'''
Name: Dylan Warcholik

File Name: KropkiGenerator4x4.py

Date Started: 5/20/25 (pulled from SudokuPuzzleGenerator4x4.py)

Description:
These functions allow me to produce a Kropki Arrangement for all 4x4 Sudoku boards and answer several counting questions, including 
how many 4x4 solutions have a unique Kropki Arrangement, what is the highest and lowest number of circles in a Kropkri Arrangement,
and how many puzzles have a given number of circles in a Kropki Arrangement,
'''
from SudokuPuzzleGenerator4x4 import solutions, print_board

print(solutions)

def find_horizontal_kropki_dots(board):
    '''
    Searches a given board and returns a 4x3 array representing horizontal kropki dot placements (1 for black, -1 for white, 0 for no dot)
    Note, currently the circles between 1 and 2 are always black.
    '''
    horizontal_dots = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

    for r in range(len(board)):
        for c in range(len(board[r]) - 1): # This will compare 0,1 1,2 and 2,3 without exceeding array bounds
            if ((board[r][c] == 1 and board[r][c+1] == 2) or (board[r][c] == 2 and board[r][c+1] == 1)): # Grey circles (1,2 combo)
                horizontal_dots[r][c] = 1
            elif (abs(board[r][c] - board[r][c+1]) == 1): # If the absolute difference of adjacent cells is 1...
                horizontal_dots[r][c] = -1
            elif (board[r][c] / board[r][c+1] == 2 or board[r][c+1] / board[r][c] == 2): # If adjacent cells are a scale factor of 2...
                horizontal_dots[r][c] = 1
    return horizontal_dots

def find_vertical_kropki_dots(board):
    '''
    Searches a given board and returns a 3x4 array representing vertical kropki dot placements (1 for black, -1 for white, 0 for no dot)
    Note, currently the circles between 1 and 2 are always black.
    '''
    vertical_dots = [[0, 0, 0, 0], [0, 0, 0, 0,], [0, 0, 0, 0]]
    for r in range(len(board) - 1):
        for c in range(len(board[r])):
            if ((board[r][c] == 1 and board[r+1][c] == 2) or (board[r][c] == 2 and board[r+1][c] == 1)): # Grey circles (1,2 combo)
                vertical_dots[r][c] = 1
            elif (abs(board[r][c] - board[r+1][c]) == 1): # If the absolute difference of adjacent cells is 1...
                vertical_dots[r][c] = -1
            elif (board[r][c] / board[r+1][c] == 2 or board[r+1][c] / board[r][c] == 2): # If adjacent cells are a scale factor of 2...
                vertical_dots[r][c] = 1
        
    return vertical_dots


def maximum_kropki(board_list):
    '''
    This function will take in all 4x4 boards and identify which has the highest number of kropki dots present
    '''
    total_opt = 0 # Number of boards with maximum number of dots
    max_dots = 0 # Default number of dots
    best_board = None # Default board
    vert_kropki_temp = None
    best_horiz = 0
    horiz_kropki_temp = None
    best_vert = 0

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

        if max_dots < (horiz_num_temp + vert_num_temp):
            best_horiz = horiz_num_temp
            best_vert = vert_num_temp
            max_dots = best_horiz + best_vert
            best_board = board
            total_opt = 1
        elif max_dots == (horiz_num_temp + vert_num_temp):
            # print("The following board...")
            # print_board(board)
            # print("Has", max_dots, "Kropki dots")
            total_opt += 1 
    
    print("There are", total_opt, "optimal boards")
    print("The optimum board has", max_dots, "Kropki dots;", best_horiz, "horizontal dots and", best_vert, "vertical dots")
    print("Printing board...")
    print_board(best_board)


# maximum_kropki(solutions)


def minimum_kropki(board_list):
    '''
    This function will take in all 4x4 boards and identify which has the lowest number of kropki dots present
    '''
    total_opt = 0 # Number of boards with minimum number of dots
    min_dots = 24 # Hypothetical maximum number of dots
    best_board = None # Default board
    vert_kropki_temp = None
    lowest_horiz = 0
    horiz_kropki_temp = None
    lowest_vert = 0

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

        if min_dots > (horiz_num_temp + vert_num_temp):
            lowest_horiz = horiz_num_temp
            lowest_vert = vert_num_temp
            min_dots = lowest_horiz + lowest_vert
            best_board = board
            total_opt = 1
        elif min_dots == (horiz_num_temp + vert_num_temp):
            # print("The following board...")
            # print_board(board)
            # print("Has", min_dots, "Kropki dots")
            total_opt += 1 
    
    print("There are", total_opt, "minumum boards")
    print("The minuimum board has", min_dots, "Kropki dots;", lowest_horiz, "horizontal dots and", lowest_vert, "vertical dots")
    print("Printing board...")
    print_board(best_board)

# minimum_kropki(solutions)

def all_kropki_numbers(board_list):
    '''
    Returns a dictionary counting all Kropki arrangements, where the key is the number of dots and the value is the number of puzzles with that many dots
    '''
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

kropki_solutions = []
def all_kropki_solutions(board_list):
    '''
    This function will append to the existing list, kropki_solutions, a tuple of horizontal dots and vertical dots (which are each two dimensional arrays)
    Then, we will examine kropki_solutions to check for uniqueness by counting repeating arrangements
    '''
    non_unique_count = 0
    for board in board_list:
        kropki_solutions.append((find_horizontal_kropki_dots(board), find_vertical_kropki_dots(board)))
    
    for i in range(len(kropki_solutions)):
        if kropki_solutions.count(kropki_solutions[i]) > 1:
            non_unique_count +=1
            print("The arrangement:")
            print(kropki_solutions[i])
            print("Appears", kropki_solutions.count(kropki_solutions[i]), "times. Here is the current board with the arrangement:")
            print_board(board_list[i])
    print("Total non-unique arrangements:", non_unique_count)

# all_kropki_solutions(solutions)
# print(kropki_solutions[3])
