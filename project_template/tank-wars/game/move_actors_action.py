from game.action import Action
from game.point import Point
import game.constants as constants


class MoveActorsAction(Action):
    def execute(self, cast):
        for group in cast.values():
            # for actor in group:
            self._move_actor(group)

    def _move_actor(self, actor):
        """Moves the given actor to its next position according to its
        velocity. Will wrap the position from one side of the screen to the
        other when it reaches the edge in either direction.

        Args:
            actor (Actor): The actor to move.

        Contributors:
            Template
        """
        # position = actor.get_position()
        # velocity = actor.get_velocity()
        print(actor)
        x1 = actor.get_x()
        y1 = actor.get_y()
        x2 = actor.get_velocity_x() # nonetype
        y2 = actor.get_velocity_y() # nonetype
        x = 1 + (x1 + x2 - 1) % (constants.MAX_X - 1)
        y = 1 + (y1 + y2 - 1) % (constants.MAX_Y - 1)
        position = Point(x, y)
        actor.set_position(x, y)
