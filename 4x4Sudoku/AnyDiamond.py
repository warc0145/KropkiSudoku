"""
Name: Dylan Warcholik

File Name: BlackDiamond.py

Date Started: 7/13/2025

Description:
Narrows down all of the Kropki arrangements to a list of only those that contain a "black diamond" or a "white diamond" of dots.
"""
from KropkiGenerator4x4 import kropki_solutions
from AltLatexPrinter import latex_print

diamond_list = []
no_diamond_list = []
full_cell_list = []
no_full_cells_list = []

for k_sol in kropki_solutions:
    count = 0
    valid = False
    # k_sol is three layers deep. First, horizontal and vertical dots, then the row or column within the type of dots, then the position in the row or column

    ### WHITE DIAMOND
    # Here, I check for diamonds in which the top is in the top row:
    if k_sol[0][0][0] == -1 and k_sol[0][1][0] == -1: # top and bottom of diamond
        if k_sol[1][0][0] == -1 and k_sol[1][0][1] == -1: # Sides of diamond
            valid = True
            count += 1
    elif k_sol[0][0][1] == -1 and k_sol[0][1][1] == -1: # top and bottom of diamond
        if k_sol[1][0][1] == -1 and k_sol[1][0][2] == -1: # Sides of diamond
            valid = True
            count += 1
    elif k_sol[0][0][2] == -1 and k_sol[0][1][2] == -1: # top and bottom of diamond
        if k_sol[1][0][2] == -1 and k_sol[1][0][3] == -1: # Sides of diamond
            valid = True
            count += 1

    # Here, I check for diamonds in which the top is in the second row:
    elif k_sol[0][1][0] == -1 and k_sol[0][2][0] == -1: # top and bottom of diamond
        if k_sol[1][1][0] == -1 and k_sol[1][1][1] == -1: # Sides of diamond
            valid = True
            count += 1
    elif k_sol[0][1][1] == -1 and k_sol[0][2][1] == -1: # top and bottom of diamond
        if k_sol[1][1][1] == -1 and k_sol[1][1][2] == -1: # Sides of diamond
            valid = True
            count += 1
    elif k_sol[0][1][2] == -1 and k_sol[0][2][2] == -1: # top and bottom of diamond
        if k_sol[1][1][2] == -1 and k_sol[1][1][3] == -1: # Sides of diamond
            valid = True
            count += 1

    # Here, I check for diamonds in which the top is in the third row:
    elif k_sol[0][2][0] == -1 and k_sol[0][3][0] == -1: # top and bottom of diamond
        if k_sol[1][2][0] == -1 and k_sol[1][2][1] == -1: # Sides of diamond
            valid = True
            count += 1
    elif k_sol[0][2][1] == -1 and k_sol[0][3][1] == -1: # top and bottom of diamond
        if k_sol[1][2][1] == -1 and k_sol[1][2][2] == -1: # Sides of diamond
            valid = True
            count += 1
    elif k_sol[0][2][2] == -1 and k_sol[0][3][2] == -1: # top and bottom of diamond
        if k_sol[1][2][2] == -1 and k_sol[1][2][3] == -1: # Sides of diamond
            valid = True
            count += 1

    

    ### BLACK DIAMONDS
    # Here, I check for diamonds in which the top is in the top row:
    elif k_sol[0][0][0] == 1 and k_sol[0][1][0] == 1: # top and bottom of diamond
        if k_sol[1][0][0] == 1 and k_sol[1][0][1] == 1: # Sides of diamond
            valid = True
            count += 1
    elif k_sol[0][0][1] == 1 and k_sol[0][1][1] == 1: # top and bottom of diamond
        if k_sol[1][0][1] == 1 and k_sol[1][0][2] == 1: # Sides of diamond
            valid = True
            count += 1
    elif k_sol[0][0][2] == 1 and k_sol[0][1][2] == 1: # top and bottom of diamond
        if k_sol[1][0][2] == 1 and k_sol[1][0][3] == 1: # Sides of diamond
            valid = True
            count += 1

    # Here, I check for diamonds in which the top is in the second row:
    elif k_sol[0][1][0] == 1 and k_sol[0][2][0] == 1: # top and bottom of diamond
        if k_sol[1][1][0] == 1 and k_sol[1][1][1] == 1: # Sides of diamond
            valid = True
            count += 1
    elif k_sol[0][1][1] == 1 and k_sol[0][2][1] == 1: # top and bottom of diamond
        if k_sol[1][1][1] == 1 and k_sol[1][1][2] == 1: # Sides of diamond
            valid = True
            count += 1
    elif k_sol[0][1][2] == 1 and k_sol[0][2][2] == 1: # top and bottom of diamond
        if k_sol[1][1][2] == 1 and k_sol[1][1][3] == 1: # Sides of diamond
            valid = True
            count += 1

    # Here, I check for diamonds in which the top is in the third row:
    elif k_sol[0][2][0] == 1 and k_sol[0][3][0] == 1: # top and bottom of diamond
        if k_sol[1][2][0] == 1 and k_sol[1][2][1] == 1: # Sides of diamond
            valid = True
            count += 1
    elif k_sol[0][2][1] == 1 and k_sol[0][3][1] == 1: # top and bottom of diamond
        if k_sol[1][2][1] == 1 and k_sol[1][2][2] == 1: # Sides of diamond
            valid = True
            count += 1
    elif k_sol[0][2][2] == 1 and k_sol[0][3][2] == 1: # top and bottom of diamond
        if k_sol[1][2][2] == 1 and k_sol[1][2][3] == 1: # Sides of diamond
            valid = True
            count += 1
    if valid:
        diamond_list.append(k_sol)
    else:
        no_diamond_list.append(k_sol)
 
