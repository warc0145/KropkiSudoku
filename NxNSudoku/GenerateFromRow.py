'''
Name: Dylan Warcholik
Date: 8/17/25
Description:
As I begin to explore counting unique Kropki arrangements on larger size puzzles, this file will include methods will enumerate 
the 4x4, 6x6, and 9x9 possible rows and determine the uniqueness of the Kropki arrangements of the rows for all sizes.
'''
import itertools # Quick combination generator
from PartialSudokuSolver import partial_sudoku_solver, solutions
from GenerateFromBox import find_horizontal_kropki_dots#, find_vertical_kropki_dots # Shouldn't need vertical dots


def row_generator_4x4():
    """
    Will generate all ways to solve a blank row using itertools.permutations, then will find each Kropki arrangement, and finally
    return a dictionary summarizing the uniqueness of kropki rows on this size board
    """
    # The following will record all kropki arrangements from the rows, counting the number of occurrances
    kropki_row_dict = dict()
    
    # Generate a list of rows:
    all_rows = list(itertools.permutations((1,2,3,4), 4))

    # Now, iterate through all rows, generate the kropki arrangement, and count it in the kropki_row_dict 
    for row in all_rows:
        kropki_row = find_horizontal_kropki_dots([row]) # Call on a list of one row to avoid error in find_horizontal
        if kropki_row in kropki_row_dict:
            kropki_row_dict[kropki_row] += 1
        else:
            kropki_row_dict[kropki_row] = 1
        # Need to compare indices 0,1, then 2,3, then 0,2 and 1,3
    return (all_rows, kropki_row_dict)


def row_generator_6x6():
    """
    Will generate all ways to solve a blank row using itertools.permutations, then will find each Kropki arrangement, and finally
    return a dictionary summarizing the uniqueness of kropki rows on this size board
    """
    # The following will record all kropki arrangements from the rows, counting the number of occurrances
    kropki_row_dict = dict()
    
    # Generate a list of rows:
    all_rows = list(itertools.permutations((1,2,3,4,5,6), 6))

    # Now, iterate through all rows, generate the kropki arrangement, and count it in the kropki_row_dict 
    for row in all_rows:
        kropki_row = find_horizontal_kropki_dots([row]) # Call on a list of one row to avoid error in find_horizontal
        if kropki_row in kropki_row_dict:
            kropki_row_dict[kropki_row] += 1
        else:
            kropki_row_dict[kropki_row] = 1
        # Need to compare indices 0,1, then 2,3, then 0,2 and 1,3
    return (all_rows, kropki_row_dict)


def row_generator_9x9():
    """
    Will generate all ways to solve a blank row using itertools.permutations, then will find each Kropki arrangement, and finally
    return a dictionary summarizing the uniqueness of kropki rows on this size board
    """
    # The following will record all kropki arrangements from the rows, counting the number of occurrances
    kropki_row_dict = dict()
    
    # Generate a list of rows:
    all_rows = list(itertools.permutations((1,2,3,4,5,6,7,8,9), 9))

    # Now, iterate through all rows, generate the kropki arrangement, and count it in the kropki_row_dict 
    for row in all_rows:
        kropki_row = find_horizontal_kropki_dots([row]) # Call on a list of one row to avoid error in find_horizontal
        if kropki_row in kropki_row_dict:
            kropki_row_dict[kropki_row] += 1
        else:
            kropki_row_dict[kropki_row] = 1
        # Need to compare indices 0,1, then 2,3, then 0,2 and 1,3
    return (all_rows, kropki_row_dict)



print("Generating 4x4 dictionary...")
rows_4, dict_4 = row_generator_4x4()
count_dict_4 = dict()
for value in dict_4.values():
    if value in count_dict_4:
        count_dict_4[value] += 1
    else:
        count_dict_4[value] = 1
print(count_dict_4) # To confirm count is correct: "Sum =", sum(key * val for key,val in count_dict_4.items())


print("\n\nGenerating 6x6 dictionary...")
rows_6, dict_6 = row_generator_6x6()
count_dict_6 = dict()
for value in dict_6.values():
    if value in count_dict_6:
        count_dict_6[value] += 1
    else:
        count_dict_6[value] = 1
print(count_dict_6) # To confirm count is correct: "Sum =", sum(key * val for key,val in count_dict_6.items())


print("\n\nGenerating 9x9 dictionary...")
rows_9, dict_9 = row_generator_9x9()
count_dict_9 = dict()
for value in dict_9.values():
    if value in count_dict_9:
        count_dict_9[value] += 1
    else:
        count_dict_9[value] = 1
print(count_dict_9)


print("4 max:", max(count_dict_4.keys()))
print("6 max:", max(count_dict_6.keys()))
print("9 max:", max(count_dict_9.keys()))
