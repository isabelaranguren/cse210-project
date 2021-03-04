from time import sleep
from game import constants

class Director:

    def __init__(self, cast, script):
        self._cast = cast
        self._script = script

    def __init__(self, cast, script):
        """The class constructor.
        
        Args:
            cast (dict): The game actors {key: tag, value: list}.
            script (dict): The game actions {key: tag, value: list}.

        Contributors:
            Template
            Juliano
            Jordan McIntyre
        """
        self._cast = cast
        self._script = script
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.

        Contributors:
            Template
            Juliano
            Jordan McIntyre
        """
        while True:
            self._cue_action("input")
            self._cue_action("update")
            self._cue_action("output")
            sleep(constants.FRAME_LENGTH)

    def _cue_action(self, tag):
        """Executes the actions with the given tag.
        
        Args:
            tag (string): The given tag.

        Contributors:
            Template
            Juliano
            Jordan McIntyre
        """ 
        for action in self._script[tag]:
            action.execute(self._cast)