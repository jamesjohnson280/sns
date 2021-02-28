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

if __name__ == '__main__':
  unittest.main()