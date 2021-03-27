import arcade
import game.constants as constants
from game.gameview import GameView
from game.instruction_view import MainView
from game.score import Score


class Window(arcade.Window):
    def __init__(self):
        super().__init__(constants.X_CONSTANT, constants.Y_CONSTANT, constants.TITLE)

        self.master_volume = constants.DEFAULT_VOLUME

        self.score = Score()
        self.start_view = MainView()
        self.background_music = arcade.Sound(constants.MAIN_SCREEN_SOUND)
        self.background_music.play(self.master_volume, loop = True)

    def reset_gameview(self):
        gameview = GameView()
        return gameview
    

def main():
    window = Window()
    start_view = MainView()
    window.show_view(start_view)
    arcade.run()

if __name__ == "__main__":
    main()