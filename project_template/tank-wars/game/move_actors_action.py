from game.action import Action
from game.point import Point
import game.constants as constants
from game.output_service import Output_service
import arcade


class MoveActorsAction(Action):

    pass
    """def __init__(self, sprite_list):
        self.sprite_list = sprite_list


    def execute(self):
        arcade.SpriteList.update(self.sprite_list)
    # bullet.update()"""

"""
    def update(self, actor):
        actor.update()
        # for actor in cast:
            # actor.update()

    def execute(self, cast):
       
        cast.update()"""

    # def _move_actor(self, actor):
"""Moves the given actor to its next position according to its
        velocity. Will wrap the position from one side of the screen to the
        other when it reaches the edge in either direction.

        Args:
            actor (Actor): The actor to move.

        Contributors:
            Template
        """
"""        # position = actor.get_position()
        # velocity = actor.get_velocity()
        print(actor)
        x1 = actor.get_x()
        y1 = actor.get_y()
        x2 = actor.get_velocity_x() # nonetype
        y2 = actor.get_velocity_y() # nonetype
        x = 1 + (x1 + x1 - 1) % (constants.MAX_X - 1)
        y = 1 + (y1 + y1 - 1) % (constants.MAX_Y - 1)
        position = Point(x, y)
        actor.set_position(x, y)
"""