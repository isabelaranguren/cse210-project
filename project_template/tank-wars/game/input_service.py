'''
source: https://realpython.com/arcade-python-game-framework/
'''

import arcade

class Input_Service(arcade.Window):
    
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
            self.actor.change_y = 5

        if symbol == arcade.key.K or symbol == arcade.key.DOWN:
            self.actor.change_y = -5

        if symbol == arcade.key.J or symbol == arcade.key.LEFT:
            self.actor.change_x = -5

        if symbol == arcade.key.L or symbol == arcade.key.RIGHT:
            self.actor.change_x = 5

    def on_key_release(self, symbol: int, modifiers: int, actor):
        """Undo movement vectors when movement keys are released

        Arguments:
            symbol {int} -- Which key was pressed
            modifiers {int} -- Which modifiers were pressed
            actor -- which will be modified (tank1 or tank2)
        """
        if (
            symbol == arcade.key.I
            or symbol == arcade.key.K
            or symbol == arcade.key.UP
            or symbol == arcade.key.DOWN
        ):
            self.actor.change_y = 0

        if (
            symbol == arcade.key.J
            or symbol == arcade.key.L
            or symbol == arcade.key.LEFT
            or symbol == arcade.key.RIGHT
        ):
            self.actor.change_x = 0