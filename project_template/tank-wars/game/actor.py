from game import constants
from game.point import Point
import arcade

class Actor(arcade.SpriteList):
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

    def __init__(self):
        """The class constructor."""
        super().__init__()
        self._tag = ""
        self.sprite_list = None
        self.x = None
        self.y = None
        self._asset = ""

    def get_tag(self):
        
        """Updates the actor's tag to the given value.
        
         _tag: The actor's textual representation.
    
        Contributors:
            Isabel Aranguren
        """
        
        return self._tag
    
    def set_tag(self, tag):
        
        """ Gets the actor's tag and direction.
        
         _tag: The actor's textual representation.
        
         Contributors:
            Isabel Aranguren

        """
        self._tag = tag
    
    def set_asset(self, asset):
        """Sets file path"""
        self._asset = asset
    
    def get_assest(self):
        return self._asset

    def set_y(self, y):
        self.y = y

    def get_y(self):
        return self.y
    
    def set_y(self, x):
        self.x = x

    def get_y(self):
        return self.x

