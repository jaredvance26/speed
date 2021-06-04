import random
import time
from game.actor import Actor
from game import constants

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

    def random_word(self):
        """ Picks a random word and returns it """
        length = len(self._words) - 1
        word_num = random.randint(0, length)
        return(self._words[word_num])

""" Testing Area """
# word = Word()


# for i in range(7000):
#     random_word = word.random_word()
#     time.sleep(2)
#     print (random_word)


