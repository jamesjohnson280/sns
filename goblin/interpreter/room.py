'''A basic location in the game world'''

class Room:
  '''Represents a single location in the game'''
  def __init__(self, key, settings):
    '''Intializes this Room'''
    self.key = key
    self.name = settings['name']
    self.description = settings['description']