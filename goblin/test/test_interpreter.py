import unittest
from unittest.result import failfast

class TestInterpreter(unittest.TestCase):
  def test_true(self):
    self.assertEquals(True, False)