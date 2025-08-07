"""
Name: Dylan Warcholik

File Name: ReverseKropki6x6.py

Date Started: 8/6/2025

Description:
This file will produce a random 6x6 solution, fill in the dots, erase the numbers, and then find all solutions to that Kropki arrangement.
The results will be used to check for uniqueness of arrangments.
"""
from PuzzleGenerator6x6 import check_row, check_column, check_box, print_board
from LatexPrint6x6 import latex_print
from Coloring6x6 import colorer_6x6
import random


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
    horizontal_valid = True
    vertical_valid = True

    # Check horizontal dot (to the left)
    if current_column > 0:
        k_col = current_column - 1 # Location of the dot to the left of the current position
        if kropki_sol[0][current_row][k_col] == -1:
            difference = guess - current_board[current_row][k_col]
            if difference == 1 or difference == -1:
                horizontal_valid = True
            else:
                horizontal_valid = False

        elif kropki_sol[0][current_row][k_col] == 1:
            quotient = guess / current_board[current_row][k_col]
            if quotient == 2 or quotient == 0.5:
                horizontal_valid = True
            else:
                horizontal_valid = False

        else: # 0, so no dot, so the cells must NOT have a difference of one or quotient of 2
            difference = guess - current_board[current_row][k_col]
            if difference == 1 or difference == -1:
                horizontal_valid = False
            else:
                quotient = guess / current_board[current_row][k_col]
                if quotient == 2 or quotient == 0.5:
                    horizontal_valid = False
                else:
                    horizontal_valid = True
    
    # Check vertical dots
    if current_row > 0:
        k_row = current_row - 1 # Location of the dot above the current position
        if kropki_sol[1][k_row][current_column] == -1:
            difference = guess - current_board[k_row][current_column]
            # if (current_row == 3 and current_column == 5 and guess == 1):
            #     print("The difference between here and above is", difference)
            if difference == 1 or difference == -1:
                vertical_valid = True
            else:
                vertical_valid = False

        elif kropki_sol[1][k_row][current_column] == 1:
            quotient = guess / current_board[k_row][current_column]
            if quotient == 2 or quotient == 0.5:
                vertical_valid = True
            else:
                vertical_valid = False

        else: # 0, so no dot, so the cells must NOT have a difference of one or quotient of 2
            difference = guess - current_board[k_row][current_column]
            if difference == 1 or difference == -1:
                vertical_valid = False
            else:
                quotient = guess / current_board[k_row][current_column]
                if quotient == 2 or quotient == 0.5:
                    vertical_valid = False
                else:
                    vertical_valid = True
    if horizontal_valid and vertical_valid:
        return True
    else:
        return False

def find_puzzles_with_kropki(current_board, current_row, current_column, kropki_sol):
    """
    A recursive Depth-First Search function to find all 6x6 sudoku puzzles that are valid solutions to the Kropki arrangement, kropki_sol
    """
    # print("Now in position " + str((current_row,current_column))) # Error / process check
    guess = 1

    while guess < 7:
        # print("row, col, guess", current_row, current_column, guess)
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
                                # print("current board", current_board, "is valid. Appending...")
                                valid_solutions.append([row.copy() for row in current_board])
                            

                    # After recursively exploring all substates of this valid partial solution, backtrack to continue finding all valid solutions!
                    current_board[current_row][current_column] = 0

        # We arrive here if one of the checks failed OR we've backtracked from all solutions at this point; increment guess and check new answer
        guess += 1

# solution_num = random.randint(0,2000)
# print("Using solution number", solution_num)
# line = ""
print("Opening...")
with open("6x6Sudoku/AllSolutions6x6.txt", 'r') as f:
    line_num = 0
    single_solutions = 0
    multiple_solutions = 0
    max_solutions = 0 # Highest number of solutions
    # print("Starting at line 0...")
    for line in f:
        valid_solutions = [] # Reset to no solutions for every line

        line_num += 1
        if line_num % 100000 == 0:
            print(line_num)
        
        starting_solution = [[line[2], line[5], line[8], line[11], line[14], line[17]],
                            [line[22], line[25], line[28], line[31], line[34], line[37]],
                            [line[42], line[45], line[48], line[51], line[54], line[57]],
                            [line[62], line[65], line[68], line[71], line[74], line[77]],
                            [line[82], line[85], line[88], line[91], line[94], line[97]],
                            [line[102], line[105], line[108], line[111], line[114], line[117]]]
        # Cast the num strings to integers
        for i in range(len(starting_solution)):
            for j in range(len(starting_solution[i])):
                starting_solution[i][j] = int(starting_solution[i][j])
        
        original_coloring = colorer_6x6(starting_solution)

        blank_board = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0 ,0]]

        h_dots = find_horizontal_kropki_dots(starting_solution)
        v_dots = find_vertical_kropki_dots(starting_solution)

        all_dots = (h_dots, v_dots)
        find_puzzles_with_kropki(blank_board, 0, 0, all_dots)
        
        # print("Solution number", line_num, "led to", len(valid_solutions), "valid solutions. Printing...")
        # print("Kropki Arrangement:")
        # latex_print(all_dots)
        # for i in range(len(valid_solutions)):
        #     print("Solution #", i)
        #     print_board(valid_solutions[i])

        # Currently prints only puzzles with 2+ solutions of the same coloring
        if (len(valid_solutions) > 1):
            multiple_solutions += 1
            
            ## When looking for the highest number of solutions to an arrangement: # Found at least 7 to one, but did not make it through all solutions
            # if len(valid_solutions) > max_solutions:
            #     max_solutions = len(valid_solutions)

            # Count how many solutions have the same coloring as the original board:
            same_coloring_count = 0
            same_coloring_lst = []
            for sol in valid_solutions:
                current_coloring = colorer_6x6(sol)
                if current_coloring == original_coloring:
                    same_coloring_count += 1
                    same_coloring_lst.append(sol)
            if same_coloring_count > 1:
                print("The original solution", starting_solution, "led to", same_coloring_count, "boards with the same coloring.")
                for sol in same_coloring_lst:
                    print_board(sol)
                
            # print("Solution number", line_num, "led to", len(valid_solutions), "valid solutions. Printing...")
            # print("Kropki Arrangement:")
            # latex_print(all_dots)
            # for i in range(len(valid_solutions)):
            #     print("Solution #", i)
            #     print_board(valid_solutions[i])
        elif len(valid_solutions) == 1:
            single_solutions += 1

print("Single solutions:", single_solutions, "; multiple solutions:", multiple_solutions, "total:", (single_solutions + multiple_solutions))



# start_board = [[1, 2, 3, 4, 5, 6], [4, 5, 6, 1, 2, 3], [2, 1, 4, 3, 6, 5], [3, 6, 5, 2, 1, 4], [5, 3, 1, 6, 4, 2], [6, 4, 2, 5, 3, 1]]