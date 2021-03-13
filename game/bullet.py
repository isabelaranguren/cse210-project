import arcade
import game.constants as constants

class BulletSprite(arcade.Sprite):
    def __init__(self):
        super().__init__()

        self.texture = arcade.load_texture(file_name= constants.BULLET_SPRITE)
        self.scale = constants.BULLET_SCALE


class Bullet:
    def __init__(self):
        super().__init__()
        self.bullet = BulletSprite()
        self.bullet_sprite_list = arcade.SpriteList()
        self.bullet_sprite_list.append(self.bullet)

    def shoot_bullet(self):
        self.bullet.center_x = 300
        self.bullet.center_y = 155
        self.bullet.velocity = constants.BULLET_INITIAL_VELOCITY