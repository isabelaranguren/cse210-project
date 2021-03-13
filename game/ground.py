import arcade
import game.constants as constants

from random import randint


class GroundSprite(arcade.Sprite):
    def __init__(self):
        super().__init__()

        self.center_y = constants.GROUND_Y
        self.texture = arcade.load_texture(file_name = constants.GROUND_SPRITE)
        self.scale = constants.GROUND_SCALE

class Ground:
    def __init__(self):
        
        self.ground_sprite_list = arcade.SpriteList(use_spatial_hash= True)
        for x in range(0,1250,64):
            ry = randint(0,32)
            for y in range(0, ry):
                self.ground = GroundSprite()
                self.ground.center_x = x
                self.ground.center_y = y
                self.ground_sprite_list.append(self.ground)
