"""
Name: Dylan Warcholik

File Name: ReverseAndSolve.py

Date Started: 7/13/2025

Description:
Because of the similarity of the number of puzzles with white diamonds and black diamonds, this program will take the list, reverse the color of dots on every puzzle,
and observe if the puzzle is still able to be solved (uniquely).
"""
from AnyDiamond import diamond_list, no_diamond_list, full_cell_list, no_full_cells_list

def color_reverser(board):
    for dot_type in range(len(board)):
        # Allows iterating through horizontal and vertical dots
        for row in range(len(board[dot_type])):
            for col in range(len(board[dot_type][row])):
                if abs(board[dot_type][row][col]) == 1:
                    board[dot_type][row][col] *= -1 
                    # This is to say, for every dot, reverse the color

# print(diamond_list[0])
# color_reverser(diamond_list[0])
# print(diamond_list[0])