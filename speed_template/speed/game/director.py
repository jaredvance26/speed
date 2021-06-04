from time import sleep
from game import constants
from game.word import Word
from game.score import Score
from game.buffer impor Buffer



class Director:


    def __init__(self, input_service, output_service):
        self._word = Word()
        self._input_service = input_service
        self._keep_playing = True
        self._output_service = output_service
        self.score = Score()
        self.buffer = Buffer()

    def start_game(self):
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            sleep(constants.FRAME_LENGTH)

    def _get_inputs(self):
        pass

    def _do_updates(self):
        pass

    def _do_outputs(self):
        pass

    