'''
Name: Dylan Warcholik

File Name: SudokuPuzzleGenerator4x4.py

Date Started: 2/24/2025

Description:
This file is part of my research on Sudoku puzzles with Kropki dots.
It first intends to be able to produce a random complete 4x4 sudoku
puzzle, or possibly all complete sudoku puzzles of size 4x4.
'''


def check_row(current_board, current_row, current_column, guess):
    """
    Ensure that there are no violations in the current row before updating this cell
    Returns true if there is no violation and false if a violation is found
    """

    if current_board[current_row].count(guess) > 0:
        # Then the value we are guessing is already present in the row, which is a violation
        
        return False
    else:
        # There is no violation, so this is a valid guess
        return True



def check_column(current_board, current_row, current_column, guess):
    """
    Ensure that there are no violations in the current column before updating this cell
    Returns true if there is no violation and false if a violation is found
    """
    for row in current_board:
        if row[current_column] == guess:
            # Then the value we are guessing is already present in the row, which is a violation
            return False
        else:
            # There is no violation, so check next place in column
            continue # Redundant line

    # If we have not found a violation in this column, then our guess is valid
    return True



def check_box(current_board, current_row, current_column, guess):
    """
    Ensure that there are no violations in the current box before updating this cell
    Returns true if there is no violation and false if a violation is found
    """
    current_box = ""

    # First, determine which box we are in and need to check

    # Checking top vs bottom
    if current_row < 2:
        # top half of the puzzle
        current_box = current_box + "top_"
    else:
        # bottom half of the puzzle
        current_box = current_box + "bottom_"

    # Checking left vs right
    if current_column < 2:
        # left half of the puzzle
        current_box = current_box + "left"
    else:
        # right half of the puzzle
        current_box = current_box + "right"


    # Check the appropriate quadrant
    if current_box == "top_left":
        box_vals = [current_board[0][0], current_board[0][1], current_board[1][0], current_board[1][1]]
        if guess in box_vals:
            # Then the value is already present in this box, which is a violation
            return False

    elif current_box == "top_right":
        box_vals = [current_board[0][2], current_board[0][3], current_board[1][2], current_board[1][3]]
        if guess in box_vals:
            # Then the value is already present in this box, which is a violation
            return False

    elif current_box == "bottom_left":
        box_vals = [current_board[2][0], current_board[2][1], current_board[3][0], current_board[3][1]]
        if guess in box_vals:
            # Then the value is already present in this box, which is a violation
            return False
    elif current_box == "bottom right": # ELSE should also work here
        box_vals = [current_board[2][2], current_board[2][3], current_board[3][2], current_board[3][3]]
        if guess in box_vals:
            # Then the value is already present in this box, which is a violation
            return False

    # If we did not find a box violation, then it is a valid move
    return True

def print_board(board):
    """
    Print a visual of the board, which should be a two dimensional, 4x4 array
    """
    for row_num in range(4):
        row = board[row_num]
        if row_num % 2 == 0:
            print("-------------")
        print("|", row[0], row[1], "|", row[2], row[3], "|")
    print("-------------")


