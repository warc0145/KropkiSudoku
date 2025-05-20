'''
Name: Dylan Warcholik

File Name: NonUniqueExploration.py

Date Started: 5/20/25

Description:
This program will explore the 8 Kropki arrangements that resort in non-unique solutions.
'''
from NonUniqueKropkiGenerator import find_horizontal_kropki_dots, find_vertical_kropki_dots
from SudokuPuzzleGenerator4x4 import solutions

for i in range(10):
  print(i)
  print(find_horizontal_kropki_dots(solutions[i]))
  print(find_vertical_kropki_dots(solutions[i]))
