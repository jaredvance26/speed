import sys
from game.point import Point
from asciimatics.event import KeyboardEvent

class InputService:
    """Detects player input. The responsibility of the class of objects is to detect player keypresses and translate them into a point representing a direction (or velocity).

    Stereotype: 
        Service Provider

    Attributes:
        _screen (Screen): An Asciimatics screen.
        _keys (Dict): A dictionary containing Points for U, D, L and R.
        _current (Point): The last direction that was pressed.
    """

    def __init__(self, screen):
        """The class constructor.
        
        Args:
            self (InputService): An instance of InputService.
        """
        self._screen = screen
        self._keys = {}
        self._keys[119] = Point(0, -1) # UP
        self._keys[115] = Point(0, 1) # DOWN
        self._keys[97] = Point(-1, 0) # LEFT
        self._keys[100] = Point(1, 0) # RIGHT
        self._current = Point(0, 1)
        
    def get_direction(self):
        """Gets the selected direction. If one hasn't been selected the last 
        one is returned.

        Args:
            self (InputService): An instance of InputService.

        Returns:
            Point: The selected direction.
        """
        return self._current