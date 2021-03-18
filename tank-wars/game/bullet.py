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
        super().__init__()
        self.bullet_sprite_list = arcade.SpriteList()
        self.bounce = 0
        
    def shoot_bullet(self,tank_x, tank_y, tank_angle):
        """Function to shoot the bullet and to rotate bullet to match tank angle

        Attributes:
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
        # self.bullet.velocity = constants.BULLET_INITIAL_VELOCITY
        self.bullet_sprite_list.append(self.bullet)
        arcade.play_sound(self.bullet.tank_fire)
        # Convert angle in degrees to radians.
        self.bullet.update()
    
    def bullet_bounce(self, bullet, tank_angle):
        bullet.change_y = -math.cos(math.radians(np.pi + tank_angle)) * self.bullet.speed
        bullet.change_x = math.sin(math.radians(np.pi + tank_angle)) * self.bullet.speed
        bullet.angle = math.degrees(math.atan2(bullet.change_y, bullet.change_x))
    
    def get_bounces(self):
        self.bounce +=1
        return self.bounce