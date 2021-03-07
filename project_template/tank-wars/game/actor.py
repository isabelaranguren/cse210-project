from game import constants
from game.point import Point
import arcade

class Actor(arcade.Sprite):
    """A visible, moveable thing that participates in the game. The responsibility of Actor is to keep track of its appearance, position 
    and velocity in 2d space.

    Stereotype:
        Information Holder

    Attributes:
        _tag (string): The actor's tag.
        _text (string): The textual representation of the actor.
        _position (Point): The actor's position in 2d space.
        _velocity (Point): The actor's speed and direction.
    """

    def __init__(self, filename):
        """The class constructor."""
        super().__init__(filename)
        self.scale = ""
        self.center_x = None
        self.center_y = None
        self.velocity_x = None
        self.velocity_y = None
        self.velocity = None

    def get_y(self):
        return self.center_y

    def get_x(self):
        return self.center_x
    
    def get_velocity(self):
        return self.velocity

    def get_position(self):
        return self.position

    def get_velocity_x(self):
        return self.velocity_x

    def get_velocity_y(self):
        return self.velocity_y
