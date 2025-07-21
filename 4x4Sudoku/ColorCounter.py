'''
Name: Dylan Warcholik

File Name: ColorCounter.py

Date Started: 5/26/25

Description:
This program will produce information summarizing the appearance of white and black dots in all of the 4x4 arrangements
'''
from NonUniqueKropkiGenerator.py import non_unique_kropki_solutions
from KropkiGenerator4x4.py import kropki_solutions

def white_counter(solution):
    """
    Takes in a Kropki arrangement and returns the number of white dots present.
    Called by unique_counter and non_unique_counter

    Solution will be a tuple with a 4x3 array then a 3x4 array
    """
    white_dot_count = 0
    for type in solution: # Considers horizontal dots then vertical dots
        for row in type:
            for col in row:
                if col == -1:
                    white_dot_count += 1
    return white_dot_count
        
    

def black_counter(solution):
    """
    Takes in a Kropki arrangement and returns the number of black dots present.
    Called by unique_counter and non_unique_counter
    Solution will be a tuple with a 4x3 array then a 3x4 array
    """
    black_dot_count = 0
    for type in solution: # Considers horizontal dots then vertical dots
        for row in type:
            for col in row:
                if col == 1:
                    black_dot_count += 1
    return black_dot_count

def non_unique_counter(solutions):
    """
    Will go through the non-unique set of Kropki Arrangements (where white dots are present between 1 and 2), and produce dictionaries
    that describe the number of white and black dots found across all puzzles
    """
    non_unique_white = dict()
    non_unique_black = dict()

    for solution in non_unique_kropki_solutions:
        white_count = white_counter(solution)
        black_count = black_counter(solution)

        # Update white dict
        if white_count in non_unique_white:
            non_unique_white[white_count] += 1
        else:
            non_unique_white[white_count] = 1
        
        # Update black dict
        if black_count in non_unique_black:
            non_unique_black[black_count] += 1
        else:
            non_unique_black[black_count] = 1
    
    

    
def unique_counter(solutions):
    """
    Will go through the unique set of Kropki Arrangements (where black dots are present between 1 and 2), and produce dictionaries
    that describe the number of white and black dots found across all puzzles
    """
    unique_white = dict()
    unique_black = dict()

    for solution in unique_kropki_solutions:
        white_count = white_counter(solution)
        black_count = black_counter(solution)

        # Update white dict
        if white_count in unique_white:
            unique_white[white_count] += 1
        else:
            unique_white[white_count] = 1
        
        # Update black dict
        if black_count in unique_black:
            unique_black[black_count] += 1
        else:
            unique_black[black_count] = 1

unique_counter()
non_unique_counter()
