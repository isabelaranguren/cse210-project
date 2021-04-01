import arcade
import game.constants as constants
from random import randint


class PowerUp(arcade.Sprite):
    """
    Power ups for Tank Wars
    Stereotype:
        Information Holder
    Attributes:
        speed (speed): initializes power up speed
        scale (constants.TANK_SCALE/2): initializes power up scale
        center_x (random integer): initializes power up center x
        center_y (random integer): initializes power up center y
        value (value): initializes power up value. Used to differentiate between various power ups
        power_texture (arcade.load_texture): load power up texture
        texture (power_texture): initializes power up texture
    Contributors:
        Jordan McIntyre
        Adrianna Lund
        """
    def __init__(self, value):
        """Initalize the PowerUp class
        
        Attributes:
            self (PowerUp): An instance of the PowerUp
            value (integer): 0 is power down, 1 is power up, 2 is explode
        Contributors:
            Reed Hunsaker
            Jordan McIntyre
        """
        super().__init__()
        self.speed = 0
        self.scale = constants.TANK_SCALE/2
        self.center_y = randint(25, constants.Y_CONSTANT - 25)
        self.center_x = randint(25, constants.X_CONSTANT - 25)
        self.value = value
        self.power_texture = arcade.load_texture(file_name=constants.HEALTH_POWER_UP_SPRITE)
        self.texture = self.power_texture

    def get_value(self):
        """
        Returns: self.value
        Args:
            self (PowerUp): An instance of PowerUp
        Contributors:
            Jordan McIntyre
            Adrianna Lund
        """
        return self.value


class SpawnRandom:
    """ Creates a PowerUp with a random value
    Stereotype:
        Information Holder
    Attributes:
        sprite_list (arcade.SpriteList): Initializes a sprite list
        power (PowerUp): Creates a PowerUp with a random value
    Contributors:
        Jordan McIntyre
    """
    def __init__(self):
        """
        Initialize SpawnRandom class
        Args:
            self (SpawnRandom): An instance of SpawnRandom
        Contributors:
            Jordan McIntyre
            Adrianna Lund
        """
        self.sprite_list = arcade.SpriteList()
        random_number = randint(0, 2)
        self.power = PowerUp(random_number)
        self.sprite_list.append(self.power)