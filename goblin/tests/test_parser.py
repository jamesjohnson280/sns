import unittest

from goblin.interpreter import parser

class ConsoleTestCase(unittest.TestCase):
  '''The `Parser`'''
  def test_parse(self):
    '''it should convert english into game commands'''
    command = parser.parse('quit')
    self.assertEqual(command, {'verb': 'quit'})
