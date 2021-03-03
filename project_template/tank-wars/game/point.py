class Point:
    """
    Represents distance from the orgin as (0,0)
    Stereotype:
        Information Holder
    
    Attributes:
        _x (integer): ther horizontal distance
        _y (Point): The vertical distance
    Contributors:
 
    """

    def __init__(self, x, y):
        """The clas constructor
        Agrs:
        self (Point): An instance of Point.
        x (integer): A horizontal distance:
        y (integer): A vertical distnace.
        Contributors:
          
        """
        self._x = x
        self._y = y

    def get_x(self):
        """
        Gets the horizontal distance
        Args:
            self (Point): An instance of Point.
        
        Returns:
            integer: The horizontal distance.
        Contributors:
  
        """
        return self._x
    
    def get_y(self):
        """
        Gets the vertical distance
        Args:
            self (Point): An instance of Point.
        Returns:
            integer: The vertical distance
        """
        return self._y

    def equals(self, other):
        """
        Whether orn ot this Point is equal to the given one.
        Args:
            self (Point): An instance of Point.
            other (Point): The Point to compare.
        
        Returns:
            boolean: True if both x and y are equal; false if not
        

        """
        return self._x == other.get_x() and self._y == other.get_y()