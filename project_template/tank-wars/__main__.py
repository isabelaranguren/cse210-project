# program entry point

import arcade
import random
import game.constants
from game.output_service import Output_service
from game.draw_actors_action import DrawActorsAction
from game.director import Director
from game.control_actors_action import ControlActorsAction
from game.input_service import Input_Service
from game.actor import Actor
from game.point import Point

def main():
   # create the cast {key: tag, value: list}
    cast = {}
    # must put .scale (if don't want change put = 1)
    tank = Actor("assets/tank-pack/tanks_tankGrey1.png")
    tank.scale = 0.65
    tank = Actor("project_template/tank-wars/assets/tank-pack/tanks_tankGreen1.png")
    tank.scale = 1
    tank.center_x = 150
    tank.velocity = (0,0)
    tank.center_y = game.constants.TANK_Y
    cast["tank"] = tank

    tank2 = Actor("assets/tank-pack/tanks_tankGreen1.png")
    tank2.scale = 0.65
    tank2.center_x = 650
    tank2.center_y = game.constants.TANK_Y
    tank2.velocity = (0,0)
    cast["tank2"] = tank2

    bullet = Actor("assets/tank-pack/tank_bulletFly4.png")
    bullet.scale = 0.75
    bullet.center_y = 155
    bullet.center_x = 300
    bullet.velocity = (5,0)
    cast["bullet"] = bullet

    cast["grounds"] = []
    for x in range(0, 1250, 64):
        ground = Actor(":resources:images/tiles/dirtRight.png")
        ground.scale = 1
        ground.center_x = x
        ground.center_y = 32
        ground.velocity = (0,0)
        cast["grounds"].append(ground)
    # print(cast)
    # create the script {key: tag, value: list}
    script = {}

    input_service = Input_Service()
    output_service = Output_service()
    draw_actors_action = DrawActorsAction(output_service)
    control_actors_action = ControlActorsAction(input_service)
    # output_service.setup()
    # arcade.run()
    # script["input"] = [control_actors_action]
    # script["update"] = [move_actors_action, handle_collisions_acition]
    script["output"] = [draw_actors_action]

    # start the game
    director = Director(cast, script)
    director.start_game()


main()
