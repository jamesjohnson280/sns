from . import interpreter
from .data import rooms
from .interpreter import console

interpreter.init({'rooms': rooms.Rooms}, console)
interpreter.play()