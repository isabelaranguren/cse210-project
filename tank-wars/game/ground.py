import arcade
import game.constants as constants

from random import randint

class GroundSprite(arcade.Sprite):
    def __init__(self):
        super().__init__()
        
        # Our physics engine
        self.physics_engine = None
    
class Ground:
    def __init__(self):
        # Name of map file to load
        self.map_name = constants.WALLS
        self.platforms_layer_name = 'Walls'
        
        # Read in the tiled map
        self.my_map = arcade.tilemap.read_tmx(self.map_name)    
        self.ground_sprite_list = arcade.tilemap.process_layer(map_object=self.my_map,
                                                      layer_name=self.platforms_layer_name,
                                                      scaling=constants.TILE_SCALING,
                                                      use_spatial_hash=True)
        # Set the background color
        if self.my_map.background_color:
            arcade.set_background_color(self.my_map.background_color)

        # Create the 'physics engine'
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.ground_sprite_list,
                                                             constants.GRAVITY)