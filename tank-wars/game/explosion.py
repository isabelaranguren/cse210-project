import arcade
import game.constants as constants

class Explosion(arcade.Sprite):
    """ Controls the progression of the explosion
    Stereotype:
        Information Holder
    Attributes:
        current_texture (None): declares current texture variable
        textures (None): declares texture list variable
    Contributors:
        Adrianna Lund
    """
    def __init__(self, texture_list):
        """ Declares variables for the Explosion class
        Args:
            self (Explosion): an instance of GameView
            texture_list: list of explosion images

        Contributors:
            Adrianna Lund
        """
        super().__init__()
        self.current_texture = 0
        self.textures = texture_list
        
    
    def update(self):
        """ Progresses through the list of images for the explosion, then removes them from the sprite lists
        Args:
            self (Explosion): an instance of GameView
            
        Contributors:
            Adrianna Lund
        """
        self.current_texture +=1
        if self.current_texture < len(self.textures):
            self.set_texture(self.current_texture)
            
        else:
            self.remove_from_sprite_lists()

        return self.current_texture 