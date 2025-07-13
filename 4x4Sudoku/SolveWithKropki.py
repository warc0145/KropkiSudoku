'''
Name: Dylan Warcholik

File Name: SolveWithKropki.py

Date Started: 7/13/2025

Description:
Finds all solutions to a 4x4 sudoku puzzle given a Kropki Arrangement
'''

from KropkiGenerator4x4 import kropki_solutions

from SudokuPuzzleGenerator4x4 import check_row, check_column, check_box, print_board

def check_kropki(current_board, current_row, current_column, kropki_sol, guess):
    """
    Ensure that there are no violations with Kropki dots before updating this cell
    Returns true if there is no violation and false if a violation is found

    Will only check dots above and to the left, since cells to the right and below will not be filled yet.
    """
    # print("Current board:")
    # print_board(current_board)
    # print("kropki_sol:", kropki_sol)
    # print("row, col, guess:", current_row, current_column, guess, "\n\n")
    # Check horizontal dot (to the left)
    if current_column > 0:
        k_col = current_column - 1 # Location of the dot to the left of the current position
        if kropki_sol[0][current_row][k_col] == -1:
            difference = guess - current_board[current_row][k_col]
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
            difference = guess - current_board[current_row][k_col]
            if difference == 1 or difference == -1:
                return False
            else:
                # print(current_board)
                # print(solutions)
                quotient = guess / current_board[current_row][k_col]
                if quotient == 2 or quotient == 0.5:
                    return False
                else:
                    return True
    
    # Check vertical dots
    if current_row > 0:
        k_row = current_row - 1 # Location of the dot to the left of the current position
        if kropki_sol[1][k_row][current_column] == -1:
            difference = guess - current_board[k_row][current_column]
            if difference == 1 or difference == -1:
                return True
            else:
                return False

        elif kropki_sol[1][k_row][current_column] == 1:
            quotient = guess / current_board[k_row][current_column]
            if quotient == 2 or quotient == 0.5:
                return True
            else:
                return False

        else: # 0, so no dot, so the cells must NOT have a difference of one or quotient of 2
            difference = guess - current_board[k_row][current_column]
            if difference == 1 or difference == -1:
                return False
            else:
                quotient = guess / current_board[k_row][current_column]
                if quotient == 2 or quotient == 0.5:
                    return False
                else:
                    return True
    return True # In the case that we are in position (0,0), there are no dots to check


solutions = []

def kropki_solver(current_board, kropki_sol, current_row, current_column):
    """
    A Depth First Search to solve a 4x4 sudoku board according to a given arrangement of Kropki dots.
    """
    guess = 1
    while guess < 5:
        row_valid = check_row(current_board, current_row, current_column, guess)

        if row_valid: # Then we should check the column
            column_valid = check_column(current_board, current_row, current_column, guess)

            if column_valid: # Then we should check the box
                box_valid = check_box(current_board, current_row, current_column, guess)

                if box_valid: # Then we should check the kropki_arrangement
                    kropki_valid = check_kropki(current_board, current_row, current_column, kropki_sol, guess)

                    if kropki_valid: # Then our guess is valid!
                        current_board[current_row][current_column] = guess

                        if current_column < 3: # move to next column
                    
                            kropki_solver(current_board, kropki_sol, current_row, current_column+1)
                        
                        else: # At the end of the current row
                            if current_row < 3: # Move to next row
                                kropki_solver(current_board, kropki_sol, current_row + 1, 0)
                        
                            else: # We are at the end of the board!                            
                                solutions.append([row.copy() for row in current_board])

                    # After recursively exploring all substates of this valid partial solution, backtrack to continue finding all valid solutions!
                    current_board[current_row][current_column] = 0
        
        # We arrive here if one of the checks failed OR we've backtracked from all solutions at this point; increment guess and check new answer
        guess += 1


    

blank_board = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
kropki_solver(blank_board, kropki_solutions[0], 0, 0)
print(solutions)