import arcade

class Explosion(arcade.Sprite):
    def __init__(self, texture_list):
        super().__init__()

        self.current_texture = 0
        self.textures = texture_list
    
    def update(self):
        self.current_texture +=1
        if self.current_texture < len(self.textures):
            self.set_texture(self.current_texture)
        else:
            self.remove_from_sprite_lists()