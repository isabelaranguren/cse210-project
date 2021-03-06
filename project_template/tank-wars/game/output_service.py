import arcade
from game import constants
import sys

class Output_service(arcade.Window):
    def __init__(self):
        super().__init__(constants.X_CONSTANT, constants.Y_CONSTANT, constants.SCREEN_TITLE)

        self.player_list = None
        self.wall_list = None
        self.player_sprite = None
        
        # Used to keep track of our scrolling
        self.view_bottom = 0
        self.view_left = 0
        arcade.set_background_color(arcade.color.SMOKY_BLACK)
        
    def setup(self):
        """
        Set up the game/ restart
        """
        #Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash= True)
        
        # Used to keep track of our scrolling
        self.view_bottom = 0
        self.view_left = 0
  # --- Load in a map from the tiled editor ---

        # Name of map file to load
        map_name = "project_template/tank-wars/assets/map.tmx"
        # Name of the layer in the file that has our platforms/walls
        platforms_layer_name = 'Platforms'
        
        # Read in the tiled map
        my_map = arcade.tilemap.read_tmx(map_name)

        # -- Platforms
        self.wall_list = arcade.tilemap.process_layer(map_object=my_map,
                                                      layer_name=platforms_layer_name,
                                                      scaling= constants.TILE_SCALING,
                                                      use_spatial_hash=True)
    
        if my_map.background_color:
            arcade.set_background_color(my_map.background_color)

        # Create the 'physics engine'
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                             self.wall_list,
                                                             constants.GRAVITY)

    def on_draw(self):
        """ Render the Screen """
        arcade.start_render()

        #draw to screen
        self.wall_list.draw()
    
