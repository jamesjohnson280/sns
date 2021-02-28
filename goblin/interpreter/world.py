from .room import Room

_game_objects = {}

def init(rooms):
  '''Initializes the world'''
  global _game_objects

  for _, settings in rooms.items():
    room = Room(settings['key'], settings)
    _game_objects[settings['key']] = room

def get(key):
  '''Returns a game object indexed by `key`'''
  return _game_objects[key]