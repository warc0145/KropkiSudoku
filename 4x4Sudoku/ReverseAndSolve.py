'''
Name: Dylan Warcholik

File Name: ReverseAndSolve.py

Date Started: 7/13/2025

Description:
Because of the similarity of the number of puzzles with white diamonds and black diamonds, this program will take the list, reverse the color of dots on every puzzle,
and observe if the puzzle is still able to be solved (uniquely).
'''
from AnyDiamond import diamond_list, no_diamond_list, full_cell_list, no_full_cells_list
from SolveWithKropki import blank_board, kropki_solver
from AltLatexPrinter import latex_print

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
fun_solutions = []
for k_sol in diamond_list:
    print("Reversing and solving the solution", k_sol)
    color_reverser(k_sol)
    solutions = kropki_solver(blank_board, k_sol, 0, 0)
    if len(solutions) > 0:
        fun_solutions.append(k_sol)

print("There are", len(fun_solutions), "fun solutions")
for sol in fun_solutions:
    latex_print(k_sol)
