
'''
Name: Dylan Warcholik

File Name: PartialSolutionSolver.py

Date Started: 7/28/2025

Description:
Previous solvers assume that where a dot is not present, a dot *cannot* be present. This solver does not make that assumption and
instead assumes that the kropki arrangement is a partial arrangement, finding all possible solutions.
'''
import itertools
from SudokuPuzzleGenerator4x4 import check_row, check_column, check_box
from SolveWithKropki import kropki_solver
from Coloring import colorer
from AltLatexPrinter import color_printer
from KropkiGenerator4x4 import all_kropki_numbers, find_horizontal_kropki_dots, find_vertical_kropki_dots

def check_partial_kropki(current_board, partial_kropki, current_row, current_column, guess):
    """
    Ensure that there are no violations with Kropki dots before updating this cell
    Returns true if there is no violation and false if a violation is found

    Will only check dots above and to the left, since cells to the right and below will not be filled yet.
    """
    # In the case that we are in position (0,0), there are no dots to check, so these are the default values:
    vertical_valid = True
    horizontal_valid = True
    # print("Current board:")
    # print_board(current_board)
    # print("partial_kropki:", partial_kropki)
    # print("row, col, guess:", current_row, current_column, guess, "\n\n")

    # Check horizontal dot (to the left)
    if current_column > 0:
        k_col = current_column - 1 # Location of the dot to the left of the current position
        if partial_kropki[0][current_row][k_col] == -1:
            difference = guess - current_board[current_row][k_col]
            if difference == 1 or difference == -1:
                # Must also consider if it is a 1 and 2; this requires a black dot, so it would be invalid here
                if guess == 1 or current_board[current_row][k_col] == 1:
                    horizontal_valid = False
                else:
                    horizontal_valid = True
            else:
                horizontal_valid = False

        elif partial_kropki[0][current_row][k_col] == 1:
            quotient = guess / current_board[current_row][k_col]
            if quotient == 2 or quotient == 0.5:
                horizontal_valid = True
            else:
                horizontal_valid = False

        else: # 0, so no dot, so the cells may or may not have a black or white dot; any value is valid
            horizontal_valid = True
        
        # Check vertical dots
        if current_row > 0:
            k_row = current_row - 1 # Location of the dot to the left of the current position
            if partial_kropki[1][k_row][current_column] == -1:
                # print("We are guessing a value for the location", current_row, current_column, "which has a white dot to the left")
                # print("Our guess is", guess, "and the value to the left is")
                difference = guess - current_board[k_row][current_column]
                if difference == 1 or difference == -1: 
                    # Since we don't want a white dot between a one and a two, we must check that neither are a one:
                    if guess == 1 or current_board[k_row][current_column] == 1:
                        vertical_valid = False
                    else:
                        vertical_valid = True
                else:
                    vertical_valid = False

            elif partial_kropki[1][k_row][current_column] == 1:
                quotient = guess / current_board[k_row][current_column]
                if quotient == 2 or quotient == 0.5:
                    vertical_valid = True

                else:
                    vertical_valid = False

            else: # 0, so no dot, so the cells may or may not have a black or white dot; any value is valid
                vertical_valid = True
        
    if horizontal_valid and vertical_valid:
        return True
    else:
        return False


def partial_solver(current_board, partial_kropki, current_row, current_column, solutions):
    """
    A Depth First Search to solve a 4x4 sudoku board according to a given arrangement of Kropki dots assuming that 
    all dots are not necessarily present.
    """
    guess = 1
    while guess < 5:
        # print("Current row, column, guess:", current_row, current_column, guess)
        # print("Current board:", current_board, "\n")
        row_valid = check_row(current_board, current_row, current_column, guess)

        if row_valid: # Then we should check the column
            column_valid = check_column(current_board, current_row, current_column, guess)

            if column_valid: # Then we should check the box
                box_valid = check_box(current_board, current_row, current_column, guess)

                if box_valid: # Then we should check the kropki_arrangement
                    # print("Just called kropki valid with currentboard=", current_board, "and row,col,guess=", current_row, current_column, guess)
                    kropki_valid = check_partial_kropki(current_board, partial_kropki, current_row, current_column, guess)
                    # print("the result is", kropki_valid)
                    if kropki_valid: # Then our guess is valid!
                        current_board[current_row][current_column] = guess

                        if current_column < 3: # move to next column
                            partial_solver(current_board, partial_kropki, current_row, current_column+1, solutions)
                            
                        else: # At the end of the current row
                            if current_row < 3: # Move to next row
                                partial_solver(current_board, partial_kropki, current_row + 1, 0, solutions)
                            else: # We are at the end of the board!                            
                                solutions.append([row.copy() for row in current_board])

                    # After recursively exploring all substates of this valid partial solution, backtrack to continue finding all valid solutions!
                    current_board[current_row][current_column] = 0
                    
        
        # We arrive here if one of the checks failed OR we've backtracked from all solutions at this point; increment guess and check new answer 
        # if we haven't reached the end of the board with the last guess
        guess += 1
    if current_row == 0 and current_column == 0:
        return solutions
