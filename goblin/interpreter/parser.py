'''Parses player commands in English and converts them to game commands'''

def parse(text):
  '''Attempts to understand a string and returns a game command'''
  if text == 'quit':
    return {'verb': 'quit'}