'''
Name: Dylan Warcholik
Date: 8/16/25
Description:
This file will include methods for solving a sudoku board given a non-empty start state.
This will assist in finding solved boxes that lead to unique solutions "easier" (have lower number of solutions, require less 
aditional clues to narrow down to a single solution)
'''
from CheckBoxMethods import check_4x4_box, check_6x6_box, check_9x9_box
#### check_row and check_column come directly from SudokuPuzzleGenerator4x4.py

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


# slight modifications to check_box to allow for any size
def check_box(current_board, board_size, current_row, current_column, guess):
    """
    Makes call to appropriate check_NxN_box method
    """

    # First, determine which size grid we are in, then call appropriate sub-method:
    if board_size == 4:
        return check_4x4_box(current_board, current_row, current_column, guess)
    elif board_size == 6:
        return check_6x6_box(current_board, current_row, current_column, guess)
    elif board_size == 9:
        return check_9x9_box(current_board, current_row, current_column, guess)
    else:
        print("Unrecognized board_size:", boardsize)
        return False




def partial_sudoku_solver(start_state, current_board, current_row, current_column):
    """
    Given a starting state, this method will perform a Depth First Search skipping over clues that are already known.

    Will attempt to be general to allow any valid sudoku size (must at least be nxn).
    """
    # First, ensure all rows are a valid length, same as the height of the board
    board_size = len(start_state)
    for row in start_state:
        if not (len(row) == board_size):
            print("Error: Given start state was not a square board:")
            for row in start_state:
                print(row)
            return ""
    
    
    if (current_row == 0 and current_column == 0):
        # Then we are in the starting position, let's add the known board information:
        for row in range(len(start_state)):
            for col in range(len(start_state)):
                current_board[row][col] = start_state[row][col]


    # Next make sure that we are guessing at a location that isn't already solved (by given start state)
    if (not (start_state[current_row][current_column] == 0)):
        # Then we already know what value goes here! Move to next location:
        if current_column < (board_size - 1): 
            # # Not at the last column yet, move to next column
            # print("Moving to next column!") # Error / process check
            partial_sudoku_solver(start_state, current_board, current_row, current_column+1)
                        
        else: # At the end of the current row
            if current_row < 3: # Move to next row
                # print("Moving to next row!") # Error / process check
                partial_sudoku_solver(start_state, current_board, current_row + 1, 0)
                        
            else: # We are at the end of the board!
                # print("current board", current_board, "is valid. Appending...") 
                solutions.append([row.copy() for row in current_board])
                # print(len(solutions))


    else: # So only in the case that we are at a cell that needs to be filled in, do we begin guessing

        # Now, Depth First Search for all solutions
        guess = 1

        while guess < (board_size + 1): # For NxN board, want to go up to but not guess N+1
            row_valid = check_row(current_board, current_row, current_column, guess)

            if row_valid: # Then we should check the column
                column_valid = check_column(current_board, current_row, current_column, guess)

                if column_valid: # Then we should check the box
                    # print("Checking box at position", current_row, current_column, "with guess", guess)
                    box_valid = check_box(current_board, board_size, current_row, current_column, guess)
                    # print("After checking the box, we find:", box_valid)
                    if box_valid: # Then our guess is valid!
                        current_board[current_row][current_column] = guess
                        # print(guess, "is a valid guess; current board:", current_board)
                        # print("We are in position " + str((current_row,current_column))) # Error / process check
                        # print("The board appears as:") # Error / process check
                        # print(current_board) # Error / process check

                        if current_column < (board_size - 1): 
                            # # Not at the last column yet, move to next column
                            # print("Moving to next column!") # Error / process check
                            partial_sudoku_solver(start_state, current_board, current_row, current_column+1)
                            
                        else: # At the end of the current row
                            if current_row < (board_size - 1): 
                            # # Not at the last row yet, move to next row
                                # print("Moving to next row!") # Error / process check
                                partial_sudoku_solver(start_state, current_board, current_row + 1, 0)
                            
                            else: # We are at the end of the board!
                                # print("current board", current_board, "is valid. Appending...")
                                
                                solutions.append([row.copy() for row in current_board])
                                # print(len(solutions))

                                    
                        # After recursively exploring all substates of this valid partial solution, backtrack to continue finding all valid solutions!
                        # BUT! In this case, make sure not to erase KNOWN values
                        if start_state[current_row][current_column] == 0:
                            current_board[current_row][current_column] = 0

            # We arrive here if one of the checks failed OR we've backtracked from all solutions at this point; increment guess and check new answer
            guess += 1

# Initialioze solutions, an empty list:
solutions = []
blank_board_4 = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
blank_board_6 = [[0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0]]
blank_board_9 = [[0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0]]

# The following example completes the first three rows, the first column, and places all 1's; 5312 solutions follow from this state
ex_9 = [[1,2,3,4,5,6,7,8,9], [4,5,6,7,8,9,1,2,3], [7,8,9,1,2,3,4,5,6],
        [2,1,0,0,0,0,0,0,0], [3,0,0,0,1,0,0,0,0], [5,0,0,0,0,0,0,0,1],
        [6,0,0,0,0,0,0,1,0], [8,0,1,0,0,0,0,0,0], [9,0,0,0,0,1,0,0,0]]


# partial_sudoku_solver([[1,2,0,0],
#                         [0,0,1,2],
#                         [0,1,0,0],
#                         [0,0,0,1]], blank_board_4, 0, 0)
# partial_sudoku_solver([[1,2,3,0,0,0], [4,5,6,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0]], blank_board_6, 0, 0)

# partial_sudoku_solver(ex_9,  blank_board_9, 0, 0)

print(len(solutions))

# print(solutions)