'''
Name: Dylan Warcholik
Date: 8/13/25
Description:
As I begin to explore counting unique Kropki arrangements on larger size puzzles, this file will include methods will enumerate 
the 4x4, 6x6, and 9x9 possible "boxes" and determine the uniqueness of the Kropki arrangements of the boxes for all sizes.
'''
import itertools # Quick combination generator
from PartialSudokuSolver import partial_sudoku_solver, solutions

# The following two methods will allow us to generate the Kropki arrangement of the given box:
def find_horizontal_kropki_dots(board):
    """
    Searches a given board and returns a Nx(N-1) array representing horizontal kropki dot placements (1 for black, -1 for white, 0 for no dot)
    Note, currently the circles between 1 and 2 are always black.
    """
    # In a row, there is len(board[0]) - 1 horizontal dots, and there are len(board) rows;
    # The following generates the blank board of horizontal dots
    horizontal_dots = [[0] * (len(board[0]) -1) for i in range(len(board))]

    # We want horizontal_dots to be mutable while we are filling it in, but then we need it to be immutable to be hashable
    # We will convert it to a tuple after the following loops:

    for r in range(len(board)):
        for c in range(len(board[r]) - 1): # This will all horizontally adjacent cells without exceeding bounds oif the array
            if ((board[r][c] == 1 and board[r][c+1] == 2) or (board[r][c] == 2 and board[r][c+1] == 1)): # Grey circles (1,2 combo)
                horizontal_dots[r][c] = 1
            elif (abs(board[r][c] - board[r][c+1]) == 1): # If the absolute difference of adjacent cells is 1...
                horizontal_dots[r][c] = -1
            elif (board[r][c] / board[r][c+1] == 2 or board[r][c+1] / board[r][c] == 2): # If adjacent cells are a scale factor of 2...
                horizontal_dots[r][c] = 1
    
    # Must convert every list to a tuple for hashability
    return tuple(tuple(x) for x in horizontal_dots)
# print(find_horizontal_kropki_dots([[1,2,3], [4,5,6]]))

def find_vertical_kropki_dots(board):
    """
    Searches a given board and returns a (N-1)xN array representing vertical kropki dot placements (1 for black, -1 for white, 0 for no dot)
    Note, currently the circles between 1 and 2 are always black.
    """
    vertical_dots = [[0] * len(board[0]) for i in range(len(board) - 1)]
    # print(vertical_dots)
    for r in range(len(board) - 1):
        for c in range(len(board[r])):
            if ((board[r][c] == 1 and board[r+1][c] == 2) or (board[r][c] == 2 and board[r+1][c] == 1)): # Grey circles (1,2 combo)
                vertical_dots[r][c] = 1
            elif (abs(board[r][c] - board[r+1][c]) == 1): # If the absolute difference of adjacent cells is 1...
                vertical_dots[r][c] = -1
            elif (board[r][c] / board[r+1][c] == 2 or board[r+1][c] / board[r][c] == 2): # If adjacent cells are a scale factor of 2...
                vertical_dots[r][c] = 1
    # Must convert every list to a tuple for hashability
    return tuple(tuple(x) for x in vertical_dots)
# print(find_vertical_kropki_dots([[1,2,3], [5,4,6]]))

def box_generator_4x4():
    """
    Generates the kropki arrangements of a single box from the 4x4 grid, report uniqueness

    Using a one dimensional array to represent the following solution, the numbers inside the box represent the index that 
    position will be located at in the list:
    -------
    | 0 1 |
    | 2 3 |
    -------
    """
    # The following will record all kropki arrangements from the box, counting the number of occurrances
    kropki_box_dict = dict()
    
    # Generate a list of boxes:
    all_boxes = list(itertools.permutations((1,2,3,4), 4))


    # Now change the one dimensional list to a 2x2, for convenience of maintaining the same methods for finding horiz and vert dots
    for i in range(len(all_boxes)):
        # print("Modifying:", all_boxes[i])
        all_boxes[i] = [[all_boxes[i][0], all_boxes[i][1]], [all_boxes[i][2], all_boxes[i][3]]]
    # print(all_boxes, "\n\n")

    # Finally, iterate through all boxes, generate the kropki arrangement, and count it in the kropki_box_dict 
    for box in all_boxes:
        kropki_arrangement = (find_horizontal_kropki_dots(box), find_vertical_kropki_dots(box))
        if kropki_arrangement in kropki_box_dict:
            kropki_box_dict[kropki_arrangement] += 1
        else:
            kropki_box_dict[kropki_arrangement] = 1
        # Need to compare indices 0,1, then 2,3, then 0,2 and 1,3
    return (all_boxes, kropki_box_dict)


def box_generator_6x6():
    """
    Generates the kropki arrangements of a single box from the 4x4 grid, report uniqueness

    Using a one dimensional array to represent the following solution, the numbers inside the box represent the index that 
    position will be located at in the list:
    ----------
    | 0 1 2 |
    | 3 4 5 |
    ----------
    """
    # The following will record all kropki arrangements from the box, counting the number of occurrances
    kropki_box_dict = dict()
    
    # Generate a list of boxes:
    all_boxes = list(itertools.permutations((1,2,3,4,5,6), 6))

    # Now change the one dimensional list to a 2x3, for convenience of maintaining the same methods for finding horiz and vert dots
    for i in range(len(all_boxes)):
        # print("Modifying:", all_boxes[i])
        all_boxes[i] = [[all_boxes[i][0], all_boxes[i][1], all_boxes[i][2]], 
                        [all_boxes[i][3], all_boxes[i][4], all_boxes[i][5]]]
    # print(all_boxes, "\n\n")

    # Finally, iterate through all boxes, generate the kropki arrangement, and count it in the kropki_box_dict 
    for box in all_boxes:
        kropki_arrangement = (find_horizontal_kropki_dots(box), find_vertical_kropki_dots(box))
        if kropki_arrangement in kropki_box_dict:
            # print("incrementing", kropki_box_dict[kropki_arrangement])
            # print("Sum so far:", sum(kropki_box_dict.values()))
            kropki_box_dict[kropki_arrangement] += 1
        else:
            # print("Creating...", kropki_arrangement)
            # print("Sum so far:", sum(kropki_box_dict.values()))
            kropki_box_dict[kropki_arrangement] = 1
        # Need to compare indices 0,1, then 2,3, then 0,2 and 1,3
    return (all_boxes, kropki_box_dict)

