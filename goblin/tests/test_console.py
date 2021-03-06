import io
import sys
import unittest

from goblin.interpreter import console

class ConsoleTestCase(unittest.TestCase):
  '''The `Interpreter`'''
  def setUp(self):
    self.stdout = sys.stdout
    sys.stdout = io.StringIO()

  def test_write(self):
    '''it should print to stdout'''
    console.write('Hello, world!')
    self.assertEqual(sys.stdout.getvalue(), 'Hello, world!\n')

  def tearDown(self):
    sys.stdout = self.stdout
