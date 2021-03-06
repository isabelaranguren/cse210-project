from game.action import Action
import time


class DrawActorsAction(Action):
    """A code template for drawing actors. The responsibility of this class of
    objects is use an output service to draw all actors on the screen.

    Stereotype:
        Controller

    Attributes:
        _output_service (OutputService): An instance of OutputService.

    Contributor:
        Template
    """

    def __init__(self, output_service):
        """The class constructor.

        Args:
            output_service (OutputService): An instance of OutputService.

        Contributor:
            Template
        """
        self._output_service = output_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.

        Contributor:
            Template
        """
        for group in cast.values():
            self._output_service.setup(group)