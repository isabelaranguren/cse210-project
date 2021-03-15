
import random


from game.tanks import Tanks

class Score(Tanks):
    """Points earned. The responsibility of Score is to keep track of the player's points.
    Stereotype:
        Information Holder
    Attributes: 
        _score (integer): The position of the score bar
        set_text (Actor): Writes score
    Contributors:
            Isabel Aranguren
         
    """
    def __init__(self):
        """The class constructor. Invokes the superclass constructor, initializes points to zero, sets the position and updates the text.
        
        Args:
            self (Score): an instance of Score.
        
        """
        super().__init__()
        self._score = 0
        # self._set_text(f"Score: {self._score}")
    
    def add_score(self):
        """Adds the given points to the running total and updates the text.
        Args:
            self (Score): An instance of Score.
            points (integer): The points to add.
        """
        self._score += 1
        # self.set_text(f"Score: {self._score}")

    def get_score(self):
        return self._score