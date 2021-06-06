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
        
    def random_word(self):
        """ Picks a random word and returns it 
        
        Return: word (string)
        """
        length = len(self._words) - 1
        word_num = random.randint(0, length)
        self.words_generated = []
        self.words_generated.append(self._words[word_num])

        return(self._words[word_num])

    def _add_segment(self, text, position, velocity):
        segment = Actor()
        segment.set_text(text)
        segment.set_position(position)
        segment.set_velocity(velocity)

    def move(self):
        x = int(random.randint(0, constants.MAX_X))
        y = int(random.randint(0, constants.MAX_Y))
        for n in range(constants.STARTING_WORDS):
            text = self.random_word()
            position = Point(x, y)
            velocity = Point(0, 0)
            self._add_segment(text, position, velocity)

    

""" Testing Area """
# word = Word()


# for i in range(7000):
#     random_word = word.random_word()
#     time.sleep(2)
#     print (random_word)


