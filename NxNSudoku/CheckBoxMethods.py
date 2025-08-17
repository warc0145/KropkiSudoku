'''
Name: Dylan Warcholik

Date: 8/16/25

Description:
This file only contains the methods for checking a 4x4, 6x6, and 9x9 box. They're imported into PartialSudokuSolver.py, but written
here to prevent unecessary crowding in that file.
'''
def check_4x4_box(current_board, current_row, current_column, guess):
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



def check_6x6_box(current_board, current_row, current_column, guess):
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


def check_9x9_box(current_board, current_row, current_column, guess):
    """
    Ensure that there are no violations in the current box before updating this cell
    Returns true if there is no violation and false if a violation is found.

    Boxes numbered as follows:
    -------------------------
    |       |       |       |
    |   1   |   2   |   3   |
    |       |       |       |
    -------------------------
    |       |       |       |
    |   4   |   5   |   6   |
    |       |       |       |
    -------------------------
    |       |       |       |
    |   7   |   8   |   9   |
    |       |       |       |
    -------------------------
    """
    # Default value:
    quadrant = 0

    # First, determine which box we are in and need to check

    if current_row < 3:
        if current_column < 3:
            quadrant = 1
        elif current_column < 6:
            quadrant = 2
        else:
            quadrant = 3
    elif current_row < 6:
        if current_column < 3:
            quadrant = 4
        elif current_column < 6:
            quadrant = 5
        else:
            quadrant = 6
    else:
        if current_column < 3:
            quadrant = 7
        elif current_column < 6: 
            quadrant = 8
        else:
            quadrant = 9
    # print("The quadrant number is", quadrant)
    # Assign the box values to the appropriate quadrant
    if quadrant == 1:
        box_vals = [current_board[0][0], current_board[0][1], current_board[0][2], 
                    current_board[1][0], current_board[1][1], current_board[1][2],
                    current_board[2][0], current_board[2][1], current_board[2][2]]

    elif quadrant == 2:
        box_vals = [current_board[0][3], current_board[0][4], current_board[0][5], 
                    current_board[1][3], current_board[1][4], current_board[1][5],
                    current_board[2][3], current_board[2][4], current_board[2][5]]

    elif quadrant == 3:
        box_vals = [current_board[0][6], current_board[0][7], current_board[0][8], 
                    current_board[1][6], current_board[1][7], current_board[1][8],
                    current_board[2][6], current_board[2][7], current_board[2][8]]

    elif quadrant == 4:
        box_vals = [current_board[3][0], current_board[3][1], current_board[3][2], 
                    current_board[4][0], current_board[4][1], current_board[4][2],
                    current_board[5][0], current_board[5][1], current_board[5][2]]
    
    elif quadrant == 5:
        box_vals = [current_board[3][3], current_board[3][4], current_board[3][5], 
                    current_board[4][3], current_board[4][4], current_board[4][5],
                    current_board[5][3], current_board[5][4], current_board[5][5]]
    
    elif quadrant == 6:
        box_vals = [current_board[3][6], current_board[3][7], current_board[3][8], 
                    current_board[4][6], current_board[4][7], current_board[4][8],
                    current_board[5][6], current_board[5][7], current_board[5][8]]

    elif quadrant == 7:
        box_vals = [current_board[6][0], current_board[6][1], current_board[6][2], 
                    current_board[7][0], current_board[7][1], current_board[7][2],
                    current_board[8][0], current_board[8][1], current_board[8][2]]

    elif quadrant == 8:
        box_vals = [current_board[6][3], current_board[6][4], current_board[6][5], 
                    current_board[7][3], current_board[7][4], current_board[7][5],
                    current_board[8][3], current_board[8][4], current_board[8][5]]
    
    else: # quadrant == 9
        box_vals = [current_board[6][6], current_board[6][7], current_board[6][8], 
                    current_board[7][6], current_board[7][7], current_board[7][8],
                    current_board[8][6], current_board[8][7], current_board[8][8]]
    
    # print("The quadrant vals are:", box_vals, "and our guess is", guess)
    # print(guess in box_vals)
    
    # If we did not find a box violation, then it is a valid move
    if guess in box_vals:
        return False
    else:
        return True

