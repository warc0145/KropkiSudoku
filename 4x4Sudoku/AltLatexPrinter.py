
'''
Name: Dylan Warcholik

File Name: AltLatexPrinter.py

Date Started: 5/30/2025

Description:
Uses previous existing Kropki Arrangements and prints it out in the form that Latex will take as two arguments.
Takes up less lines in printing by printing the horizontal dots in one line rather than one row per line, as well as for the vertical dots.
New addition as of 7/21/25: A method that will print out in latex form but with the full solution filled in.
'''
# from KropkiGenerator4x4 import kropki_solutions
from Coloring import sudoku_colorings

def latex_print(kropki_arrangement):
    """
    Takes in a Kropki arrangement and outputs in a form that Latex will use for the \\blankkropki macro I made
    """
    print("\\begin{tikzpicture}")
    print("    \\blankkropki{")
    for type in kropki_arrangement: # horizontal and vertical
        for row in range(len(type)):
            if row == 0 and type == kropki_arrangement[0]:
                print(" "*8, end="")
            for col in range(len(type[row])):
                print(str(type[row][col]), end="")
                if not(col == (len(type[row]) -1) and row == (len(type) - 1)):
                    print(", ", end="")
            # print("")
        print("}")
        if type == kropki_arrangement[0]:
            print("        {",end="")
    print("\\end{tikzpicture}")

def solved_latex_print(solution, kropki_arrangement):
    """
    Takes in a 4x4 solution and a Kropki arrangement and outputs in a form that Latex will use for the \\kropki macro I made
    """
    print("\\begin{tikzpicture}")
    print("    \\kropki{")
    print(" " * 8, end="")

    # printing the cell solutions in the required format

    for row in range(len(solution)):
        if row == 2: # If we are at the half way point, return to make two lines for easier reading
            print("\n" + " "*8, end="")
        for col in range(len(solution[row])):
            print(solution[row][col], end="")
            if not (row == (len(solution) - 1) and col == (len(solution[row]) - 1)):
                print(", ", end="")
    print("}{")

    # Now printing the arrangement in the required format

    for type in kropki_arrangement: # horizontal and vertical
        for row in range(len(type)):
            if row == 0 and type == kropki_arrangement[0]:
                print(" "*8, end="")
            for col in range(len(type[row])):
                print(str(type[row][col]), end="")
                if not(col == (len(type[row]) -1) and row == (len(type) - 1)):
                    print(", ", end="")
            # print("")
        print("}")
        if type == kropki_arrangement[0]:
            print("        {",end="")

    print("\\end{tikzpicture}")


def color_printer(coloring):
    """
    Takes in a coloring and prints out the latex macro form.
    """
    print("\\sudokuColor")
    for color in coloring: # Four colors, each have four locations
        print("    {",end="")
        for location in color: # Iterate through the four locations
            print(str(location[0]) + "/" + str(location[1]), end="")
            if location is not color[-1]: 
                print(", ", end="")
            else:
                print("}")


# for sol in kropki_solutions[:10]:
#     latex_print(sol)
ex_sol = [[1, 2, 3, 4], [3, 4, 1, 2], [2, 1, 4, 3], [4, 3, 2, 1]]
ex_kropki = ([[1, -1, -1], [-1, 0, 1], [1, 0, -1], [-1, -1, 1]], [[0, 1, 0, 1], [-1, 0, 0, -1], [1, 0, 1, 0]])
# solved_latex_print(ex_sol, ex_kropki)

for each in sudoku_colorings:
    color_printer(each)