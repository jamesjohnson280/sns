import unittest

from goblin.interpreter import world
from goblin.interpreter.room import Room
from goblin.data.rooms import Rooms

class WorldTestCase(unittest.TestCase):
  '''The `World`'''
  def setUp(self):
    world.init(Rooms)

  def test_init_rooms(self):
    '''it should contain the 'Dusty Dirt Road' room'''
    road = world.get('road')
    self.assertIsInstance(road, Room)