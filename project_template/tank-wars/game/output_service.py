import arcade
from game import constants

class Output_service(arcade.Window):
    def __init__(self):
        super().__init__(constants.X_CONSTANT, constants.Y_CONSTANT, constants.SCREEN_TITLE)

        arcade.set_background_color(arcade.color.SMOKY_BLACK)
        print("Hello Main")
    
    def setup(self):
        """
        Set up the game/ restart
        """
        pass

    def on_draw(self):
        """ Render the Screen """
        arcade.start_render()

