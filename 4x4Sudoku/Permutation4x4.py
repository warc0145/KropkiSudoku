'''
Name: Dylan Warcholik

File Name: Permutation4x4.py

Date Started: 8/25/25

Description:
Iterate through all 4x4 boards to confirm or disprove the following conjecture by brute force:
By making the following permutation: 1's become 2's, 2's become 3's, 3's become 1's, and 1's become 4's,
black dots become white dots, white dots become no-dots, and no-dots become black dots.
'''
from KropkiGenerator4x4 import solutions, kropki_solutions, find_horizontal_kropki_dots, find_vertical_kropki_dots

for i in range(len(solutions)):
    board = solutions[i]
    # Generate the blank form that will become the permuted board:
    new_board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for row in range(len(board)):
        for col in range(len(board)):

            # Now iterate through the original board and modify new_board to have the permuted form
            if board[row][col] == 1:
                new_board[row][col] = 2
            elif board[row][col] == 2:
                new_board[row][col] = 3
            elif board[row][col] == 3:
                new_board[row][col] = 1
            else: # board[row][col] == 4:
                new_board[row][col] = 4
    
    # Find the original board's kropki solution:
    original_k_sol = kropki_solutions[i]

    # Now modify it to the form we predict the permuted board will have:
    for dot_type in original_k_sol:
        for row in range(len(dot_type)):
            for col in range(len(dot_type[row])):
                if dot_type[row][col] == 1:
                    dot_type[row][col] = -1
                elif dot_type[row][col] == -1:
                    dot_type[row][col] = 0
                else: # dot_type[row][col] == 0
                    dot_type[row][col] = 1
    
    # Now generate the permuted board's ACTUAL kropki arrangement and compare to our prediction
    current_k_sol = (find_horizontal_kropki_dots(new_board), find_vertical_kropki_dots(new_board))
    if not (current_k_sol == original_k_sol):
        print("Solution number", i, "does not work with the permutation; See original board and new board:")
        print("OG:", board, "\nNew:", new_board)
        print("OG k_sol:", kropki_solutions[i], "\nNew k_sol:", current_k_sol)
    else:
        print("Works for solution number", i)