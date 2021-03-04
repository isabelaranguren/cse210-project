import arcade
from game import constants

class Output_service(arcade.Window):
    def __init__(self):
        super().__init__(constants.X_CONSTANT, constants.Y_CONSTANT, constants.SCREEN_TITLE)

        self.player_list = None
        self.wall_list = None


        self.player_sprite = None

        arcade.set_background_color(arcade.color.SMOKY_BLACK)

    def setup(self):
        """
        Set up the game/ restart
        """
        #Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash= True)

        #player sprite
        self.player_sprite = arcade.Sprite("assets/Tank2.png")
        self.player_sprite.center_x = 250
        self.player_sprite.center_y = 250
        self.player_list.append(self.player_sprite)

        #ground sprite
        for x in range(0, 1250, 64):
            wall = arcade.Sprite(":resources:images/tiles/dirtRight.png")
            wall.center_x = x
            wall.center_y = 32
            self.wall_list.append(wall)

    def on_draw(self):
        """ Render the Screen """
        arcade.start_render()

        #draw to screen
        self.wall_list.draw()
        self.player_list.draw()
