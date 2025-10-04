'''
Name: Dylan Warcholik

File Name: Mod3Sudoku.py

Date Started: 10/4/25

Description:
Alternate puzzle style, so that there are three dots with an even number of number pairs, such as how kropki applies to the 4x4.

0,1,2 represent the dots between two numbers, and each dot reveals the sum of the two digits in mod 3.
'''

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
start_board = [[1, 2, 3, 4, 5, 6], [4, 5, 6, 1, 2, 3], [2, 1, 4, 3, 6, 5], [3, 6, 5, 2, 1, 4], [5, 3, 1, 6, 4, 2], [6, 4, 2, 5, 3, 1]]
mod_dots = (find_horizontal_mod_dots[start_board]), find_vertical_mod_dots[start_board])
print(mod_dots)
