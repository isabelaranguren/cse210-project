import arcade
import game.constants as constants

class Explosion(arcade.Sprite):
    def __init__(self, texture_list):
        super().__init__()

        self.current_texture = 0
        self.textures = texture_list
        self.tank_explode = arcade.load_sound(constants.EXPLOSION_SOUND)
    
    def update(self):
        self.current_texture +=1
        if self.current_texture < len(self.textures):
            self.set_texture(self.current_texture)
            arcade.play_sound(self.tank_explode,.5)
        else:
            self.remove_from_sprite_lists()