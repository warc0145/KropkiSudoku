
'''
Name: Dylan Warcholik

File Name: LatexPrint6x6.py

Date Started: 8/4/2025

Description:
Prints out kropki arrangements for 6x6 boards in the form that my latex macro will read and print
'''

def latex_print(kropki_arrangement):
    """
    Takes in a Kropki arrangement and outputs in a form that Latex will use for the \\blankkropki macro I made
    """
    print("\\begin{tikzpicture}")
    print("    \\blankkropki{")
    for type in kropki_arrangement: # horizontal and vertical dots
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

def full_color_print(board, coloring, kropki_arrangement):
    """
    Takes in a list of lists and prints out, in a form appropriate for latex, a call to a coloring macro
    """
    print("\\begin{tikzpicture}")
    print("    \\sudokuColorWithNumsAndDots{")

    # First item passed must be the full board:
    for i in range(len(board)):
        print("        ", end="")
        for j in range(len(board[i])):
            print(board[i][j], end = "")
            if not ((i == len(board) - 1) and (j == len(board[i]) - 1)):
                print(", ", end = "")
        if i == len(board) - 1:
            print("}")
        else:
            print()
    
    # Now print the colors
    for color in coloring:
        print("        {", end = "")
        for tup in color:
            print(str(tup[0]) + "/" + str(tup[1]), end = "")
            if not tup == color[-1]:
                print(",", end = "")
        print("}")
    
    # Finally, add the kropki dots:
    for type in kropki_arrangement: # horizontal and vertical dots
        print("        {", end = "")
        for row in range(len(type)):
            for col in range(len(type[row])):
                print(str(type[row][col]), end="")
                if not(col == (len(type[row]) -1) and row == (len(type) - 1)):
                    print(", ", end="")
            # print("")
        print("}")
    
    
    print("\\end{tikzpicture}")