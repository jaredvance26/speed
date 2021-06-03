import random
import time
class Word:
    """ Picks a random word and returns it 
    
    Stereotype: 
        Service Provider

    Attributes:
        words

    """ 
    def __init__(self):
        """ Class constructor. Reads file and splits it into a list """

        with open ('/Users/densmoreb/Desktop/21Spring/CSE 210/week07/speed/speed_template/speed/game/words.txt') as file:
            words = file.read()

        self._words = words.splitlines()

    def random_word(self):
        """ Picks a random word and returns it """
        length = len(self._words) - 1
        
        # This way spits out the entire file in a random order
        # for i in range(len(self.words)):
        #     random_num = random.randint(0, length)
        #     return (self.words[random_num])

        #This way spits out words randomly whenever it is called
        word_num = random.randint(0, length)
        return(self._words[word_num])

""" Testing Area """
word = Word()

for i in range(7000):
    random_word = word.random_word()
    time.sleep(2)
    print (random_word)


