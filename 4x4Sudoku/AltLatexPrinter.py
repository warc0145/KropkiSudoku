
'''
Name: Dylan Warcholik

File Name: AltLatexPrinter.py

Date Started: 5/30/2025

Description:
Uses previous existing Kropki Arrangements and prints it out in the form that Latex will take as two arguments.
Takes up less lines in printing by printing the horizontal dots in one line rather than one row per line, as well as for the vertical dots.
'''
from KropkiGenerator4x4 import kropki_solutions

def latex_print(sol):
    '''
    Takes in a Kropki arrangement and outputs in a form that Latex will use for the \\blankkropki macro I made
    '''
    print("\\begin{tikzpicture}")
    print("    \\blankkropki{")
    for type in sol: # horizontal and vertical
        for row in range(len(type)):
            if row == 0 and type == sol[0]:
                print(" "*8, end="")
            for col in range(len(type[row])):
                print(str(type[row][col]), end="")
                if not(col == (len(type[row]) -1) and row == (len(type) - 1)):
                    print(", ", end="")
            # print("")
        print("}")
        if type == sol[0]:
            print("        {",end="")
    print("\\end{tikzpicture}")

for sol in kropki_solutions[:10]:
    latex_print(sol)