def find_horizontal_kropki_dots(board):
    '''
    Searches a given board and returns a 4x3 array representing horizontal kropki dot placements (1 for black and -1 for white)
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
    Searches a given board and returns a 3x4 array representing vertical kropki dot placements (1 for black and -1 for white)
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


def find_puzzles(current_board, current_row, current_column):
    """
    A recursive Depth-First Search function to find all 4x4 sudoku puzzles
    """
     # print("Now in position " + str((current_row,current_column))) # Error / process check
    guess = 1

    while guess < 5:
        row_valid = check_row(current_board, current_row, current_column, guess)

        if row_valid: # Then we should check the column
            column_valid = check_column(current_board, current_row, current_column, guess)

            if column_valid: # Then we should check the box
                box_valid = check_box(current_board, current_row, current_column, guess)

                if box_valid: # Then our guess is valid!
                    current_board[current_row][current_column] = guess
                    # print(guess, "is a valid guess; current board:", current_board)
                    # print("We are in position " + str((current_row,current_column))) # Error / process check
                    # print("The board appears as:") # Error / process check
                    # print(current_board) # Error / process check

                    if current_column < 3: # move to next column
                        # print("Moving to next column!") # Error / process check
                        find_puzzles(current_board, current_row, current_column+1)
                        
                    else: # At the end of the current row
                        if current_row < 3: # Move to next row
                            # print("Moving to next row!") # Error / process check
                            find_puzzles(current_board, current_row + 1, 0)
                        
                        else: # We are at the end of the board!
                            # print("current board", current_board, "is valid. Appending...")
                            
                            solutions.append([row.copy() for row in current_board])
                            # print("Solution appended, length:", len(solutions)) # Error / process check
                            
                            # if len(solutions) == 288:
                            #     print("Solutions:", solutions)

                            # if solutions[-1] == [[1, 2, 3, 4], [3, 4, 1, 2], [2, 1, 4, 3], [4, 3, 2, 1]]:
                            #     print("Example solution found, searching and printing kropki dots...")
                            #     print_board(solutions[-1])
                            #     horiz_kropki = find_horizontal_kropki_dots(solutions[-1])
                            #     vert_kropki = find_vertical_kropki_dots(solutions[-1])

                            #     print("Horizontal:", horiz_kropki)
                            #     print("Vertical:", vert_kropki)

                                

                    
                    # After recursively exploring all substates of this valid partial solution, backtrack to continue finding all valid solutions!
                    current_board[current_row][current_column] = 0

        # We arrive here if one of the checks failed OR we've backtracked from all solutions at this point; increment guess and check new answer
        guess += 1
    

solutions = [] # This will be a list of two dimensional arrays, representing all possible solutions from a given starting point (currently only a blank board)

blank_board = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
row_board = [[1,2,3,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
column_board = [[1,0,0,0], [2,0,0,0], [3,0,0,0], [0,0,0,0]]

'''
print(check_row(blank_board, 0, 0, 1))
print(check_row(row_board, 0, 0, 1))
print(check_row(row_board, 0, 0, 4))

print(check_column(column_board, 3, 0, 1))
print(check_column(column_board, 3, 0, 4))
'''       


find_puzzles(blank_board, 0, 0) # Base call to find_puzzles, starting in the (0,0) position with a blank board (all zeroes)

# for sol in solutions[:10]:
#     print(solutions.count(sol))

# print(solutions)

all_boards = solutions.copy()

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


# maximum_kropki(all_boards)


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

# minimum_kropki(all_boards)

def all_kropki_numbers(board_list):
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

# all_kropki_numbers(all_boards)

kropki_solutions = []
def all_kropki_solutions(board_list):
    '''
    This function will append to the existing list, kropki_solutions, a tuple of horizontal dots and vertical dots (which are each two dimensional arrays)
    Then, we will examine kropki_solutions to check for uniqueness
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

all_kropki_solutions(all_boards)
print(kropki_solutions[3])

'''
Where am I now:
The program currently produces solutions, a list of 4x4 lists of all 288 unique valid solutions to 4x4 sudoku problems, taking a recursive
depth first search approach.

It also has functions maximum_kropki(board_list) and minimum_kropki(board_list) which determine the puzzles in the list with the maximum and
minimum number of possible Kropki dots.

Finally, all_krokpi_numbers has produced the following dictionary where the key is the number of kropki dots, and the value is the number of
solutions with that number of kropki dots, covering all 4x4 solutions: {16: 136, 18: 64, 15: 64, 12: 8, 14: 16}

Where am I going:
Now, I want to be able to explore the uniqueness of the Kropki dot arrangements to see if a given arrangement can represent a unique solution.
I might do this by first comparing the 8 minimum puzzles. Python makes list comparisons very simple, including lists of lists, so I can simply use
the equality operator to check for repeats... Aditionally, I could try to implement a dictionary that counts the number of each arrangement of 
Kropki dots.

Another question to consider: How many puzzles / what kinds of puzzles have a unique arrangement of Kropki dots? I should think about the cases
in which a Kropki dot could be black or white, and how this effects the uniqueness of the solution based on the arrangement, if it is not unique
given the current set up. Maybe I should allow for a "grey" Kropki dot for between cells with a 1 and 2.



The program should also be close to being able to find all solutions given any start state, not just a blank board. I should only need to add
a strategy to keep track of which clues cannot be turned back into zeroes (clues given in the start state). Likely if I record the starting 
board along with the current board, I can check if a clue is in the start board before reverting it or entering the while loop to guess that 
position's value.
'''