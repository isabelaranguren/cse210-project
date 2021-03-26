import arcade
import game.constants as constants
from random import randint


class PowerUp(arcade.Sprite):
    def __init__(self, value):
        super().__init__()
        self.speed = 0
        self.scale = constants.TANK_SCALE/2
        self.center_y = randint(25, constants.Y_CONSTANT - 25)
        self.center_x = randint(25, constants.X_CONSTANT - 25)
        self.value = value

        self.power_texture = arcade.load_texture(file_name=constants.HEALTH_POWER_UP_SPRITE)
        self.texture = self.power_texture
        # self.health_boost_texture = arcade.load_texture(file_name=constants.HEALTH_POWER_UP_SPRITE)
        # self.health_penalty_texture = arcade.load_texture(file_name=constants.HEALTH_POWER_DOWN_SPRITE)

    def get_value(self):
        return self.value


class PowerDown(PowerUp):
    def __init__(self):
        super(PowerDown, self).__init__(0)
        self.scale = constants.TANK_SCALE / 2
        self.texture = self.power_texture
        self.value = 0
        # self.description = "Bad"


class HealthBoost(PowerUp):
    def __init__(self):
        super(HealthBoost, self).__init__(1)
        self.texture = self.power_texture
        self.scale = constants.TANK_SCALE / 2
        self.value = 1
        # self.description = "Good"


class ShootBoost(PowerUp):
    def __init__(self):
        super().__init__(2)
        self.texture = self.power_texture
        self.scale = constants.TANK_SCALE/2
        self.value = 2
        # self.description = "Shoot twice"

# Use SpawnRandom() instead
class SpawnPowerDown:
    def __init__(self):
        # power down list
        self.sprite_list = arcade.SpriteList()

        self.power_down = PowerDown()

        self.sprite_list.append(self.power_down)


# Use SpawnRandom() instead
class SpawnPowerUp:
    def __init__(self):
        # power up list
        self.sprite_list = arcade.SpriteList()

        self.power_up = HealthBoost()

        self.sprite_list.append(self.power_up)


class SpawnRandom:
    def __init__(self):
        # The only difference between the powerups is the value. Maybe just have a generic powerup and set a random value?
        self.sprite_list = arcade.SpriteList()
        random_number = randint(0, 3)
        self.power = PowerUp(random_number)
        """if random_number % 4 == 0:
            self.power = PowerUp(3)
        elif random_number % 3 == 1:
            self.power = PowerUp(3)
        elif random_number % 3 == 2:
            self.power = PowerUp(3)"""
        """elif random_number % 4 == 3:
            self.power = PowerUp(3)
        print("SpawnRandom is initializing!")"""

        self.sprite_list.append(self.power)