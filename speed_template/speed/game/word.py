import random
import time
from game.actor import Actor
from game import constants
from game.point import Point

class Word(Actor):
    """ Picks a random word and returns it 
    
    Stereotype: 
        Service Provider

    Attributes:
        words = takes in the words from the file into a list format
    """ 
    def __init__(self):
        """ Class constructor. Reads file and splits it into a list """
        super().__init__()
        self._words = constants.LIBRARY
        self.set_text(self.random_word())
        self.move()

    def random_word(self):
        """ Picks a random word and returns it 
        
        Return: word (string)
        """
        length = len(self._words) - 1
        word_num = random.randint(0, length)
        return(self._words[word_num])

    def _add_segment(self, text, position, velocity):
        """Adds a new segment to the snake using the given text, position and velocity.

        Args:
            self (Snake): An instance of snake.
            text (string): The segment's text.
            position (Point): The segment's position.
            velocity (Point): The segment's velocity.
        """
        segment = Actor()
        segment.set_text(text)
        segment.set_position(position)
        segment.set_velocity(velocity)

    def move(self):
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y / 2)
        for n in range(constants.STARTING_WORDS):
            text =  self.random_word()
            position = Point(x - n, y)
            velocity = Point(1, 0)
            self._add_segment(text, position, velocity)

    

""" Testing Area """
# word = Word()


# for i in range(7000):
#     random_word = word.random_word()
#     time.sleep(2)
#     print (random_word)