blank_board = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
blank_arrangement = ([[0,0,0],[0,0,0],[0,0,0],[0,0,0]],[[0,0,0,0],[0,0,0,0],[0,0,0,0]])

# print(len(partial_solver(blank_board, blank_arrangement, 0, 0, [])))

# Now, I want to use the above method to find the minimum number of dots required for a unique solution
def partial_solution_minimizer():
    """
    The number assigned to dot locations:
    ([[1,2,3], [4,5,6], [7,8,9], [10,11,12]], 
    [[13,14,15,16], [17,18,19,20], [21,22,23,24]])

    When I need to choose three dots, I will choose every combination ofthree numbers from 1-24 
    then consider every combination of those being black or white.

    e.g. three dots, first choice is 1,2,3. could be bbb,bbw,bwb,bww,wbb,wbw,wwb,www
    """
    current_k_arrangement = ([[0,0,0], [0,0,0], [0,0,0], [0,0,0]], [[0,0,0,0], [0,0,0,0], [0,0,0,0]])
    # First build a dictionary that relates number to a dot's position on the board:
    position_dict = dict()
    count = 1
    for dot_type in range(len(current_k_arrangement)): # Counts horizontal dots (current_k_arrangement[0]) and vertical dots (current_k_arrangement[1])
        for row in range(len(current_k_arrangement[dot_type])): # Considers each row of each type
            for col in range(len(current_k_arrangement[dot_type][row])): # Considers each column in each row in each type (now considering every dot location)
                position_dict[count] = (dot_type, row, col)
                count += 1

    for num_dots in range(1,12): # Through brute force counting, I know that there are unique 12 dot solutions, so no need to consider 13-24 dots
        print("Num dots:", num_dots)
        # dot_sets will be a list of all combinations of length(num_dots) of the numbers 1-24. Must examine each set individually
        dot_sets = list(itertools.combinations(position_dict.keys(), num_dots))
        # print(dot_sets)
        for set_num in range(len(dot_sets)): # The length of dot_sets is dependent on num_dots. len(dot_sets) = (24 choose num_dots)
            locations = [position_dict[key] for key in dot_sets[set_num]]
            # print("locations:", locations)
            
            # Now that we have the locations we need to explore, we need every combination of black and white dots. 
                # For one location, this will just be b and w at each
                # For two locations, this will be bb,ww,bw,wb for each set of two
                # For three, bbb,bbw,bwb,bww,wbb,wbw,wwb,www for each set of three
                # And so on
            # Below, dot_types becomes a list of every color combination that is the length of num_dots
            dot_types = list(itertools.product((1,-1), repeat=num_dots))
            # print("all dot combos:", dot_types)

            for each in dot_types:
                # print("Dot types:", each)
                for x in range(len(each)):
                    i,j,k = locations[x]
                    current_k_arrangement[i][j][k] = each[x]
                all_solutions = partial_solver([[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]],
                                                current_k_arrangement, 0, 0, [])
                num_solutions = len(all_solutions)
                if num_solutions == 1:
                    print("Answer found!")
                    print("The current kropki arrangement is " + str(current_k_arrangement) + " and it has one solution")
                    return
                # After attempting solution, return current kropki arrangement to blank form
                for x in range(len(each)):
                    i,j,k = locations[x]
                    current_k_arrangement[i][j][k] = 0
                
