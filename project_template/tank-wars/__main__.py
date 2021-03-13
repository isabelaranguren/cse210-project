from game import constants
import arcade
from game.game_view import GameView
from game.instruction_view import InstructionView

def main(): 
    window = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.TITLE)
    start_view = InstructionView()
    window.show_view(start_view)
    arcade.run()

if __name__ == "__main__":
    main()
