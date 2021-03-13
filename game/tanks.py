import arcade
import game.constants as constants

class Tanks(arcade.Sprite):
    """Changes apply to both tanks

    """
    def __init__(self):
        super().__init__()

        #common tank values
        self._life = 100
        self.center_y = constants.TANK_Y
        self.scale = constants.TANK_SCALE
        #player textures load
        self.player1_texture = arcade.load_texture(file_name = constants.PLAYER1_SPRITE)
        self.player2_texture = arcade.load_texture(file_name = constants.PLAYER2_SPRITE)

    def is_alive(self):
        if self._life <= 0:
            return False
        else:
            return True

class Player1(Tanks):
    """Changes apply to Player1
    """
    def __init__(self):
        super().__init__()
        self.center_x = constants.PLAYER1_X
        self.texture = self.player1_texture

class Player2(Tanks):
    """Changes apply to Player2
    """
    def __init__(self):
        super().__init__()
        self.center_x = constants.PLAYER2_X
        self.texture = self.player2_texture


class Run:
    """Public class will be the one called
    to make changes throughout program
    """
    def __init__(self):
        self.sprite_list = arcade.SpriteList()
        self.player1 = Player1()
        self.player2 = Player2()

        self.sprite_list.append(self.player1)
        self.sprite_list.append(self.player2)