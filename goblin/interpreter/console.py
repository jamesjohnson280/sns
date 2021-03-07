'''Handles console I/O'''
import textwrap

def write(s):
  '''Prints a string to stdout'''
  paragraphs = s.split('\n')
  for p in paragraphs:
    print(textwrap.fill(p))

def read(prompt = ''):
  '''Reads in a string from stdin and returns it'''
  return input(prompt)