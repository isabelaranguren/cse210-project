
"""Sets velocitity and position. passes along info to move actors action. 
Isabel Aranguren bravely offers to conquer this trial"""

from game import constants
from game.action import Action

class ControlActorsAction(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
        
    Contribuitors:
        Isabel Aranguren
        
    """

    def __init__(self, input_service):
        """The class constructor.
        
        Args:
            input_service (InputService): An instance of InputService.
        """
        self._input_service = input_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        direction = self._input_service.get_direction()
        
        # TODO: 
        # Don't know if this is the correct way of doing it  
        bullet = cast["bullet"]
        self._input_service.set_bullet(bullet)
        # This is moving the first brick in the list. Bricks should probable be immobile
        # brick = cast["brick"][0]
        # brick.set_velocity(direction)
        # This is moving the ball where the user sends it. The ball should probably move with it's own velocity
        # ball.set_velocity(direction)