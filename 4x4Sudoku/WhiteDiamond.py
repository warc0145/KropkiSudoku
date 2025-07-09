"""
Name: Dylan Warcholik

File Name: WhiteDiamond.py

Date Started: 7/9/2025

Description:
Narrows down all of the Kropki arrangements to a list of only those that contain a "white diamond" of dots.
"""
from KropkiGenerator4x4 import kropki_solutions

white_diamonds = []

for k_sol in kropki_solutions:
    valid = False
    # k_sol is three layers deep. First, horizontal and vertical dots, then the row or column within the type of dots, then the position in the row or column

    # Here, I check for diamonds in which the top is in the top row:
    if k_sol[0][0][0] == -1 and k_sol[0][1][0] == -1: # top and bottom of diamond
        if k_sol[1][0][0] == -1 and k_sol[1][0][1] == -1: # Sides of diamond
            valid == True
    elif k_sol[0][0][1] == -1 and k_sol[0][1][1] == -1: # top and bottom of diamond
        if k_sol[1][0][1] == -1 and k_sol[1][0][2] == -1: # Sides of diamond
            valid == True
    elif k_sol[0][0][2] == -1 and k_sol[0][1][2] == -1: # top and bottom of diamond
        if k_sol[1][0][2] == -1 and k_sol[1][0][3] == -1: # Sides of diamond
            valid == True

    # Here, I check for diamonds in which the top is in the second row:
    if k_sol[0][1][0] == -1 and k_sol[0][2][0] == -1: # top and bottom of diamond
        if k_sol[1][1][0] == -1 and k_sol[1][1][1] == -1: # Sides of diamond
            valid == True
    elif k_sol[0][1][1] == -1 and k_sol[0][2][1] == -1: # top and bottom of diamond
        if k_sol[1][1][1] == -1 and k_sol[1][1][2] == -1: # Sides of diamond
            valid == True
    elif k_sol[0][1][2] == -1 and k_sol[0][2][2] == -1: # top and bottom of diamond
        if k_sol[1][1][2] == -1 and k_sol[1][1][3] == -1: # Sides of diamond
            valid == True

    # Here, I check for diamonds in which the top is in the third row:
    if k_sol[0][2][0] == -1 and k_sol[0][3][0] == -1: # top and bottom of diamond
        if k_sol[1][2][0] == -1 and k_sol[1][2][1] == -1: # Sides of diamond
            valid == True
    elif k_sol[0][2][1] == -1 and k_sol[0][3][1] == -1: # top and bottom of diamond
        if k_sol[1][2][1] == -1 and k_sol[1][2][2] == -1: # Sides of diamond
            valid == True
    elif k_sol[0][2][2] == -1 and k_sol[0][3][2] == -1: # top and bottom of diamond
        if k_sol[1][2][2] == -1 and k_sol[1][2][3] == -1: # Sides of diamond
            valid == True
  
    if valid == True:
       white_diamonds.append(k_sol)

print("The number of puzzles with at least one white diamond is", str(len(white_diamonds)))
for s in white_diamonds:
    print(s)
