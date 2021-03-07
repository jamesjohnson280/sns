from . import interpreter
from .data import Data as data
from .interpreter import console

interpreter.init(data, console)
interpreter.play()