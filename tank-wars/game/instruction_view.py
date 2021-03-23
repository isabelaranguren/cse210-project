import arcade
import game.constants as constants
from game.gameview import GameView

class InstructionView(arcade.View):
    """ View to show instructions """
    
    def __init__(self):
        super().__init__()
        self.music = arcade.load_sound(constants.MAIN_SCREEN_SOUND)

    def on_show(self):
        """ This is run once when we switch to this view """
       
        self.texture = arcade.load_texture(constants.CAMO)
        arcade.play_sound(self.music,0.1)

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        self.texture.draw_sized(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2,
                                constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        
        arcade.draw_text("Tank Wars", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Click to advance", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2-75,
                         arcade.color.WHITE, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, start the game. """
        # arcade.stop_sound(self.music)
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)