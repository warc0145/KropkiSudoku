'''
Name: Dylan Warcholik
Date: 8/13/25
Description:
As I begin to explore counting unique Kropki arrangements on larger size puzzles, this file will include methods will enumerate the 4x4, 6x6, and 9x9 possible "boxes" and determine the uniqueness
of the Kropki arrangements of the boxes for all sizes.
'''
import itertools # Quick combination generator

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
    return kropki_box_dict


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
    return kropki_box_dict

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
    return kropki_box_dict


print("Generating 4x4 dictionary...")
dict_4 = box_generator_4x4()
count_dict_4 = dict()
for value in dict_4.values():
    if value in count_dict_4:
        count_dict_4[value] += 1
    else:
        count_dict_4[value] = 1
print(count_dict_4) # To confirm count is correct: "Sum =", sum(key * val for key,val in count_dict_4.items())

print("\n\nGenerating 6x6 dictionary...")
dict_6 = box_generator_6x6()
count_dict_6 = dict()
for value in dict_6.values():
    if value in count_dict_6:
        count_dict_6[value] += 1
    else:
        count_dict_6[value] = 1
print(count_dict_6) # To confirm count is correct: "Sum =", sum(key * val for key,val in count_dict_6.items())

print("\n\nGenerating 9x9 dictionary...")
dict_9 = box_generator_9x9()
count_dict_9 = dict()
for value in dict_9.values():
    if value in count_dict_9:
        count_dict_9[value] += 1
    else:
        count_dict_9[value] = 1
print(count_dict_9) # To confirm count is correct: sum(key * val for key,val in count_dict_9.items())