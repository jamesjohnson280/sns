import unittest

from goblin.interpreter.room import Room

class RoomTestCase(unittest.TestCase):
  '''The `Room`'''
  def setUp(self):
    self.room = Room('room', {
      'name': 'Room',
      'description': 'This is a room'
    })

  def test_key(self):
    '''it should have a key'''
    self.assertEqual(self.room.key, 'room')

  def test_name(self):
    '''it should have a name'''
    self.assertEqual(self.room.name, 'Room')

  def test_description(self):
    '''it should have a description'''
    self.assertEqual(self.room.description, 'This is a room')

  def test_invalid_init(self):
    '''it should throw an error on incomplete settings'''
    with self.assertRaises(KeyError):
      invalidRoom = Room('invalid', {})

  def test_player_description(self):
    '''`Room.player_description()` should return the full description'''
    description = self.room.player_description()
    self.assertEqual(description, 'Room\nThis is a room\n')

  def test_short_description(self):
    '''calling `Room.player_description()` a second time should return the short description'''
    self.room.player_description()
    description = self.room.player_description()
    self.assertEqual(description, 'Room\n')

  def test_room_connection(self):
    '''`Room.connect_to()` should create an exit'''
    forest = Room('forest', {
      'name': 'Forest',
      'description': 'This is a forest'
    })
    self.room.connect('east', forest)
    self.assertEqual(self.room.exits['east'], forest)

if __name__ == '__main__':
  unittest.main()