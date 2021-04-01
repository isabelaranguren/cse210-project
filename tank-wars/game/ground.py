import arcade
import game.constants as constants

from random import randint

class GroundSprite(arcade.Sprite):
    """ Class inherits from arcade.Sprite for Ground sprites 
    Stereotype:
        Information Holder
    Attributes:
        physics_engine(None): intialize the phusics engine variable
    Contributors:
        Isabel Aranguren
        Reed Hunsaker
    """
    def __init__(self):
        """Initalize the GroundSprite class
        Args:
            self (GroundSprite): An instance of GroundSprite
        Contributors:
            Reed Hunsaker
            Isabel Aranguren
        """
        super().__init__()
        
        # Our physics engine
        self.physics_engine = None
    
class Ground:
    """ Class creates map 
    Stereotype:
        Information Holder
    Attributes:
        map_name(file_path): map file
        platforms_layer_name (string): layer name for the platforms
        my_map (arcade.titlemap.read_tmx): intializes the map using the arcade library
        ground_sprite_list (arcade.tilemap.process_layer): ground sprite list
        physics_engine (arcade.PhysicsEnginePlatformer): intialize the physics engine with the wall
    Contributors:
        Isabel Aranguren
        Reed Hunsaker
    """
    def __init__(self):
        """Initalize the Gorund class
        Args:
            self (Ground): An instance of Ground
        Contributors:
            Reed Hunsaker
            Isabel Aranguren
        """
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