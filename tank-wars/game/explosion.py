import arcade
import game.constants as constants

class Explosion(arcade.Sprite):
    def __init__(self):
        super().__init__()

        self.current_texture = 0
        self.load_tex = arcade.load_texture(constants.EXPLOSION_4)
        self.texture = self.load_tex
    
    def update(self):
        self.current_texture +=1
        if self.current_texture < len(self.textures):
            self.set_texture(self.current_texture)
        else:
            self.remove_from_sprite_lists()