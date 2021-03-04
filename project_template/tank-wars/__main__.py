# program entry point

import arcade
import random
import game.constants
from game.output_service import Output_service
from game.director import Director
from game.actor import Actor
from game.point import Point

def main():
   # create the cast {key: tag, value: list}
    cast = {}
    
    cast["ground"] = []
    for x in range(0, game.constants.X_CONSTANT):
        for y in range(0, 150):
            y = random.randint(0, 150)
            position = Point(x,y)
            ground = Actor()
            ground.set_position(position)
    # create the script {key: tag, value: list}
    script = {}


    output_service = Output_service()
    output_service.setup()
    arcade.run()
    # script["input"] = [control_actors_action]
    # script["update"] = [move_actors_action, handle_collisions_acition]
    # script["output"] = [draw_actors_action]

    # start the game
    director = Director(cast, script)
    director.start_game()


main()