import arcade
import game.constants as constants

class BulletSprite(arcade.Sprite):
    def __init__(self):
        super().__init__()

        self.texture = arcade.load_texture(file_name= constants.BULLET_SPRITE)
        self.scale = constants.BULLET_SCALE

        self.tank_fire = arcade.load_sound(constants.TANK_FIRE)


class Bullet:
    def __init__(self):
        super().__init__()
        self.bullet = BulletSprite()
        # self.bullet_sprite_list = arcade.SpriteList()
        # self.bullet_sprite_list.append(self.bullet)

    def shoot_bullet(self,tank_x, tank_y):
        self.bullet.center_x = tank_x
        self.bullet.center_y = tank_y
        self.bullet.velocity = constants.BULLET_INITIAL_VELOCITY
        self.bullet_sprite_list = arcade.SpriteList()
        self.bullet_sprite_list.append(self.bullet)
        arcade.play_sound(self.tank_fire)
