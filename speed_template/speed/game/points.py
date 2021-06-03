class Point:
    """ Adds points if the keyboard input matches any of the words. """
    def __init__(self):
        self.points = 0

    def add_points(self, num_true):
        """ Takes in a number of how many times a word is entered correctly and adds it."""
        self.points += num_true
        return self.points