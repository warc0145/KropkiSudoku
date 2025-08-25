'''
Name: Dylan Warcholik

Date: 8/19/25

Description:
Generates a dictionary for the kropki numbers (how many dots in a puzzle) for all 6x6 solutions.
'''
# from ReverseKropki6x6 import find_horizontal_kropki_dots, find_vertical_kropki_dots

def kropki_num_generator(board):
    """
    Returns the kropki number for a given board
    """

    vert_num = 0
    horiz_num = 0
    horiz_kropki = find_horizontal_kropki_dots(board)
    vert_kropki = find_vertical_kropki_dots(board)
        
    # Count the number of horizontal kropki dots:
    for row in horiz_kropki:
        for col in row:
            if col != 0:
                horiz_num += 1
    # Count the number of vertical kropki dots:
    for row in vert_kropki:
        for col in row:
            if col != 0:
                vert_num += 1
        
    return vert_num + horiz_num

# print("Opening...")
# with open("6x6Sudoku/AllSolutions6x6.txt", 'r') as f:
#     kropki_num_dict = dict() # Keys will be the number of solutions, values will be the number of puzzles that had that many solutions
#     line_num = 0
    
#     for line in f:
#         line_num += 1
#         if line_num % 100000 == 0:
#             print(line_num)
        
#         starting_solution = [[line[2], line[5], line[8], line[11], line[14], line[17]],
#                             [line[22], line[25], line[28], line[31], line[34], line[37]],
#                             [line[42], line[45], line[48], line[51], line[54], line[57]],
#                             [line[62], line[65], line[68], line[71], line[74], line[77]],
#                             [line[82], line[85], line[88], line[91], line[94], line[97]],
#                             [line[102], line[105], line[108], line[111], line[114], line[117]]]
#         # Cast the num strings to integers
#         for i in range(len(starting_solution)):
#             for j in range(len(starting_solution[i])):
#                 starting_solution[i][j] = int(starting_solution[i][j])
        
#         kropki_num = kropki_num_generator(starting_solution)
#         if kropki_num in kropki_num_dict:
#             kropki_num_dict[kropki_num] += 1
#         else:
#             kropki_num_dict[kropki_num] = 1
# print(kropki_num_dict)

dic = {33: 1042072, 32: 1574244, 36: 234472, 35: 397904, 38: 70020, 37: 129544, 30: 2744968, 
        34: 665520, 29: 3166512, 31: 2166528, 27: 3224704, 28: 3399352, 26: 2830700, 40: 21032, 
        25: 2263920, 39: 35352, 22: 683932, 23: 1102944, 41: 8720, 42: 4824, 43: 1800, 24: 1654004, 
        21: 387960, 20: 204552, 19: 100160, 18: 48196, 44: 1136, 45: 320, 46: 112, 17: 21008, 16: 8296, 
        47: 48, 15: 3184, 14: 2040, 13: 520, 11: 48, 12: 216, 10: 24, 48: 72}
lst = []
# # print(lst.sort())
# print(dic.keys())

# for key, val in dic.items():
#     lst.append((key,val))

# lst.sort(key=lambda tup: tup[0])
# print(lst)