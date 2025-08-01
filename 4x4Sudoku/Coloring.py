'''
Name: Dylan Warcholik

File Name: Coloring.py

Date Started: 7/23/2025

Description:
Will assist in counting all of the ways to color a 4x4 sudoku. Unsure at the moment how or if it will relate to kropki dots.
'''
from SudokuPuzzleGenerator4x4 import solutions
from NonUniqueKropkiGenerator import non_unique_boards
from SolveWithKropki import kropki_solver
from BlackDiamond import black_cells
from WhiteDiamond import white_cells
from AltLatexPrinter import color_printer

def colorer(board_list):
    """
    This method will develop a dictionary where the key is a 4-tuple of 4-tuples of 2-tuples...
    It will contain four colors, and for each of which four locations which are stored as coordinates.
    (0,0) will be the top left cell, and (3,3) will be the bottom right cell

    board_list, passed to the method, will be a list of completed 4x4 sudoku boards.
    """
    # Create a blank dictionary that will store a 4-tuple of 4-tuples of 2-tuples; the outer tuple organizing the colors,
    # the middle tuple storing coordinate points, and the inner tuple being the x,y (or i,j) of the coordinates
    colorings = dict()

    for board in board_list:
        # Determine which number will be associated with each "color"
        first, second, third, fourth = board[0][0], board[0][1], board[0][2], board[0][3]
        
        # Create empty lists that will store the coordinates of these colors
        first_lst = []
        second_lst = []
        third_lst = []
        fourth_lst = []

        # Iterate through the board adding the coordinates of tiles with the same color to the appropriate list
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
        # print("Using the board", board)
        # print("Our lists:")
        # print(first_lst, "\n", second_lst, "\n", third_lst, "\n", fourth_lst)
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

# sudoku_colorings = colorer(solutions)
# print("Now coloring boards with non unique arrangements:", non_unique_boards)
# non_unique_colorings = colorer(non_unique_boards)
# print(non_unique_colorings)

# finding the colorings of all boards with a black cell:
black_cell_boards = []
for s in black_cells:
    black_cell_boards.append(kropki_solver([[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]],
                                            s, 0, 0, [])[0])
    # The [0] indexing at the end returns the first element in the list that is returned by kropki solver;
    # kropki_solver returns a list of all valid solutions, and these arrangements all have one solution, so the list has one element
black_colorings = colorer(black_cell_boards)
# print("Colorings of puzzles with black cells:", black_colorings)

# Now latex print the colorings:
print("Colorings of boards with black cells:")
for b_coloring in black_colorings:
    print(f"\\paragraph{{The following coloring appears {black_colorings[b_coloring]} times}}")
    color_printer(b_coloring)

# finding the colorings of all boards with a whitecell:
white_cell_boards = []
for s in white_cells:
    white_cell_boards.append(kropki_solver([[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]],
                                            s, 0, 0, [])[0])
    # The [0] indexing at the end returns the first element in the list that is returned by kropki solver;
    # kropki_solver returns a list of all valid solutions, and these arrangements all have one solution, so the list has one element
white_colorings = colorer(white_cell_boards)
# print("Colorings of puzzles with white cells:", white_colorings)

# Now latex print the colorings:
print("Colorings of boards with white cells:")
for w_coloring in white_colorings:
    print(f"\\paragraph{{The following coloring appears {white_colorings[w_coloring]} times}}")
    color_printer(w_coloring)