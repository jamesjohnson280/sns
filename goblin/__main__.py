from . import interpreter
from .data import rooms

interpreter.init({'rooms': rooms.Rooms})
interpreter.play()