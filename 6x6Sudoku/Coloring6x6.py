'''
Name: Dylan Warcholik

File Name: Coloriong6x6.py

Date Started: 

Description:
Will assist in identifying the coloring of a 6x6 Sudoku board.
'''


def colorer_6x6(board):
    """
    This function will take in a board (a list of 6 lists, each of length six, representing the rows and columns)
    And it will return a list of six lists, each item in the inner list being a tuple acting as a coordinate.
    
    The outershell will be the color, then there will be a list of coordinates (each a 2-tuple) where that color appears
    """
    # Determine which number will be associated with each "color"
    first, second, third, fourth, fifth, sixth = board[0][0], board[0][1], board[0][2], board[0][3], board[0][4], board[0][5]
        
    # Create empty lists that will store the coordinates of these colors
    first_lst = []
    second_lst = []
    third_lst = []
    fourth_lst = []
    fifth_lst = []
    sixth_lst = []

    # Iterate through the board adding the coordinates of tiles with the same color to the appropriate list
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == first:
                first_lst.append((i,j))
            elif board[i][j] == second:
                second_lst.append((i,j))
            elif board[i][j] == third:
                third_lst.append((i,j))
            elif board[i][j] == fourth:
                fourth_lst.append((i,j))
            elif board[i][j] == fifth:
                fifth_lst.append((i,j))
            else: # board[i][j] == sixth:
                sixth_lst.append((i,j))
        # print("Using the board", board)
        # print("Our lists:")
        # print(first_lst, "\n", second_lst, "\n", third_lst, "\n", fourth_lst)
        # Now we know the coordinates of all numbers, add it to the dictionary or increment the count
    return [first_lst, second_lst, third_lst, fourth_lst, fifth_lst, sixth_lst]

# print(colorer_6x6([[6, 5, 4, 3, 2, 1], [3, 2, 1, 6, 5, 4], [5, 6, 2, 1, 4, 3], [1, 4, 3, 2, 6, 5], [2, 3, 5, 4, 1, 6], [4, 1, 6, 5, 3, 2]]))