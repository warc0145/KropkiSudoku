'''
Name: Dylan Warcholik

File Name: Coloring.py

Date Started: 7/23/2025

Description:
Will assist in counting all of the ways to color a 4x4 sudoku. Unsure at the moment how or if it will relate to kropki dots.
'''
from SudokuPuzzleGenerator4x4 import solutions

def colorer(board_list):
    """
    This method will develop a dictionary where the key is a 4-tuple of 4-tuples of 2-tuples...
    It will contain four colors, and for each of which four locations which are stored as coordinates.
    (0,0) will be the top left cell, and (3,3) will be the bottom right cell
    """
    colorings = dict()

    for board in board_list:
        # Determine which number will be associated with each "color"
        first, second, third, fourth = board[0][0], board[0][1], board[0][2], board[0][3]
        
        first_lst = []
        second_lst = []
        third_lst = []
        fourth_lst = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == first:
                    first_lst.append((i,j))
                elif board[i][j] == second:
                    second_lst.append((i,j))
                elif board[i][j] == third:
                    third_lst.append((i,j))
                else: # board[i][j] == fourth
                    fourth_lst.append((i,j))
        
        # Now we know the coordinates of all numbers, add it to the dictionary or increment the count
        this_sol = ((first_lst[0], first_lst[1], first_lst[2], first_lst[3]), 
                    (second_lst[0], second_lst[1], second_lst[2], second_lst[3]), 
                    (third_lst[0], third_lst[1], third_lst[2], third_lst[3]), 
                    (fourth_lst[0], fourth_lst[1], fourth_lst[2], fourth_lst[3]))
        if this_sol in colorings:
            # If we have seen this arrangement, increment the count
            colorings[this_sol] += 1
        else:
            # Otherwise, add it with a count of 1
            colorings[this_sol] = 1
    return colorings

sudoku_colorings = colorer(solutions)