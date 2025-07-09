"""
Name: Dylan Warcholik

File Name: WhiteDiamond.py

Date Started: 7/9/2025

Description:
Narrows down all of the Kropki arrangements to a list of only those that contain a "white diamond" of dots.
"""
from KropkiGenerator4x4 import kropki_solutions
from AltLatexPrinter import latex_print

white_diamonds = []
white_diamonds_1 = []
white_diamonds_2 = []
white_diamonds_3 = []
white_diamonds_4 = []
white_diamonds_5 = []
white_diamonds_6 = []
white_diamonds_7 = []
white_diamonds_8 = []
white_diamonds_9 = []
multiple_diamonds = []
white_cells = []

for k_sol in kropki_solutions:
    count = 0
    valid = False
    # k_sol is three layers deep. First, horizontal and vertical dots, then the row or column within the type of dots, then the position in the row or column

    # Here, I check for diamonds in which the top is in the top row:
    if k_sol[0][0][0] == -1 and k_sol[0][1][0] == -1: # top and bottom of diamond
        if k_sol[1][0][0] == -1 and k_sol[1][0][1] == -1: # Sides of diamond
            valid = True
            white_diamonds_1.append(k_sol)
            count += 1
    if k_sol[0][0][1] == -1 and k_sol[0][1][1] == -1: # top and bottom of diamond
        if k_sol[1][0][1] == -1 and k_sol[1][0][2] == -1: # Sides of diamond
            valid = True
            white_diamonds_2.append(k_sol)
            count += 1
    if k_sol[0][0][2] == -1 and k_sol[0][1][2] == -1: # top and bottom of diamond
        if k_sol[1][0][2] == -1 and k_sol[1][0][3] == -1: # Sides of diamond
            valid = True
            white_diamonds_3.append(k_sol)
            count += 1

    # Here, I check for diamonds in which the top is in the second row:
    if k_sol[0][1][0] == -1 and k_sol[0][2][0] == -1: # top and bottom of diamond
        if k_sol[1][1][0] == -1 and k_sol[1][1][1] == -1: # Sides of diamond
            valid = True
            white_diamonds_4.append(k_sol)
            count += 1
    if k_sol[0][1][1] == -1 and k_sol[0][2][1] == -1: # top and bottom of diamond
        if k_sol[1][1][1] == -1 and k_sol[1][1][2] == -1: # Sides of diamond
            valid = True
            white_diamonds_5.append(k_sol)
            count += 1
    if k_sol[0][1][2] == -1 and k_sol[0][2][2] == -1: # top and bottom of diamond
        if k_sol[1][1][2] == -1 and k_sol[1][1][3] == -1: # Sides of diamond
            valid = True
            white_diamonds_6.append(k_sol)
            count += 1

    # Here, I check for diamonds in which the top is in the third row:
    if k_sol[0][2][0] == -1 and k_sol[0][3][0] == -1: # top and bottom of diamond
        if k_sol[1][2][0] == -1 and k_sol[1][2][1] == -1: # Sides of diamond
            valid = True
            white_diamonds_7.append(k_sol)
            count += 1
    if k_sol[0][2][1] == -1 and k_sol[0][3][1] == -1: # top and bottom of diamond
        if k_sol[1][2][1] == -1 and k_sol[1][2][2] == -1: # Sides of diamond
            valid = True
            white_diamonds_8.append(k_sol)
            count += 1
    if k_sol[0][2][2] == -1 and k_sol[0][3][2] == -1: # top and bottom of diamond
        if k_sol[1][2][2] == -1 and k_sol[1][2][3] == -1: # Sides of diamond
            valid = True
            white_diamonds_9.append(k_sol)
            count += 1
    if valid:
       white_diamonds.append(k_sol)
    if count > 1:
        multiple_diamonds.append(k_sol)

print("The number of puzzles with at least one white diamond is", str(len(white_diamonds)))

print("#1", len(white_diamonds_1))
for s in white_diamonds_1:
    print(s)
print("#2", len(white_diamonds_2))
for s in white_diamonds_2:
    print(s)
print("#3", len(white_diamonds_3))
for s in white_diamonds_3:
    print(s)
print("#4", len(white_diamonds_4))
for s in white_diamonds_4:
    print(s)
print("#5", len(white_diamonds_5))
for s in white_diamonds_5:
    print(s)
print("#6", len(white_diamonds_6))
for s in white_diamonds_6:
    print(s)
print("#7", len(white_diamonds_7))
for s in white_diamonds_7:
    print(s)
print("#8", len(white_diamonds_8))
for s in white_diamonds_8:
    print(s)
print("#9", len(white_diamonds_9))
for s in white_diamonds_9:
    print(s)
print("Multiple:", len(multiple_diamonds))
for s in multiple_diamonds:
    latex_print(s)


for k_sol in kropki_solutions:
    # Checks if top left cell (of center four) is a "white cell"
    if k_sol[0][1][0] == -1 and k_sol[0][1][1] == -1: # Sides of the cell
        if k_sol[1][0][1] == -1 and k_sol[1][1][1] == -1: # top and bottom of the cell
            white_cells.append(k_sol)
    
    # Checks if top right cell (of center four) is a "white cell"
    elif k_sol[0][1][1] == -1 and k_sol[0][1][2] == -1: # Sides of the cell
        if k_sol[1][0][2] == -1 and k_sol[1][1][2] == -1: # top and bottom of the cell
            white_cells.append(k_sol)

    # Checks if bottom left cell (of center four) is a "white cell"
    elif k_sol[0][2][0] == -1 and k_sol[0][2][1] == -1: # Sides of the cell
        if k_sol[1][1][1] == -1 and k_sol[1][2][1] == -1: # top and bottom of the cell
            white_cells.append(k_sol)
    
    # Checks if bottom right cell (of center four) is a "white cell"
    elif k_sol[0][2][1] == -1 and k_sol[0][2][2] == -1: # Sides of the cell
        if k_sol[1][1][2] == -1 and k_sol[1][2][2] == -1: # top and bottom of the cell
            white_cells.append(k_sol)
print("White cells:", len(white_cells))
for s in white_cells:
    latex_print(s)