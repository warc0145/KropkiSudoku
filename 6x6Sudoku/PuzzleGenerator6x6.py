'''
Name: Dylan Warcholik

File Name: PuzzleGenerator6x6.py

Date Started: 5/20/2025

Description:
This file will generate all complete solutions to a 6x6 Sudoku.
Outline copied from SudokuPuzzleGenerator4x4.py (check_row and check_column are identical)
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

    The quadrants I will number as follows:
    -----------------
    |   1   |   2   |
    |       |       |
    -----------------
    |   3   |   4   |
    |       |       |
    -----------------
    |   5   |   6   |
    |       |       |
    -----------------
    """
    quadrant = 0

    # First, determine which box we are in and need to check

    if current_row < 2:
        if current_column < 3:
            quadrant = 1
        else:
            quadrant = 2
    elif current_row < 4:
        if current_column < 3:
            quadrant = 3
        else:
            quadrant = 4
    else:
        if current_column < 3:
            quadrant = 5
        else: 
            quadrant = 6


    # Check the appropriate quadrant
    if quadrant == 1:
        box_vals = [current_board[0][0], current_board[0][1], current_board[0][2], 
                    current_board[1][0], current_board[1][1], current_board[1][2]]
        if guess in box_vals:
            # Then the value is already present in this box, which is a violation
            return False

    elif quadrant == 2:
        box_vals = [current_board[0][3], current_board[0][4], current_board[0][5], 
                    current_board[1][3], current_board[1][4], current_board[1][5]]
        if guess in box_vals:
            # Then the value is already present in this box, which is a violation
            return False

    elif quadrant == 3:
        box_vals = [current_board[2][0], current_board[2][1], current_board[2][2], 
                    current_board[3][0], current_board[3][1], current_board[3][2]]
        if guess in box_vals:
            # Then the value is already present in this box, which is a violation
            return False
    
    elif quadrant == 4:
        box_vals = [current_board[2][3], current_board[2][4], current_board[2][5], 
                    current_board[3][3], current_board[3][4], current_board[3][5]]
        if guess in box_vals:
            # Then the value is already present in this box, which is a violation
            return False
    elif quadrant == 5:
        box_vals = [current_board[4][0], current_board[4][1], current_board[4][2], 
                    current_board[5][0], current_board[5][1], current_board[5][2]]
        if guess in box_vals:
            # Then the value is already present in this box, which is a violation
            return False

    else: # quadrant == 6
        box_vals = [current_board[4][3], current_board[4][4], current_board[4][5], 
                    current_board[5][3], current_board[5][4], current_board[5][5]]
        if guess in box_vals:
            # Then the value is already present in this box, which is a violation
            return False

    # If we did not find a box violation, then it is a valid move
    return True

def print_board(board):
    """
    Print a visual of the board, which should be a two dimensional, 6x6 array
    """
    for row_num in range(4):
        row = board[row_num]
        if row_num % 2 == 0:
            print("-----------------")
        print("|", row[0], row[1], row[2], "|", row[3], row[4], row[5], "|", row[6], row[7], row[8], "|")
    print("-----------------")


def find_puzzles(current_board, current_row, current_column):
    """
    A recursive Depth-First Search function to find all 4x4 sudoku puzzles
    """
    print("Now in position " + str((current_row,current_column))) # Error / process check
    guess = 1

    while guess < 7:
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
                        print("Moving to next column!") # Error / process check
                        find_puzzles(current_board, current_row, current_column+1)
                        
                    else: # At the end of the current row
                        if current_row < 3: # Move to next row
                            print("Moving to next row!") # Error / process check
                            find_puzzles(current_board, current_row + 1, 0)
                        
                        else: # We are at the end of the board!
                            print("current board", current_board, "is valid. Appending...")
                            
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

blank_board = [[0,0,0,0,0,0], [0,0,0,0,0,0,], [0,0,0,0,0,0], [0,0,0,0,0,0]]




find_puzzles(blank_board, 0, 0) # Base call to find_puzzles, starting in the (0,0) position with a blank board (all zeroes)

# for sol in solutions[:10]:
#     print(solutions.count(sol))
print("There are", len(solutions), "solutions")
for i in range(10):
  print("Solution #", i, "appears", solutions.count(solutions[i]), "time(s). This solution is:")
  print_board(solutions[i])
