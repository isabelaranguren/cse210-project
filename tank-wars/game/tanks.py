import arcade
import game.constants as constants
import math
from random import randint


class Tanks(arcade.Sprite):
    """Class that represent the tank sprites on screen.
    
    Stereotype:
        Information Holder
    
    Attributes:
        _life (integer): Life value of the tanks
        cur_health(integer): Current Life value of the tanks
        speed (integer): speed of tanks
        center_y (integer): y value pixel of tank spirte
        scale (integer): scale of sprite
        player1_texture (arcade.load_texture): file path for player1 sprite using arcade.load_texture
        player2_texture (arcade.load_texture): file path for player2 sprite using arcade.load_texture
    
    Contributors:
        Reed Hunsaker
        Isabel Aranguren
    """
    def __init__(self):
        super().__init__()
        

        #common tank values
        self._life = 300
        self.cur_health = 300
        self.speed = 0
        # self.center_y = constants.TANK_Y
        self.scale = constants.TANK_SCALE
     
        #player textures load
        self.player1_texture = arcade.load_texture(file_name = constants.PLAYER1_SPRITE)
        self.player2_texture = arcade.load_texture(file_name = constants.PLAYER2_SPRITE)
        


    def is_alive(self):
        """checks to see if take is alive
        Contributors:
            Reed Hunsaker
        """
        if self._life <= 0:
            return False
        else:
            return True
    
    
    def set_life(self, points_change):
        self._life += points_change
    
    
    def get_life(self):
        return self._life
    
    
    def draw_life_number(self):
        """ Draw how many hit points we have """

        health_string = f"{self._life}/{self.cur_health}"
        arcade.draw_text(health_string,
                         start_x=self.center_x + constants.HEALTH_NUMBER_OFFSET_X,
                         start_y=self.center_y + constants.HEALTH_NUMBER_OFFSET_Y,
                         font_size=9,
                         color=arcade.color.WHITE)

    def draw_life_bar(self):
        """ Draw the health bar """

        # Draw the 'unhealthy' background
        if self.cur_health < self._life:
            arcade.draw_rectangle_filled(center_x=self.center_x,
                                         center_y=self.center_y + constants.HEALTHBAR_OFFSET_Y,
                                         width=constants.HEALTHBAR_WIDTH,
                                         height=3,
                                         color=arcade.color.BLACK)

        # Calculate width based on health
        health_width = constants.HEALTHBAR_WIDTH * ( self._life  /self.cur_health  )
        arcade.draw_rectangle_filled(center_x=self.center_x - 0.5 * (constants.HEALTHBAR_WIDTH - health_width),
                                     center_y=self.center_y - 10,
                                     width=health_width,
                                     height= constants.HEALTHBAR_HEIGHT,
                                     color=arcade.color.GREEN)

    def update(self):
        """ Updates the sprite as it rotates on the screen
        Contributors:
            Reed Hunsaker
        """
        # Convert angle in degrees to radians.
        angle_rad = math.radians(self.angle)

        # Rotate the tank
        self.angle += self.change_angle

        # Use math to find our change based on our speed and angle
        self.center_x += -self.speed * math.sin(angle_rad) # This could be essing with the tank speed, sort of randomizing it
        self.center_y += self.speed * math.cos(angle_rad)  # same here

class Player1(Tanks):
    """ Class that represent the player1 on screen.
    Stereotype:
        Information Holder
    Attributes:
        center_x (integer): x pixel value of the center of sprite
        texture (string): file path of player1 sprite
    Contributors:
        Reed Hunsaker
    """
    def __init__(self):
        super().__init__()
        self.name = 0
        self.center_x = randint(450, 810)
        self.center_y = randint(250, 500)
        self.texture = self.player1_texture

class Player2(Tanks):
    """Class that represent the player2 on screen.
    Stereotype:
        Information Holder
    Attributes:
        center_x (integer): x pixel value of the center of sprite
        texture (string): file path of player2 sprite
    Contributors:
        Reed Hunsaker
    """
    def __init__(self):
        super().__init__()
        self.name = 1
        self.center_x = randint(50, 450)
        self.center_y = randint(10, 250)
        self.texture = self.player2_texture

class Run:
    """Class that represent the player2 on screen.
    Stereotype:
        Controller
    Attributes:
        sprite_list (aracde.SpriteList): creates sprite list for the tanks
        player1 (Player1): initializes player1
        player2 (Player2): initializes player2
    Contributors:
        Reed Hunsaker
    """
    def __init__(self):
        self.sprite_list = arcade.SpriteList()
        self.player1 = Player1()
        self.player2 = Player2()

        self.sprite_list.append(self.player1)
        self.sprite_list.append(self.player2)