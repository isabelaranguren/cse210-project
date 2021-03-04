from game import constants
from game.point import Point

class Actor:
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
        self._tag = ""
        self._description = ""
        self._text = ""
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)
        self._value = 0

    def get_description(self):
        """Gets the artifact's description.
        
        Returns:
            string: The artifact's description.
        """
        return self._description 

    def get_position(self):
        """Gets the actor's position in 2d space.
        
        Returns:
            Point: The actor's position in 2d space.
        """
        return self._position
    
    def get_text(self):
        """Gets the actor's textual representation.
        
        Returns:
            string: The actor's textual representation.
        """
        return self._text

    def get_velocity(self):
        """Gets the actor's speed and direction.
        
        Returns:
            Point: The actor's speed and direction.
        """
        return self._velocity
    
    def set_description(self, description):
        """Updates the actor's description to the given one.
        
        Args:
            description (string): The given description.
        """
        self._description = description

    def set_position(self, position):
        """Updates the actor's position to the given one.
        
        Args:
            position (Point): The given position.
        """
        self._position = position
    
    def set_text(self, text):
        """Updates the actor's text to the given value.
        
        Args:
            text (string): The given value.
        """
        self._text = text

    def set_velocity(self, velocity):
        """Updates the actor's velocity to the given one.
        
        Args:
            position (Point): The given velocity.
        """
        self._velocity = velocity
        
        
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

    def set_value(self, value):
        """ sets the actor's value.
        
         value: The actor's score value
        
         Contributors:
            Isabel Aranguren
            Reed Hunsaker
            Juliano Nascimento
            Adrianna Lund
            Jordan McIntyre
        """
        self._value = value
    
    def get_value(self):
        """ Gets the actor's value.
        
         Contributors:
            Isabel Aranguren
            Adrianna Lund
            Reed Hunsaker
            Juliano Nascimento
            Jordan McIntyre
        """
        return self._value
