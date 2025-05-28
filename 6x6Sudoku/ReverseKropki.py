"""
Name: Dylan Warcholik

File Name: ReverseKropki.py

Date Started: 5/28/2025

Description:
This file will produce a random 6x6 solution, fill in the dots, erase the numbers, and then find all solutions to that Kropki arrangement.
The results will be used to check for uniqueness of arrangments.
"""
from PuzzleGenerator6x6 import check_row, check_column, check_box, print_board


def find_horizontal_kropki_dots(board):
    '''
    Searches a given board and returns a 6x5 array representing horizontal kropki dot placements (1 for black, -1 for white, 0 for no dot)
    Note, currently the circles between 1 and 2 are always black.
    '''
    horizontal_dots = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

    for r in range(len(board)):
        for c in range(len(board[r]) - 1): # This will compare 0,1 1,2 and 2,3 without exceeding array bounds
            if ((board[r][c] == 1 and board[r][c+1] == 2) or (board[r][c] == 2 and board[r][c+1] == 1)): # (1,2 combo)
                horizontal_dots[r][c] = 1
            elif (abs(board[r][c] - board[r][c+1]) == 1): # If the absolute difference of adjacent cells is 1...
                horizontal_dots[r][c] = -1
            elif (board[r][c] / board[r][c+1] == 2 or board[r][c+1] / board[r][c] == 2): # If adjacent cells are a scale factor of 2...
                horizontal_dots[r][c] = 1
    return horizontal_dots

def find_vertical_kropki_dots(board):
    '''
    Searches a given board and returns a 5x6 array representing vertical kropki dot placements (1 for black, -1 for white, 0 for no dot)
    Note, currently the circles between 1 and 2 are always black.
    '''
    vertical_dots = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    for r in range(len(board) - 1):
        for c in range(len(board[r])):
            if ((board[r][c] == 1 and board[r+1][c] == 2) or (board[r][c] == 2 and board[r+1][c] == 1)): # (1,2 combo)
                vertical_dots[r][c] = 1
            elif (abs(board[r][c] - board[r+1][c]) == 1): # If the absolute difference of adjacent cells is 1...
                vertical_dots[r][c] = -1
            elif (board[r][c] / board[r+1][c] == 2 or board[r+1][c] / board[r][c] == 2): # If adjacent cells are a scale factor of 2...
                vertical_dots[r][c] = 1
        
    return vertical_dots


def check_kropki(current_board, current_row, current_column, kropki_sol, guess):
    """
    Ensure that there are no violations with Kropki dots before updating this cell
    Returns true if there is no violation and false if a violation is found

    Will only check dots above and to the left, since cells to the right and below will not be filled yet.
    """
    # Check horizontal dot (to the left)
    if current_col > 0:
        k_col = current_col - 1 # Location of the dot to the left of the current position
        if kropki_sol[0][current_row][k_col] == -1:
            differece = guess - current_board[current_row][k_col]
            if difference == 1 or difference == -1:
                return True
            else:
                return False

        elif kropki_sol[0][current_row][k_col] == 1:
            quotient = guess / current_board[current_row][k_col]
            if quotient == 2 or quotient == 0.5:
                return True
            else:
                return False

        else: # 0, so no dot, so the cells must NOT have a difference of one or quotient of 2
            differece = guess - current_board[current_row][k_col]
            if difference == 1 or difference == -1:
                return False
            else:
                quotient = guess / current_board[current_row][k_col]
                if quotient == 2 or quotient == 0.5:
                    return False
                else:
                    return True
    
    # Check vertical dots
    if current_row > 0:
        k_row = current_row - 1 # Location of the dot to the left of the current position
        if kropki_sol[1][k_row][current_col] == -1:
            differece = guess - current_board[k_row][current_col]
            if difference == 1 or difference == -1:
                return True
            else:
                return False

        elif kropki_sol[1][k_row][current_col] == 1:
            quotient = guess / current_board[k_row][current_col]
            if quotient == 2 or quotient == 0.5:
                return True
            else:
                return False

        else: # 0, so no dot, so the cells must NOT have a difference of one or quotient of 2
            differece = guess - current_board[current_row][k_col]
            if difference == 1 or difference == -1:
                return False
            else:
                quotient = guess / current_board[k_row][current_col]
                if quotient == 2 or quotient == 0.5:
                    return False
                else:
                    return True


valid_solutions = []
def find_puzzles_with_kropki(current_board, current_row, current_column, kropki_sol):
    """
    A recursive Depth-First Search function to find all 4x4 sudoku puzzles
    """
    # print("Now in position " + str((current_row,current_column))) # Error / process check
    guess = 1

    while guess < 7:
        kropki_valid = check_kropki(current_board, current_row, current_column, kropki_sol, guess)
        
        if kropki_valid:
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

                        if current_column < 5: # move to next column
                            # print("Moving to next column!") # Error / process check
                            find_puzzles_with_kropki(current_board, current_row, current_column+1, kropki_sol)
                        
                        else: # At the end of the current row
                            if current_row < 5: # Move to next row
                                # print("Moving to next row!") # Error / process check
                                find_puzzles_with_kropki(current_board, current_row + 1, 0, kropki_sol)
                        
                            else: # We are at the end of the board!
                                print("current board", current_board, "is valid. Appending...")
                                valid_solutions.append(current_board)
                            

                    # After recursively exploring all substates of this valid partial solution, backtrack to continue finding all valid solutions!
                    current_board[current_row][current_column] = 0

        # We arrive here if one of the checks failed OR we've backtracked from all solutions at this point; increment guess and check new answer
        guess += 1

start_board = [[1, 2, 3, 4, 5, 6], [4, 5, 6, 1, 2, 3], [2, 1, 4, 3, 6, 5], [3, 6, 5, 2, 1, 4], [5, 3, 1, 6, 4, 2], [6, 4, 2, 5, 3, 1]]
blank_board = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0 ,0]]

h_dots = find_horizontal_kropki_dots(start_board)
v_dots = find_vertical_kropki_dots(start_board)

all_dots = (h_dots, v_dots)
find_puzzles_with_kropki(blank_board, 0, 0, all_dots)

print("There are", len(valid_solutions), "valid solutions to the arrangement. Printing...")
for i in range(len(valid_solutions)):
    print("Solution #", i)
    print_board(valid_solutions[i])
