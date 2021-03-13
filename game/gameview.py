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
        
    def on_key_press(self, symbol, modifiers, actor):
        """Handle user keyboard input
        Q: Quit the game
        P: Pause/Unpause the game
        I/J/K/L: Move Up, Left, Down, Right
        Arrows: Move Up, Left, Down, Right

        Arguments:
            symbol {int} -- Which key was pressed
            modifiers {int} -- Which modifiers were pressed
            actor -- which sprite will be modified (tank1 or tank2)
        """
        if symbol == arcade.key.Q:
            # Quit immediately
            arcade.close_window()

        if symbol == arcade.key.P:
            self.paused = not self.paused

        if symbol == arcade.key.I or symbol == arcade.key.UP:
            self.bullet.change_y = 5
            # change the angle of the barrel/bullet

        if symbol == arcade.key.K or symbol == arcade.key.DOWN:
            self.bullet.change_y = -5
            # change the angle of the barrel/bullet

        # if symbol == arcade.key.J or symbol == arcade.key.LEFT:
        #     self.actor.change_x = -5
            # decrease the power

        # if symbol == arcade.key.L or symbol == arcade.key.RIGHT:
        #     self.actor.change_x = 5
            # increase the power

    # def on_key_release(self, symbol: int, modifiers: int, actor):
    #     """Undo movement vectors when movement keys are released

    #     Arguments:
    #         symbol {int} -- Which key was pressed
    #         modifiers {int} -- Which modifiers were pressed
    #         actor -- which will be modified (tank1 or tank2)
    #     """
    #     if (
    #         symbol == arcade.key.I
    #         or symbol == arcade.key.K
    #         or symbol == arcade.key.UP
    #         or symbol == arcade.key.DOWN
    #     ):
    #         self.actor.change_y = 0

    #     if (
    #         symbol == arcade.key.J
    #         or symbol == arcade.key.L
    #         or symbol == arcade.key.LEFT
    #         or symbol == arcade.key.RIGHT
    #     ):
    #         self.actor.change_x = 0