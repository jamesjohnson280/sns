import unittest

from goblin.interpreter import parser

class ConsoleTestCase(unittest.TestCase):
  '''The `Parser`'''
  def test_parse(self):
    '''it should convert english into game commands'''
    command = parser.parse('quit')
    self.assertEqual(command, {'verb': 'quit'})

  def test_caseless_parse(self):
    '''it should ignore case on input strings'''
    command = parser.parse('qUiT')
    self.assertEqual(command, {'verb': 'quit'})

  def test_parser_error(self):
    '''It should throw an error if it doesn't understand the input'''
    with self.assertRaises(parser.ParserError):
      parser.parse('fr00b')
