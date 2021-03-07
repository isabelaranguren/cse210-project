# program entry point

import arcade
import random
import game.constants
from game.output_service import Output_service
from game.draw_actors_action import DrawActorsAction
from game.director import Director
from game.actor import Actor
from game.point import Point

def main():
   # create the cast {key: tag, value: list}
    cast = {}
    # must put .scale (if don't want change put = 1)
    tank = Actor("project_template/tank-wars/assets/tank-pack/tanks_tankGreen1.png")
    tank.scale = 1
    tank.center_x = 150
    tank.center_y = game.constants.TANK_Y
    cast["tank"] = tank

    cast["grounds"] = []
    for x in range(0, 1250, 64):
        ground = Actor(":resources:images/tiles/dirtRight.png")
        ground.scale = 1
        ground.center_x = x
        ground.center_y = 32
        cast["grounds"].append(ground)

    # create the script {key: tag, value: list}
    script = {}


    output_service = Output_service()
    draw_actors_action = DrawActorsAction(output_service)
    # output_service.setup()
    # arcade.run()
    # script["input"] = [control_actors_action]
    # script["update"] = [move_actors_action, handle_collisions_acition]
    script["output"] = [draw_actors_action]

    # start the game
    director = Director(cast, script)
    director.start_game()


main()
