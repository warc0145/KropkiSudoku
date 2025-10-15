'''
Name: Dylan Warcholik

File Name: Mod3Sudoku.py

Date Started: 10/4/25

Description:
Alternate puzzle style, so that there are three dots with an even number of number pairs, such as how mod applies to the 4x4.

0,1,2 represent the dots between two numbers, and each dot reveals the sum of the two digits in mod 3.
'''
from PuzzleGenerator6x6 import check_row, check_column, check_box
from ReverseKropki6x6 import line_to_board


def find_horizontal_mod_dots(board):
    '''
    Searches a given board and returns a 6x5 array representing horizontal mod-3 dot placements based on the sum of the digits
    (0 for 0mod3, 1 for 1mod3, 2 for 2mod3)
    '''
    horizontal_dots = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

    for r in range(len(board)):
        for c in range(len(board[r]) - 1): # This will compare 0,1 1,2 and 2,3 without exceeding array bounds
            horizontal_dots[r][c] = (board[r][c] + board[r][c+1]) % 3 # Set the mod-3 dot to what the sum is congruent to in mod 3
    return horizontal_dots

def find_vertical_mod_dots(board):
    '''
    Searches a given board and returns a 5x6 array representing vertical mod-3 dot placements based on the sum of the digits
    (0 for 0mod3, 1 for 1mod3, 2 for 2mod3)
    '''
    vertical_dots = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    for r in range(len(board) - 1):
        for c in range(len(board[r])):
            vertical_dots[r][c] = (board[r][c] + board[r+1][c]) % 3 # Set the mod-3 dot to what the sum is congruent to in mod 3
    return vertical_dots


def check_mod(current_board, current_row, current_column, mod_dots, guess):
    """
    Ensure that there are no violations with mod dots before updating this cell
    Returns true if there is no violation and false if a violation is found

    Will only check dots above and to the left of current cell, since cells to the right and below will not be filled yet.
    """
    # Default values: If we are row or col 0, then automatically valid for that check
    horizontal_valid = True
    vertical_valid = True

    # Check horizontal dot (to the left)
    if current_column > 0: # Check that we have a previous column
        # Then, horizontal dot is valid if the sum of the guess and the left value is congruent in mod 3 to the mod dot
        horizontal_valid = (mod_dots[0][current_row][current_column-1] == ((current_board[current_row][current_column-1] + guess) % 3))
        
    # Check vertical dots
    if current_row > 0: # Check that we have a previous row
        # Then, vertical dot is valid if the sum of the guess and the above value is congruent in mod 3 to the mod dot
        vertical_valid = (mod_dots[1][current_row-1][current_column] == ((current_board[current_row-1][current_column] + guess) % 3))
    
    return horizontal_valid and vertical_valid
    # If both are valid, return true, if either or both aren't valid, return false

def find_puzzles_with_mod(current_board, current_row, current_column, mod_dots):
    """
    A recursive Depth-First Search function to find all 6x6 sudoku puzzles that are valid solutions to the mod arrangement, mod_dots
    """
    # print("Now in position " + str((current_row,current_column))) # Error / process check
    guess = 1

    while guess < 7:
        # print("row, col, guess", current_row, current_column, guess)
        mod_valid = check_mod(current_board, current_row, current_column, mod_dots, guess)
        
        if mod_valid:
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
                            find_puzzles_with_mod(current_board, current_row, current_column+1, mod_dots)
                        
                        else: # At the end of the current row
                            if current_row < 5: # Move to next row
                                # print("Moving to next row!") # Error / process check
                                find_puzzles_with_mod(current_board, current_row + 1, 0, mod_dots)
                        
                            else: # We are at the end of the board!
                                # print("current board", current_board, "is valid. Appending...")
                                valid_solutions.append([row.copy() for row in current_board])
                        
                    # After recursively exploring all substates of this valid partial solution, backtrack to continue finding all valid solutions!
                    current_board[current_row][current_column] = 0

        # We arrive here if one of the checks failed OR we've backtracked from all solutions at this point; increment guess and check new answer
        guess += 1

start_board = [[1, 2, 3, 4, 5, 6], [4, 5, 6, 1, 2, 3], [2, 1, 4, 3, 6, 5], [3, 6, 5, 2, 1, 4], [5, 3, 1, 6, 4, 2], [6, 4, 2, 5, 3, 1]]
mod_dots = (find_horizontal_mod_dots(start_board), find_vertical_mod_dots(start_board))
# print(mod_dots)

# blank_board = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0 ,0]]

# valid_solutions = []
# find_puzzles_with_mod(blank_board, 0, 0, mod_dots)

# print(len(valid_solutions))

# for row in valid_solutions[0]:
#     print(row)
# print()    
# for row in valid_solutions[1]:
#     print(row)
# print()    
# for row in valid_solutions[2]:
#     print(row)


with open("6x6Sudoku/solutions.txt", 'r') as f:
    solution_count_dict = dict() # Keys will be the number of solutions, values will be the number of puzzles that had that many solutions
    line_num = 0
    for line in f:
        valid_solutions = [] # Reset to no solutions for every line

        line_num += 1
        if line_num % 1000 == 0:
            print(line_num)
            print(solution_count_dict)
        
        starting_solution = line_to_board(line)
        # Cast the num strings to integers
        for i in range(len(starting_solution)):
            for j in range(len(starting_solution[i])):
                starting_solution[i][j] = int(starting_solution[i][j])

        blank_board = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0 ,0]]

        h_dots = find_horizontal_mod_dots(starting_solution)
        v_dots = find_vertical_mod_dots(starting_solution)

        all_dots = (h_dots, v_dots)
        find_puzzles_with_mod(blank_board, 0, 0, all_dots)
        

        # Adds to the dictionary the number of solutions the given arrangement had:
        if len(valid_solutions) in solution_count_dict:
            solution_count_dict[len(valid_solutions)] += 1
        else:
            solution_count_dict[len(valid_solutions)] = 1
        
        
for key in solution_count_dict.keys():
    print("Mod arrangements with", key, "solutions:", solution_count_dict[key])

