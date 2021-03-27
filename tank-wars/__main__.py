import arcade
import game.constants as constants
from game.gameview import GameView
from game.instruction_view import InstructionView
from game.score import Score


class Window(arcade.Window):
    def __init__(self):
        super().__init__(constants.X_CONSTANT, constants.Y_CONSTANT, constants.TITLE)
        self.score = Score()
        self.start_view = InstructionView()
        self.music = arcade.load_sound(constants.MAIN_SCREEN_SOUND)
        arcade.play_sound(self.music,0.1, looping = True)
    def reset_gameview(self):
        gameview = Game
        View()
        return gameview

def main():
    window = Window()
    start_view = InstructionView()
    window.show_view(start_view)
    arcade.run()

if __name__ == "__main__":
    main()