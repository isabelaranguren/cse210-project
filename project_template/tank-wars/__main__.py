# program entry point

import arcade
import random
import game.constants
from game.output_service import Output_service
from game.draw_actors_action import DrawActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.move_actors_action import MoveActorsAction
from game.director import Director
from game.actor import Actor
from game.point import Point


def main():
    # create the cast {key: tag, value: list}
    cast = {}
    # must put .scale (if don't want change put = 1)

    tank = Actor("tank-wars/assets/tank-pack/tanks_tankGreen1.png")
    tank.scale = 0.85
    tank.center_x = 125
    tank.center_y = game.constants.TANK_Y
    # tank.velocity_x = 0
    # tank.velocity_y = 0
    cast["tank"] = tank
    cast["enemy"] = []
    enemy = Actor("tank-wars/assets/tank-pack/tanks_tankNavy1.png")
    enemy.scale = 0.85
    enemy.center_x = 675
    enemy.center_y = game.constants.TANK_Y
    # enemy.velocity_x = 0
    # enemy.velocity_y = 0
    cast["enemy"].append(enemy)
    cast["bullets"] = []
    bullet = Actor("tank-wars/assets/tank-pack/tank_bullet1.png")
    bullet.scale = 0.65
    bullet.center_x = 50
    bullet.center_y = 140
    bullet.velocity = (15, 10)
    # bullet.velocity_x = 15
    # bullet.velocity_y = 10
    cast["bullets"].append(bullet)
    cast["grounds"] = []
    for x in range(0, 1250, 64):
        ground = Actor(":resources:images/tiles/dirtRight.png")
        ground.scale = 1
        ground.center_x = x
        ground.center_y = 32
        cast["grounds"].append(ground)

    """sprite_list = arcade.SpriteList()
    for group in cast:
        for actor in group:
            sprite_list.append(sprite_list, "some type")
            arcade.SpriteList.append(actor)"""

    # create the script {key: tag, value: list}
    script = {}

    output_service = Output_service()
    draw_actors_action = DrawActorsAction(output_service)
    # move_actors_action = MoveActorsAction(sprite_list)
    # handle_collisions_action = HandleCollisionsAction()
    # output_service.setup()
    # arcade.run()
    # script["input"] = [control_actors_action]
    # script["update"] = [move_actors_action, handle_collisions_action]
    script["output"] = [draw_actors_action]

    # start the game
    director = Director(cast, script)
    director.start_game()


main()
