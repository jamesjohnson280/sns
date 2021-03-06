'''The adventure interpreter'''
from . import world
from . import player

_player = None

def init(data):
  global _player
  world.init(data['rooms'])
  _player = player.Player()
  _player.location = world.get('road')

def play():
  d = _player.location.player_description()
  print(d)