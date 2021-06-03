class Score:
    """ Keeps track of the score of the player 
    
        Stereotype:
            Service Provider

        Attributes:
            _current_score = Score of the player
    """

    def __init__(self):
        """ Class constrtructor. Sets the current score into a private variable """
        self._current_score = 0

    def add_points(self, points):
        """ Adds points to current score """
        self._current_score += points

        return self._current_score