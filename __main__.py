import arcade
import game.constants
from game.gameview import GameView
from game.instruction_view import InstructionView

def main():
    window = arcade.Window(game.constants.X_CONSTANT, game.constants.Y_CONSTANT, game.constants.TITLE)
    start_view = InstructionView()
    window.show_view(start_view)
    arcade.run()

if __name__ == "__main__":
    main()