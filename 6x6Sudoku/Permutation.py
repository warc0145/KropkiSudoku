'''
Name: Dylan Warcholik

File: Permutation.py

Date Started: 8/25/25

Description:
Will consider all permutations of numbers and if there is any permutation that maintains the relationship between cells, or makes
for an interesting bijection (i.e. how there is a permutation for 4x4 that reverses the color of dots)
'''
import itertools
from PuzzleGenerator6x6 import print_board
from KropkiGenerator6x6 import find_horizontal_kropki_dots, find_vertical_kropki_dots

### The "first" solution has every pair of numbers adjacent to each other, so is a valid board to check permutations on :)
### The following block is how I produced the first line in the format I use it in from solutions.txt (which has 2000 solutions)
# with open("6x6Sudoku/solutions.txt", 'r') as f:
#     line_num = 0
#     for line in f:
#         line_num += 1
#         starting_solution = [[line[2], line[5], line[8], line[11], line[14], line[17]],
#                             [line[22], line[25], line[28], line[31], line[34], line[37]],
#                             [line[42], line[45], line[48], line[51], line[54], line[57]],
#                             [line[62], line[65], line[68], line[71], line[74], line[77]],
#                             [line[82], line[85], line[88], line[91], line[94], line[97]],
#                             [line[102], line[105], line[108], line[111], line[114], line[117]]]
#         if line_num == 1:
#             for i in range(len(starting_solution)):
#                 for j in range(len(starting_solution[i])):
#                     starting_solution[i][j] = int(starting_solution[i][j])
#             print(starting_solution)

sol = [[1, 2, 3, 4, 5, 6], [4, 5, 6, 1, 2, 3], [2, 1, 4, 3, 6, 5], 
        [3, 6, 5, 2, 1, 4], [5, 3, 1, 6, 4, 2], [6, 4, 2, 5, 3, 1]]

k_sol = (find_horizontal_kropki_dots(sol), find_vertical_kropki_dots(sol))

# Generate all permutations of 1,2,3,4,5,6
permutation_lst = list(itertools.permutations([1,2,3,4,5,6]))

# A blank list that will contain all "Successful" permutations
valid_permutations = []
non_valid_count = 0

for permutation in permutation_lst:
    # Generate a blank board that will take on the permuted form of our starting solution:
    new_board = [[0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0]]

    for row in range(len(sol)):
        for col in range(len(sol)):
            current_val = sol[row][col]
            val_as_index = current_val - 1 # This will be the index of permutation we want to change this val to
            new_board[row][col] = permutation[val_as_index]

    # print("Permutation:", permutation)
    # print(sol)
    # print(new_board)

    # Now, generate our new k_sol
    new_k_sol = (find_horizontal_kropki_dots(new_board), find_vertical_kropki_dots(new_board))

    # Checks if there is a permutation that does not modify the kropki arrangement
    if (new_k_sol == k_sol) and not (new_board == sol):
        print("Surprise! This permutation led to the same kropki arrangement!")
        print("OG:", sol, "\nVS:", new_board)
        print((1,2,3,4,5,6))
        print(permutation)
    else:
        ### I don't expect the above to occur, so really we want to produce a modified kropki arrangement and see if it ever occurs
        # # print(new_k_sol)

        ### Checks if there is a permutation that rotates the dots (b->w->x->b), but there isn't
        # for dot_type in new_k_sol:
        #     for row in range(len(dot_type)):
        #         for col in range(len(dot_type[row])):
        #             if dot_type[row][col] == 1:
        #                 dot_type[row][col] = -1
        #             elif dot_type[row][col] == -1:
        #                 dot_type[row][col] = 0
        #             else: # dot_type[row][col] == 0
        #                 dot_type[row][col] = 1
        # # print(new_k_sol)
        # # print(k_sol)
        # # print()

        ### Checks if there is a permutation that flips the dots (b->w, w->b), but there isn't :(
        for dot_type in new_k_sol:
            for row in range(len(dot_type)):
                for col in range(len(dot_type[row])):
                    if dot_type[row][col] == 1:
                        dot_type[row][col] = -1
                    elif dot_type[row][col] == -1:
                        dot_type[row][col] = 1
                    else: # dot_type[row][col] == 0
                        dot_type[row][col] = 0

        # After modifying new_k_sol to our predicted form, compare to the original k_sol:
        if new_k_sol == k_sol:
            print("Yay! This permutation led to the permuted kropki arrangement!")
            print("OG:", sol, "\nVS:", new_board)
            print((1,2,3,4,5,6))
            print(permutation)
            valid_permutations.append(permutation)
        else:
            non_valid_count += 1


print("There were", len(valid_permutations), "valid permutations; here they are:")
for permutation in valid_permutations:
    print(permutation)

print("There were", non_valid_count, "non-valid permutations.")