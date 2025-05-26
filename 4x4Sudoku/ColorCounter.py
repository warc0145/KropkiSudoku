'''
Name: Dylan Warcholik

File Name: ColorCounter.py

Date Started: 5/26/25

Description:
This program will produce information summarizing the appearance of white and black dots in all of the 4x4 arrangements
'''
from NonUniqueKropkiGenerator.py import non_unique_kropki_solutions
from KropkiGenerator4x4.py import kropki_solutions

def non_unique_counter(solutions):
  '''
  Will go through the non-unique set of Kropki Arrangements (where white dots are present between 1 and 2), and produce dictionaries
  that describe the number of white and black dots found across all puzzles
  '''
  non_unique_white = dict()
  non_unique_black = dict()

def unique_counter(solutions):
  '''
  Will go through the unique set of Kropki Arrangements (where black dots are present between 1 and 2), and produce dictionaries
  that describe the number of white and black dots found across all puzzles
  '''
  unique_white = dict()
  unique_black = dict()
