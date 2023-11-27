import arcade
from game import constants

class GameOverView(arcade.View):
    """ View to show when game is over 
    Stereotype:
        Information Holder
    Attributes:
        texture (arcade.load_texture): load the texture
        lose (integer): either 0 or 1 for Green wins or Black wins
        win_text (string): Display text for game over view
        winner (method): calls the winner method
    Contributors:
        Reed Hundsaker
        Isabel Aranguren
    """

    def __init__(self, loser):
        """ This is run once when we switch to this view 
        Args:
            self (GameOverView): an intance of GameOverView
            loser(integer): 0 or 1 for Green wins or Black wins
        Contributors:
            Reed Hunsaker
            Isabel Aranguren
        """
        super().__init__()
        self.texture = arcade.load_texture(constants.GAME_OVER)
        self.loser = loser
        self.win_text = ""
        self.winner()
        
    def on_draw(self):
        """ Draw this view 
        Args:
            self (GameOverView): an intance of GameOverView
        Contributors:
            Reed Hunsaker
            Isabel Aranguren
        """
        arcade.start_render()
        self.texture.draw_sized(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2,
                                constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        arcade.draw_text(f"{self.win_text}", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 4-75,
                         arcade.color.WHITE, font_size=20, anchor_x="center")
        arcade.draw_text("Press a key to play again!", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT *(3/4),
                         arcade.color.WHITE, font_size=20, anchor_x="center")
        arcade.draw_text(f"Black Tank: {self.window.score.get_score_player1()} | Green Tank: {self.window.score.get_score_player2()}", 
        constants.SCREEN_WIDTH / 2,
        constants.SCREEN_HEIGHT / 6 -75,
        arcade.color.WHITE, 
        font_size=20, 
        anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ Method from arcade.View to get mouse events. 
        Args:
            self (GameOverView): an intance of GameOverView
        Contributors:
            Reed Hunsaker
            Isabel Aranguren
        """
        game_view = self.window.reset_gameview()
        game_view.setup()
        self.window.show_view(game_view)
    
    def on_key_press(self, symbol, modifiers):
        """ Method from arcade.View to get key events. 
        Args:
            self (GameOverView): an intance of GameOverView
        Contributors:
            Reed Hunsaker
            Isabel Aranguren
            Jordan McIntyre
        """
        game_view = self.window.reset_gameview()
        game_view.setup()
        self.window.show_view(game_view)
    
    def winner(self):
        """ Checks the winner and sets display text
        Args:
            self (GameOverView): an intance of GameOverView
        Contributors:
            Reed Hunsaker
            Isabel Aranguren
        """
        if self.loser == 0:
            self.window.score.add_score_player2()
            self.win_text = "Green Tank Wins!"
        elif self.loser == 1:
            self.window.score.add_score_player1()
            self.win_text = "Black Tank Wins!"
        else:
            self.win_text = '404 no winner found'
