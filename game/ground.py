import arcade
import game.constants as constants
from random import randint


from random import randint


class GroundSprite(arcade.Sprite):
    def __init__(self):
        super().__init__()

        self.center_y = constants.GROUND_Y
        self.texture = arcade.load_texture(file_name=constants.GROUND_SPRITE)
        self.scale = constants.GROUND_SCALE


class Ground:
    """    def __init__(self):
        self.point_list = []
    """
    def __init__(self):
        self.create_ground()
        """self.ground_sprite_list = arcade.SpriteList(use_spatial_hash= True)
        for x in range(0,1250,64):
            ry = randint(0,32)
            for y in range(0, ry):
                self.ground = GroundSprite()
                self.ground.center_x = x
                self.ground.center_y = y
                self.ground_sprite_list.append(self.ground)"""

    def create_ground(self):


        self.ground_point_list = []
        previous_random_y = randint(0, 300)
        for x in range(0, 800, 50):
            for y in range(0, previous_random_y):
                new_random_y = randint(previous_random_y-5, previous_random_y + 5)
                self.ground_point_list.append((x, new_random_y))
        self.ground_sprite_list = arcade.create_polygon(self.ground_point_list, arcade.color.ROSE)
        # self.ground_sprite_list = arcade.draw_polygon_filled(self.ground_point_list, arcade.color.ROSE)

    """def create_ground(self):
        for x in range(0, 800, 10):
            for y in range(0, 600, 10):
                print(x, y)
                self.point_list.append((x, y))
        arcade.draw_polygon_filled(self.point_list, arcade.color.AIR_FORCE_BLUE)
    """