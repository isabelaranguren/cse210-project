import arcade
import game.constants as constants
from random import randint


class PowerUp(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 0
        self.scale = constants.TANK_SCALE
        self.center_y = randint(25, constants.Y_CONSTANT - 25)
        self.center_x = randint(25, constants.X_CONSTANT - 25)

        self.health_boost_texture = arcade.load_texture(file_name=constants.HEALTH_POWER_UP_SPRITE)
        self.health_penalty_texture = arcade.load_texture(file_name=constants.HEALTH_POWER_DOWN_SPRITE)


class PowerDown(PowerUp):
    def __init__(self):
        super(PowerDown, self).__init__()
        self.scale = constants.TANK_SCALE / 2
        self.texture = self.health_penalty_texture  # self.health_boost_texture  #
        self.description = "Power Down Box"


class HealthBoost(PowerUp):
    def __init__(self):
        super(HealthBoost, self).__init__()
        self.texture = self.health_boost_texture
        # self.center_y = constants.TANK_Y + 150  # can randomize
        # self.center_x = constants.PLAYER1_X - 50  # can randomize
        self.scale = constants.TANK_SCALE / 2
        self.description = "Health Boost"


class SpawnPowerDown:
    def __init__(self):
        # power down list
        self.sprite_list = arcade.SpriteList()

        self.power_down = PowerDown()

        self.sprite_list.append(self.power_down)


class SpawnPowerUp:
    def __init__(self):
        # power up list
        self.sprite_list = arcade.SpriteList()

        self.power_up = HealthBoost()

        self.sprite_list.append(self.power_up)




