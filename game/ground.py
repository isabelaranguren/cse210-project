import arcade
import game.constants as constants

from random import randint
TILE_SCALING = 0.2
GRAVITY = 1


class GroundSprite(arcade.Sprite):
    def __init__(self):
        super().__init__()
        
         # Our physics engine
        self.physics_engine = None

        self.center_y = constants.GROUND_Y
        self.texture = arcade.load_texture(file_name = constants.GROUND_SPRITE)
        self.scale = constants.GROUND_SCALE
        
        

class Ground:
    def __init__(self):
        
        # Name of map file to load
        map_name = "game/assets/kenney_topdowntanksredux/map.tmx"
        # Name of the layer in the file that has our platforms/walls
        platforms_layer_name = 'Platforms'
        
        # Read in the tiled map
        my_map = arcade.tilemap.read_tmx(map_name)
        
        # self.ground_sprite_list = arcade.SpriteList(use_spatial_hash= True)
        
          # -- Platforms
        self.ground_sprite_list = arcade.tilemap.process_layer(map_object=my_map,
                                                      layer_name=platforms_layer_name,
                                                      scaling=TILE_SCALING,
                                                      use_spatial_hash=True)
        
        # --- Other stuff
        # Set the background color
        if my_map.background_color:
            arcade.set_background_color(my_map.background_color)

        # Create the 'physics engine'
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.ground_sprite_list,
                                                             GRAVITY)
        
        # for y in (0, 600, 200):
        #     self.ground = GroundSprite()
        #     self.ground.center_x = 400
        #     self.ground.center_y = y
        #     self.ground_sprite_list.append(self.ground)
