import unittest

from goblin.interpreter.player import Player
from goblin.interpreter.room import Room
from goblin.data.rooms import Rooms

class PlayerTestCase(unittest.TestCase):
  '''The `Player`'''
  def setUp(self):
    self.player = Player()
    self.road = Room('road', Rooms['road'])
    self.player.location = self.road

  def test_init_player(self):
    '''it should have a starting location'''
    self.assertEqual(self.player.location, self.road)
