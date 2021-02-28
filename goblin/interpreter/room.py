'''A basic location in the game world'''

class Room:
  '''Represents a single location in the game'''
  def __init__(self, key, settings):
    '''Intializes this Room'''
    self.key = key
    self.name = settings['name']
    self.description = settings['description']
    self.player_visited = False
    self.exits = {}

  def player_description(self):
    '''Returns a str containing the description of this Room and its contents
    from the player's point of view. It returns a verbose description on the 
    first call but omits `self.description` thereafter. Setting `full` to `True` 
    overrides this behaviour'''
    message = '{}\n'.format(self.name)
    if not self.player_visited:
      self.player_visited = True
      message += '{}\n'.format(self.description)
    return message

  def connect(self, exit, room):
    '''Connects this Room to another via an exit'''
    self.exits[exit] = room