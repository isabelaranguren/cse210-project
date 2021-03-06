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
    
    tank = Actor()
    tank.set_tag = "Tank"
    tank.set_asset = "assets/tank-pack/tanks_tankGrey1.png"
    tank.set_y = 250
    tank.set_x = 250
    cast["tank"] = [tank]

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