# partial_solution_minimizer()

# Now that I know that there are some four dot partial arrangements with unique solutions, let's see how many there are\
def four_dot_finder():
    """
    Find and count all four dot partial-kropki-arrangements that have a unique solution.
    """
    unique_solutions = [] # will hold a list of partial arrangements with four dots and a unique solution
    total_attempts = 0
    total_solutions = 0

    current_k_arrangement = ([[0,0,0], [0,0,0], [0,0,0], [0,0,0]], [[0,0,0,0], [0,0,0,0], [0,0,0,0]])
    # First build a dictionary that relates number to a dot's position on the board:
    position_dict = dict()
    count = 1
    for dot_type in range(len(current_k_arrangement)): # Counts horizontal dots (current_k_arrangement[0]) and vertical dots (current_k_arrangement[1])
        for row in range(len(current_k_arrangement[dot_type])): # Considers each row of each type
            for col in range(len(current_k_arrangement[dot_type][row])): # Considers each column in each row in each type (now considering every dot location)
                position_dict[count] = (dot_type, row, col)
                count += 1

    dot_sets = list(itertools.combinations(position_dict.keys(), 4))
    # print(dot_sets)
    for set_num in range(len(dot_sets)): # The length of dot_sets is (24 chooose 4)
        locations = [position_dict[key] for key in dot_sets[set_num]]
        # print("locations:", locations)
            
        # Now that we have the locations we need to explore, we need every combination of black and white dots.
        # For each set of four: bbbb,bbbw,bbwb,bbww,bwbb,bwbw,bwwb,bwww,wbbb,wbbw,wbwb,wbww,wwbb,wwbw,wwwb,wwww
        dot_types = list(itertools.product((1,-1), repeat=4))
        # print("all dot combos:", dot_types)

        for each in dot_types:
            # print("Dot types:", each)
            for x in range(len(each)):
                i,j,k = locations[x]
                current_k_arrangement[i][j][k] = each[x]
            
            all_solutions = partial_solver([[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]],
                                            current_k_arrangement, 0, 0, [])
            num_solutions = len(all_solutions)
            total_attempts += 1
            
            if num_solutions == 1:
                # Since the tuple contains list, we must append a tuple of a copy of the lists in order to continue modifying the temporary
                # version without affecting the permanent version
                total_solutions += 1
                unique_solutions.append(([row.copy() for row in current_k_arrangement[0]], [row.copy() for row in current_k_arrangement[1]]))
            # After attempting solution, return current kropki arrangement to blank form
            for x in range(len(each)):
                i,j,k = locations[x]
                current_k_arrangement[i][j][k] = 0
    return unique_solutions

four_dot_solutions = four_dot_finder()
print("Now we have a list of partial arrangements that each have one solution. There are " + str(len(four_dot_solutions)) + ".\n")

# Every 4x4 solution that appears will be stored here. We will track how many appear / are used
full_solutions = []

for partial_k in four_dot_solutions:
    current_sol = partial_solver([[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]],
                                partial_k, 0, 0, [])[0]
    if current_sol not in full_solutions:
        full_solutions.append(current_sol)

print("Done collecting; the partial arrangements cover", len(full_solutions), "of the full solutions. Counting dots in the full arrangements...")

# for sol in full_solutions:
#     print(sol)

# all_kropki_numbers(full_solutions)

