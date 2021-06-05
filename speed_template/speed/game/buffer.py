import sys
from asciimatics.event import KeyboardEvent

class Buffer: 
    
    """ Saves Input Values """
    def input_library(self):
        event = self._screen.get_key()
        input_words_list = []
        
        if event is None:
            """Compare the values of the list to user inputs"""
            final_input = self.guessed_word.join(input_words_list)
            """ Compares saved value to word bank """
            

        elif event is not None:
            """ Appends users input to list """
            self.input_words_list.append(event)
