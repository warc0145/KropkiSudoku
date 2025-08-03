'''
Name: Dylan Warcholik

File Name: ReverseAndSolve.py

Date Started: 7/13/2025

Description:
Because of the similarity of the number of puzzles with white diamonds and black diamonds, this program will take the list, reverse the color of dots on every puzzle,
and observe if the puzzle is still able to be solved (uniquely).
'''
from AnyDiamond import diamond_list, no_diamond_list, full_cell_list, no_full_cells_list
from SolveWithKropki import kropki_solver
from AltLatexPrinter import latex_print
from SudokuPuzzleGenerator4x4 import solutions
from KropkiGenerator4x4 import kropki_solutions

def color_reverser(kropki):
    """
    Takes in a Kropki Arrangement and returns a new one where all existing dots have had their colors switched
    The returned item is a tuple of two 2-dimensional arrays.
    """
    new_kropki = ([[0,0,0],[0,0,0],[0,0,0],[0,0,0]],[[0,0,0,0],[0,0,0,0],[0,0,0,0]])
    for dot_type in range(len(kropki)):
        # Allows iterating through horizontal and vertical dots
        for row in range(len(kropki[dot_type])):
            for col in range(len(kropki[dot_type][row])):
                if abs(kropki[dot_type][row][col]) == 1:
                    new_kropki[dot_type][row][col] = kropki[dot_type][row][col] * -1 
                    # This is to say, for every dot, reverse the color and put that in new_kropki
    return new_kropki

# print(diamond_list[0])
# color_reverser(diamond_list[0])
# print(diamond_list[0])
blank_board = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
fun_solutions = []


for i in range(len(diamond_list)):
    k_sol = diamond_list[i]
    k_copy = color_reverser(k_sol)
    blank_board = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]

    all_solutions = kropki_solver(blank_board, k_copy, 0, 0, [])
    # print(i, "has", len(all_solutions), "solutions")
    if len(all_solutions) > 0:
        fun_solutions.append((k_sol, k_copy))

print("There are", len(fun_solutions), "fun solutions (puzzles with diamonds that are reversible... so 12 and 12)")
for sol in fun_solutions:
    latex_print(sol[0])
    latex_print(sol[1])
    print("\\paragraph{\\\\}")

# for sol in fun_solutions:
#     num_sols = len(kropki_solver([[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]], sol[1], 0, 0, []))
#     print(num_sols)

# Now let's see how many of the 288 puzzles are solvable when colors are reversed:
# reversible_boards = []
# for i in range(len(solutions)):
#     print("Checking board #", i)
#     k_sol = kropki_solutions[i]
#     k_copy = color_reverser(k_sol)
#     blank_board = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]

#     all_solutions = kropki_solver(blank_board, k_copy, 0, 0, [])
#     # print(i, "has", len(all_solutions), "solutions")
#     if len(all_solutions) > 0:
    
#         reversible_boards.append((k_sol, k_copy))
#         print("board #", i, "has", len(all_solutions), "solutions. Appending... Now there are", len(reversible_boards))
# print("There are", len(reversible_boards), "reversible boards")