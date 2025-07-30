'''
Name: Dylan Warcholik

File Name: NonUniqueExploration.py

Date Started: 5/20/25

Description:
This program will explore the 8 Kropki arrangements that resort in non-unique solutions.
'''
from NonUniqueKropkiGenerator import non_unique_kropki_solutions as kropki_solutions
from SudokuPuzzleGenerator4x4 import solutions, print_board

duplicate_arrangements = []
for i in range(len(kropki_solutions)):
    num_dots = 0 # Will be used to count the number of dots in the repeating solutions
    for direction in kropki_solutions[i]: # Will go through the horizontal dots then the vertical dots
        for row in direction: 
            for column in row:
                if not (column == 0):
                  num_dots += 1
    count = kropki_solutions.count(kropki_solutions[i])
    if count > 1:
        duplicate_arrangements.append(kropki_solutions[i])
        # print("The Kropki Arrangement", kropki_solutions[i], "appears", count, "times. It has", num_dots,"Kropki dots. Here is a board with that arrangement:")
        # print_board(solutions[i])

# Consider all duplicate_arrangements, and print out the two boards that align with those arrangements
# for sol in duplicate_arrangements:
#     print("For the arrangement", sol, "Here are the two solutions:")
#     for i in range(len(kropki_solutions)):
#         if kropki_solutions[i] == sol:
#             print_board(solutions[i])
    
