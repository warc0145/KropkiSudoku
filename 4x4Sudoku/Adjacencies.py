'''
Name: Dylan Warcholik

File Name: Adjacencies.py

Date Started: 10/15/2025

Description:
Will check what portion of the puzzles has all combinations of adjacent numbers, versus only some.

Prints a dictionary where the key is a tuple of strings representing the number combinations, and the 
value is the number of puzzles with all of those combinations.
{('12', '13', '14', '23', '24', '34'): 264, ('12', '14', '23', '34'): 8, ('12', '13', '24', '34'): 8, ('13', '14', '23', '24'): 8}
'''

from SudokuPuzzleGenerator4x4 import solutions

adj_dict = dict()

for sol in solutions:
    curr_set = set()
    # print(sol)
    # Include horizontal adjacencies:
    for i in range(len(sol)):
        for j in range(len(sol)-1):
            curr_adj = (str(sol[i][j]), str(sol[i][j+1]))
            curr_sorted = sorted(curr_adj)
            curr_set.add(curr_sorted[0]+curr_sorted[1])
    
    # Include horizontal adjacencies:
    for i in range(len(sol)-1):
        for j in range(len(sol)):
            curr_adj = (str(sol[i][j]), str(sol[i+1][j]))
            curr_sorted = sorted(curr_adj)
            curr_set.add(curr_sorted[0]+curr_sorted[1])

    set_tuple = tuple(combo for combo in sorted(curr_set))
    

    # print(set_tuple)
    if set_tuple in adj_dict:
        adj_dict[set_tuple] += 1
    else:
        adj_dict[set_tuple] = 1

print(adj_dict)

