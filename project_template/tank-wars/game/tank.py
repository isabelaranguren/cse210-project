from game import constants
import arcade

class Tank(arcade.Sprite):
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
        self.scale = 1
        self.center_x = None
        self.center_y = None
        self.velocity = None
        
    def get_y(self):
        return self.y

    def get_y(self):
        return self.x
    
    def get_velocity(self):
        return self.velocity