def box_generator_9x9():
    """
    Generates the kropki arrangements of a single box from the 4x4 grid, report uniqueness

    Using a one dimensional array to represent the following solution, the numbers inside the box represent the index that 
    position will be located at in the list:
    ---------
    | 0 1 2 |
    | 3 4 5 |
    | 6 7 8 |
    ---------
    """
    # The following will record all kropki arrangements from the box, counting the number of occurrances
    kropki_box_dict = dict()

    # Generate a list of boxes:
    all_boxes = list(itertools.permutations((1,2,3,4,5,6,7,8,9), 9))

    # Now change the one dimensional list to a 3x3, for convenience of maintaining the same methods for finding horiz and vert dots
    for i in range(len(all_boxes)):
        # print("Modifying:", all_boxes[i])
        all_boxes[i] = [[all_boxes[i][0], all_boxes[i][1], all_boxes[i][2]], 
                        [all_boxes[i][3], all_boxes[i][4], all_boxes[i][5]],
                        [all_boxes[i][6], all_boxes[i][7], all_boxes[i][8]]]
    
    # Finally, iterate through all boxes, generate the kropki arrangement, and count it in the kropki_box_dict 
    for box in all_boxes:
        kropki_arrangement = (find_horizontal_kropki_dots(box), find_vertical_kropki_dots(box))
        if kropki_arrangement in kropki_box_dict:
            kropki_box_dict[kropki_arrangement] += 1
        else:
            kropki_box_dict[kropki_arrangement] = 1
        # Need to compare indices 0,1, then 2,3, then 0,2 and 1,3
    return (all_boxes, kropki_box_dict)

#### For all three sizes, I will now use the dictionary that is {arrangement: number of solutions} to create a dictionary that is
#### {Number of solutions : Number of arrangements that has that many solutions}
print("Generating 4x4 dictionary...")
boxes_4, dict_4 = box_generator_4x4()
count_dict_4 = dict()
for value in dict_4.values():
    if value in count_dict_4:
        count_dict_4[value] += 1
    else:
        count_dict_4[value] = 1
print(count_dict_4) # To confirm count is correct: "Sum =", sum(key * val for key,val in count_dict_4.items())

print("\n\nGenerating 6x6 dictionary...")
boxes_6, dict_6 = box_generator_6x6()
count_dict_6 = dict()
for value in dict_6.values():
    if value in count_dict_6:
        count_dict_6[value] += 1
    else:
        count_dict_6[value] = 1
print(count_dict_6) # To confirm count is correct: "Sum =", sum(key * val for key,val in count_dict_6.items())

print("\n\nGenerating 9x9 dictionary...")
boxes_9, dict_9 = box_generator_9x9()
count_dict_9 = dict()
for value in dict_9.values():
    if value in count_dict_9:
        count_dict_9[value] += 1
    else:
        count_dict_9[value] = 1
print(count_dict_9) # To confirm count is correct: sum(key * val for key,val in count_dict_9.items())

print("4 max:", max(count_dict_4.keys()))
print("6 max:", max(count_dict_6.keys()))
print("9 max:", max(count_dict_9.keys()))

# First, focusing on 4x4 for quickness:

# For other sizes I will need to only consider the boxes that are a unique solution, but for the 4x4 all of them are!
for box in boxes_4:
    # Generate the start state for each box:
    start_state_4 = [[box[0][0], box[0][1], 4, 0],
                     [box[1][0], box[1][1], 2, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0]]
    # print(start_state_4)
    blank_board_4 = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
    # Clear all previous solutions (scope is weird here since solutions comes from PartialSudokuSolver.py):
    solutions.clear()
    partial_sudoku_solver(start_state_4, blank_board_4, 0, 0)
    print(len(solutions))
    for sol in solutions:
        for row in sol:
            print(row)
        print()


# # Now 6x6
# for box in boxes_6:
#     # Generate each boxes kropki arrangement:
#     k_arrangement = (find_horizontal_kropki_dots(box), find_vertical_kropki_dots(box))
    
#     # Identify those that only have one solution, then find out how many boards have that box! (Just like 4x4, now)
#     if dict_6[k_arrangement] == 1:
#         start_state_6 = [[box[0][0], box[0][1], box[0][2], 0, 0, 0],
#                         [box[1][0], box[1][1], box[1][2], 0, 0, 0],
#                         [0, 0, 0, 0, 0, 0],
#                         [0, 0, 0, 0, 0, 0],
#                         [0, 0, 0, 0, 0, 0],
#                         [0, 0, 0, 0, 0, 0]]
#         # print(start_state_6)
#         blank_board_6 = [[0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0]]
#         # Clear all previous solutions (scope is weird here since solutions comes from PartialSudokuSolver.py):
#         solutions.clear()
#         partial_sudoku_solver(start_state_6, blank_board_6, 0, 0)
#         print(len(solutions))