import arcade
from game import constants

class GameView(arcade.View):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        
        # Call the parent class initializer
        super().__init__()
        
        #TODO: Variables that will hold sprite lists

        # Hide mouse
        self.window.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.SMOKY_BLACK)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
    

        # Score
        self.score = 0

        # TODO: Set up the player
        # Character image from kenney.nl

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()

        # Put the text on the screen.
        # output = f"Score: {self.score}"
        # arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)


    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
       
       
