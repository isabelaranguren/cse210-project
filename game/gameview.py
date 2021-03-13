import arcade

import game.constants
from game.tanks import Run
from game.ground import Ground
from game.bullet import Bullet

class Gameview(arcade.View):
    def __init__(self):
        super().__init__()

        self.setup()
    
    def setup(self):
        self.tanks = Run()
        self.ground = Ground()
        self.bullet = Bullet()
        self.bullet.shoot_bullet()
    
    def on_draw(self):
        arcade.start_render()
        self.tanks.sprite_list.draw()
        # self.ground.ground_sprite_list.draw()

    def on_update(self, delta_time: float):
        self.bullet.bullet_sprite_list.update()
        self.bullet.bullet_sprite_list.update_animation()
