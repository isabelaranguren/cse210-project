import arcade
import game.constants
from game.gameview import GameView
from game.instruction_view import InstructionView
from game.score import Score


class Window(arcade.Window):
    def __init__(self):
        super().__init__(game.constants.X_CONSTANT, game.constants.Y_CONSTANT, game.constants.TITLE)
        self.score = Score()
        self.start_view = InstructionView()
    
    def reset_gameview(self):
        gameview = GameView()
        return gameview

def main():
    window = Window()
    start_view = InstructionView()
    window.show_view(start_view)
    arcade.run()

if __name__ == "__main__":
    main()