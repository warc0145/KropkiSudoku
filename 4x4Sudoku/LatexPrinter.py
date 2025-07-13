'''
Name: Dylan Warcholik

File Name: LatexPrinter.py

Date Started: 5/30/2025

Description:
Uses previous existing Kropki Arrangements and prints it out in the form that Latex will take as two arguments
'''
from KropkiGenerator4x4 import kropki_solutions

def latex_print(sol):
    '''
    Takes in a Kropki arrangement and outputs in a form that Latex will use for the \\blankkropki macro I made
    '''
    print("\\begin{tikzpicture}")
    print("    \\blankkropki{")
    for type in sol: # horizontal and vertical
        for row in type:
            print(" "*8, end="")
            for col in range(len(row)):
                print(str(row[col]), end="")
                if not(col == (len(row) -1)):
                    print(", ", end="")
            print("")
        print("        }")
        if type == sol[0]:
            print("        {")
    print("\\end{tikzpicture}")

for sol in kropki_solutions[:10]:
    latex_print(sol)