print("The number of puzzles with at least one diamond is", str(len(diamond_list)))

print("Here are the puzzles without a diamond: (" + str(len(no_diamond_list)) + ")")
# for puzzle in no_diamond_list:
    # latex_print(puzzle)


for k_sol in kropki_solutions:
    ### SEARCHING FOR WHITE CELLS
    # Checks if top left cell (of center four) is a "white cell"
    if k_sol[0][1][0] == -1 and k_sol[0][1][1] == -1: # Sides of the cell
        if k_sol[1][0][1] == -1 and k_sol[1][1][1] == -1: # top and bottom of the cell
            full_cell_list.append(k_sol)
    
    # Checks if top right cell (of center four) is a "white cell"
    elif k_sol[0][1][1] == -1 and k_sol[0][1][2] == -1: # Sides of the cell
        if k_sol[1][0][2] == -1 and k_sol[1][1][2] == -1: # top and bottom of the cell
            full_cell_list.append(k_sol)

    # Checks if bottom left cell (of center four) is a "white cell"
    elif k_sol[0][2][0] == -1 and k_sol[0][2][1] == -1: # Sides of the cell
        if k_sol[1][1][1] == -1 and k_sol[1][2][1] == -1: # top and bottom of the cell
            full_cell_list.append(k_sol)
    
    # Checks if bottom right cell (of center four) is a "white cell"
    elif k_sol[0][2][1] == -1 and k_sol[0][2][2] == -1: # Sides of the cell
        if k_sol[1][1][2] == -1 and k_sol[1][2][2] == -1: # top and bottom of the cell
            full_cell_list.append(k_sol)

    ### SEARCHING FOR BLACK CELLS
    # Checks if top left cell (of center four) is a "black cell"
    elif k_sol[0][1][0] == 1 and k_sol[0][1][1] == 1: # Sides of the cell
        if k_sol[1][0][1] == 1 and k_sol[1][1][1] == 1: # top and bottom of the cell
            full_cell_list.append(k_sol)
    
    # Checks if top right cell (of center four) is a "black cell"
    elif k_sol[0][1][1] == 1 and k_sol[0][1][2] == 1: # Sides of the cell
        if k_sol[1][0][2] == 1 and k_sol[1][1][2] == 1: # top and bottom of the cell
            full_cell_list.append(k_sol)

    # Checks if bottom left cell (of center four) is a "black cell"
    elif k_sol[0][2][0] == 1 and k_sol[0][2][1] == 1: # Sides of the cell
        if k_sol[1][1][1] == 1 and k_sol[1][2][1] == 1: # top and bottom of the cell
            full_cell_list.append(k_sol)
    
    # Checks if bottom right cell (of center four) is a "black cell"
    elif k_sol[0][2][1] == 1 and k_sol[0][2][2] == 1: # Sides of the cell
        if k_sol[1][1][2] == 1 and k_sol[1][2][2] == 1: # top and bottom of the cell
            full_cell_list.append(k_sol)

print("Full cells:", len(full_cell_list))
