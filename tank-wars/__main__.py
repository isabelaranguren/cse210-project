import arcade
import game.constants as constants
from game.gameview import GameView
from game.instruction_view import MainView
from game.score import Score

class Window(arcade.Window):
    """Open and control main window
    Stereotype:
        Controller
    Attributes: 
        master_volume(file_path): file path for volume
        score (Score): initalize the score class
        background_music (arcade.Sound): initalize background music in arcade.Sound
    Contributors:
            Isabel Aranguren
            Reed Hunsaker
    """
    def __init__(self):
        """Initalize the Window class
        Args:
            self (Window): an instance of Window
        Contributors:
            Reed Hunsaker
            Isabel Aranguren
        """
        super().__init__(constants.X_CONSTANT, constants.Y_CONSTANT, constants.TITLE)

        self.master_volume = constants.DEFAULT_VOLUME

        self.score = Score()
        self.start_view = MainView()
        self.background_music = arcade.Sound(constants.MAIN_SCREEN_SOUND)
        self.background_music.play(self.master_volume, loop = True)

    def reset_gameview(self):
        """Reset the GameView when there is a new game
        Args:
            self (Window): an instance of Window
        Contributors:
            Reed Hunsaker
            Isabel Aranguren
        """
        gameview = GameView()
        return gameview
    

def main():
    """Run the game
    Contributors:
        Reed Hunsaker
        Adrianna Lund
        Jordan McIntyre
        Isabel Aranguren
    """
    window = Window()
    start_view = MainView()
    window.show_view(start_view)
    arcade.run()

if __name__ == "__main__":
    main()