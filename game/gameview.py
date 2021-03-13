import arcade

import game.constants
from game.tanks import Run
from game.ground import Ground

class Gameview(arcade.View):
    def __init__(self):
        super().__init__()

        self.setup()
    
    def setup(self):
        self.tanks = Run()
        self.ground = Ground()
    
    def on_draw(self):
        self.tanks.sprite_list.draw()
        self.ground.ground_sprite_list.draw()

    def on_update(self, delta_time: float):
        pass
        