# program entry point

import arcade
from game.output_service import Output_service
from game.director import Director

def main():
   # create the cast {key: tag, value: list}
    cast = {}
    
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