'''The adventure interpreter'''
from . import world
from . import player
from . import console
from . import parser

_player = None
_con = None

def init(data, console):
  global _player
  global _con
  world.init(data['rooms'])
  _player = player.Player()
  _player.location = world.get('road')
  _con = console

def play():
  d = _player.location.player_description()
  _con.write(d)
  while True:
    text = console.read('>')
    try: 
      parser.parse(text)
    except parser.ParserError as error:
      console.write(error.message)
