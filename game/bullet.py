import arcade
import game.constants as constants
import math

class BulletSprite(arcade.Sprite):
    def __init__(self):
        super().__init__()

        self.texture = arcade.load_texture(file_name= constants.BULLET_SPRITE)
        self.scale = constants.BULLET_SCALE
        self.speed = constants.BULLET_SPEED
        self.tank_fire = arcade.load_sound(constants.TANK_FIRE)



class Bullet:
    def __init__(self):
        super().__init__()
        self.bullet_sprite_list = arcade.SpriteList()
        
    def shoot_bullet(self,tank_x, tank_y, tank_angle):
        self.bullet = BulletSprite()
        self.bullet.change_y = -math.cos(math.radians(tank_angle)) * self.bullet.speed
        self.bullet.change_x = math.sin(math.radians(tank_angle)) * self.bullet.speed
        self.bullet.center_x = tank_x + (self.bullet.change_x * 9)
        self.bullet.center_y = tank_y + (self.bullet.change_y * 9)
        self.bullet.angle = math.degrees(math.atan2(self.bullet.change_y, self.bullet.change_x))
        # self.bullet.velocity = constants.BULLET_INITIAL_VELOCITY
        self.bullet_sprite_list.append(self.bullet)
        arcade.play_sound(self.bullet.tank_fire)
        # Convert angle in degrees to radians.
        self.bullet.update()
        