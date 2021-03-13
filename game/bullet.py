import arcade
import game.constants as constants

class BulletSprite(arcade.Sprite):
    def __init__(self):
        super().__init__()

        self.texture = arcade.load_texture(file_name= constants.BULLET_SPRITE)


class Bullet:
    def __init__(self):
        super().__init__()

        self.bullet = BulletSprite()
        self.bullet_sprite_list = arcade.SpriteList()