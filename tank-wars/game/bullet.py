import arcade
import game.constants as constants
import math
import numpy as np

class BulletSprite(arcade.Sprite):
    """Class that represent bullet sprites on the screen
    Stereotype:
        Information Holder
    Attributes:
        texture (arcade.load_texture): file path for bullet texture using arcade.load_texture
        scale (integer): scale of sprite
        speed (integer): speed of bullet
        tank_fire (string): file path for bullet sound effect when fired using arcade.load_sound
    Contributors:
        Reed Hunsaker
        Adrianna Lund
    """
    def __init__(self):
        """Initialize the BulletSprite class

        Args:
            self (BulletSprite): an instance of BulletSprite.
        Contributors:
            Reed Hunsaker
            Adrianna Lund
        """
        super().__init__()

        self.texture = arcade.load_texture(file_name= constants.BULLET_SPRITE)
        self.scale = constants.BULLET_SCALE
        self.speed = constants.BULLET_SPEED
        self.tank_fire = arcade.load_sound(constants.TANK_FIRE)



class Bullet:
    """Class that represent bullet sprites on the screen
    Stereotype:
        Information Holder
    Attributes:
        bullet_sprite_list (aracde.SpriteList): creates a sprite list for the bullets
    Contributors:
        Reed Hunsaker
        Adrianna Lund
    """
    def __init__(self):
        """Initialize the Bullet class

        Args:
            self (Bullet): an instance of Bullet.
        Contributors:
            Reed Hunsaker
            Adrianna Lund
        """
        super().__init__()
        self.bullet_sprite_list = arcade.SpriteList()
        
    def shoot_bullet(self,tank_x, tank_y, tank_angle):
        """Function to shoot the bullet and to rotate bullet to match tank angle

        Args:
            self (Bullet): an instance of Bullet.
            tank_x (integer): x position of tank
            tank_y (integer): y position of tank
            tank_angle (integer): angle of tank
        contributors:
            Reed Hunsaker
            Adrianna Lund
        """
        self.bullet = BulletSprite()
        self.bullet.change_y = -math.cos(math.radians(tank_angle)) * self.bullet.speed
        self.bullet.change_x = math.sin(math.radians(tank_angle)) * self.bullet.speed
        self.bullet.center_x = tank_x + (self.bullet.change_x * constants.BULLET_X_SCALE)
        self.bullet.center_y = tank_y + (self.bullet.change_y * constants.BULLET_Y_SCALE)
        self.bullet.angle = math.degrees(math.atan2(self.bullet.change_y, self.bullet.change_x))
        self.bullet_sprite_list.append(self.bullet)
        try:
            arcade.play_sound(self.bullet.tank_fire,.4)
        except Exception:
            pass
        # Convert angle in degrees to radians.
        self.bullet.update()
    
    def bullet_bounce(self, bullet, tank_angle):
        """Changes bullet direction when sprite interacts with wall

        Args:
            self (Bullet): an instance of Bullet
            bullet (object): Bullet object initiated in GameView
            tank_angle (float): Angle of the bullet
        Contributors:
            Reed Hunsaker
            Adrianna Lund
        """
        bullet.change_y = -math.cos(math.radians(np.pi + tank_angle)) * self.bullet.speed
        bullet.change_x = math.sin(math.radians(np.pi + tank_angle)) * self.bullet.speed
        bullet.angle = math.degrees(math.atan2(bullet.change_y, bullet.change_x))

