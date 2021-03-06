import io
import sys
import unittest

from goblin import interpreter
from goblin.data.rooms import Rooms

class InterpreterTestCase(unittest.TestCase):
  '''The `Interpreter`'''
  def setUp(self):
    interpreter.init({ 'rooms': Rooms })
    self.stdout = sys.stdout
    sys.stdout = io.StringIO()

  def test_init_interpreter(self):
    '''it should display the player's starting location'''
    interpreter.play()
    description = sys.stdout.getvalue()
    self.assertTrue(description.find('Dusty Dirt Road') != -1)

  def tearDown(self):
    sys.stdout = self.stdout
