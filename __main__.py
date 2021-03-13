import arcade
import game.constants
from game.gameview import Gameview

def main():

    window = arcade.Window(game.constants.X_CONSTANT,
    game.constants.Y_CONSTANT,
    game.constants.SCREEN_TITLE)
    arcade.set_background_color(arcade.color.SMOKY_BLACK)

    view = Gameview()
    window.show_view(view)
    arcade.run()

main()