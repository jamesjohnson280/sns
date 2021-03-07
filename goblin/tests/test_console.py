import io
import sys
import unittest

from goblin.interpreter import console

class ConsoleTestCase(unittest.TestCase):
  '''The `Interpreter`'''
  def setUp(self):
    self.stdin = sys.stdin
    self.stdout = sys.stdout
    sys.stdout = io.StringIO()
    sys.stdin = io.StringIO()

  def test_write(self):
    '''it should print to stdout'''
    console.write('Hello, world!')
    self.assertEqual(sys.stdout.getvalue(), 'Hello, world!\n')

  def test_write(self):
    '''it should read from stdin'''
    self.mock_stdio('Hello, world!')
    text = console.read()
    self.assertEqual(text, 'Hello, world!')

  def test_prompt(self):
    '''It should display an input prompt when supplied'''
    self.mock_stdio('hi')
    console.read('>')
    self.assertEqual(sys.stdout.getvalue(), '>')

  def tearDown(self):
    sys.stdin = self.stdin
    sys.stdout = self.stdout

  def mock_stdio(self, s):
    '''Writes a string to stdin'''
    sys.stdin = io.StringIO(s)
