'''Parses player commands in English and converts them to game commands'''

from logging import error


class ParserError(Exception):
  def __init__(self, message):
    self.message = message

def parse(text):
  '''Attempts to understand a string and returns a game command'''
  s = text.lower()
  if s == 'quit':
    return {'verb': 'quit'}
  else:
    raise ParserError("I don't understand the word '{}.'".format(s))
