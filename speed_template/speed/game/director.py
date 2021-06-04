from time import sleep
from game import constants
from game.word import Word
from game.score import Score
from game.buffer import Buffer


class Director:


    def __init__(self, input_service, output_service):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._word = Word()
        self._input_service = input_service
        self._keep_playing = True
        self._output_service = output_service
        self.score = Score()
        self.buffer = Buffer()

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            sleep(constants.FRAME_LENGTH)

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the desired direction and moving the snake.

        Args:
            self (Director): An instance of Director.
        """
        self.word = self._word.random_word()

    def _do_updates(self):
        pass

    def _do_outputs(self):
        self._output_service.draw_actor(self.word)

    