all_colorings = {(((0, 0), (1, 2), (2, 1), (3, 3)), ((0, 1), (1, 3), (2, 0), (3, 2)), ((0, 2), (1, 0), (2, 3), (3, 1)), ((0, 3), (1, 1), (2, 2), (3, 0))): 24, 
                (((0, 0), (1, 2), (2, 3), (3, 1)), ((0, 1), (1, 3), (2, 0), (3, 2)), ((0, 2), (1, 0), (2, 1), (3, 3)), ((0, 3), (1, 1), (2, 2), (3, 0))): 24, 
                (((0, 0), (1, 2), (2, 1), (3, 3)), ((0, 1), (1, 3), (2, 2), (3, 0)), ((0, 2), (1, 0), (2, 3), (3, 1)), ((0, 3), (1, 1), (2, 0), (3, 2))): 24, 
                (((0, 0), (1, 2), (2, 3), (3, 1)), ((0, 1), (1, 3), (2, 2), (3, 0)), ((0, 2), (1, 0), (2, 1), (3, 3)), ((0, 3), (1, 1), (2, 0), (3, 2))): 24, 
                (((0, 0), (1, 3), (2, 1), (3, 2)), ((0, 1), (1, 2), (2, 0), (3, 3)), ((0, 2), (1, 0), (2, 3), (3, 1)), ((0, 3), (1, 1), (2, 2), (3, 0))): 24, 
                (((0, 0), (1, 3), (2, 2), (3, 1)), ((0, 1), (1, 2), (2, 3), (3, 0)), ((0, 2), (1, 0), (2, 1), (3, 3)), ((0, 3), (1, 1), (2, 0), (3, 2))): 24, 
                (((0, 0), (1, 2), (2, 1), (3, 3)), ((0, 1), (1, 3), (2, 0), (3, 2)), ((0, 2), (1, 1), (2, 3), (3, 0)), ((0, 3), (1, 0), (2, 2), (3, 1))): 24, 
                (((0, 0), (1, 2), (2, 3), (3, 1)), ((0, 1), (1, 3), (2, 2), (3, 0)), ((0, 2), (1, 1), (2, 0), (3, 3)), ((0, 3), (1, 0), (2, 1), (3, 2))): 24, 
                (((0, 0), (1, 3), (2, 1), (3, 2)), ((0, 1), (1, 2), (2, 0), (3, 3)), ((0, 2), (1, 1), (2, 3), (3, 0)), ((0, 3), (1, 0), (2, 2), (3, 1))): 24, 
                (((0, 0), (1, 3), (2, 2), (3, 1)), ((0, 1), (1, 2), (2, 0), (3, 3)), ((0, 2), (1, 1), (2, 3), (3, 0)), ((0, 3), (1, 0), (2, 1), (3, 2))): 24, 
                (((0, 0), (1, 3), (2, 1), (3, 2)), ((0, 1), (1, 2), (2, 3), (3, 0)), ((0, 2), (1, 1), (2, 0), (3, 3)), ((0, 3), (1, 0), (2, 2), (3, 1))): 24, 
                (((0, 0), (1, 3), (2, 2), (3, 1)), ((0, 1), (1, 2), (2, 3), (3, 0)), ((0, 2), (1, 1), (2, 0), (3, 3)), ((0, 3), (1, 0), (2, 1), (3, 2))): 24}

# small_kropki_colorings = colorer(full_solutions)
# print("The 122 solutions cover", len(small_kropki_colorings), "colorings. Now printing latex form:")
# for coloring in small_kropki_colorings:
#     color_printer(coloring)

# for coloring in all_colorings:
#     if coloring not in small_kropki_colorings:
#         color_printer(coloring)



# print("Now counting number of arrangements per board...")
# # Here, I count for each of the 122 solutions with 4-dot-arrangements, how many four dot arrangements they have;
# for current_board in full_solutions:
#     num_four_dot_arrangements = 0

#     full_board_k = (find_horizontal_kropki_dots(current_board), find_vertical_kropki_dots(current_board))

#     for partial_k in four_dot_solutions: # Check every four-dot-arrangement against every full-board
#         dot_count = 0
#         for dot_type in range(len(partial_k)): # Explore horizontal dots then vertical dots
#             for row in range(len(partial_k[dot_type])): # Explore each row
#                 for cell in range(len(partial_k[dot_type][row])): # Explore every cell
#                     if partial_k[dot_type][row][cell] is not 0:
#                         # Then we need to check if it is in our current board, so we know if this counts towards the num_four_dot_arrangements
#                         if partial_k[dot_type][row][cell] == full_board_k[dot_type][row][cell]: 
#                             # Each dot that is correct add one; we will check if all four are outside of the loops
#                             dot_count += 1
        
#         if dot_count == 4:
#             # Then yes, this partial arrangement goes with this board!
#             num_four_dot_arrangements += 1
    
#     # Now we have the full count of how many four-dot-arrangements this solution hasL:
    # print("The current solution,", current_board, "with the followuing kropki arrangement", full_board_k, "has", num_four_dot_arrangements, "four dot arrangements.")