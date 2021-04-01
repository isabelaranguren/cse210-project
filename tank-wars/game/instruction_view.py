import arcade
from arcade.gui import UIImageButton, UIManager, UIToggle
import game.constants as constants
from game.gameview import GameView

class MainView(arcade.View):
    """ View to show start screen. The responsibility of this class is to
    offer the user to either play or view the instructions
    Stereotype:
        Interfacer
    Attributes:
        texture (arcade.load_texture): Loads the texture in the background
        ui_manager (UIManager): Imports the user interface manager
    Contributors:
        Reed Hunsaker
        Isabel Aranguren
    """
    
    def __init__(self):
        """Initalize the MainView class
        Arguments:
            self (MainView): An instance of MainView
        contributors:
            Reed Hunsaker
            Isabel Aranguren
        """
        super().__init__()
        self.texture = arcade.load_texture(constants.CAMO)
        self.ui_manager = UIManager()
        

    def on_show(self):
        """ run as the view appears
        Arguments:
            self (MainView): An instance of MainView
        contributors:
            Reed Hunsaker
            Isabel Aranguren
        """
        self.setup()
        self.texture = arcade.load_texture(constants.CAMO)
    
    def on_hide_view(self):
        """Method to unregestor the handlers of the ui
        Arguments:
            self (MainView): An instance of MainView
        contributors:
            Reed Hunsaker
            Isabel Aranguren
        """
        self.ui_manager.unregister_handlers()
            
    def setup(self):
        """ Setup the view
        Arguments:
            self (MainView): An instance of MainView
        contributors:
            Reed Hunsaker
            Isabel Aranguren
        """
        self.ui_manager.purge_ui_elements()

        y_slot = self.window.height // 4
        left_column_x = self.window.width // 4
        right_column_x = 3 * self.window.width // 4


        self.play_texture = arcade.load_texture(constants.PLAY_SPRITE)
        self.play_button = Button(GameView(), self.window, normal_texture= self.play_texture, y = constants.BUTTON_Y + 20)


        self.instruct_texture = arcade.load_texture(constants.INSTRUCT_SPRITE)
        self.instruct_button = Button(InstructionView(), self.window, normal_texture = self.instruct_texture, 
        y = constants.BUTTON_Y - 70)

        # self.ui_manager.add_ui_element(self.settings_button)
        # self.ui_manager.add_ui_element(self.sound_toggle)
        self.ui_manager.add_ui_element(self.play_button)
        self.ui_manager.add_ui_element(self.instruct_button)
        

    def on_draw(self):
        """ Draw this view 
        Arguments:
            self (MainView): An instance of MainView
        contributors:
            Reed Hunsaker
            Isabel Aranguren
        """
        arcade.start_render()
        self.texture.draw_sized(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2,
                                constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        # arcade.draw_text("Tank Wars", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2,
        #                  arcade.color.WHITE, font_size=50, anchor_x="center")

class Button(UIImageButton):
    """ Class for the buttons used in the Instruction and Main view
    Stereotype:
        Information holder
    Attributes:
        view (object): view in which the button will bring up
        center_x (integer): center x pixel of the button
        center_y (integer): center y pixel of the button
        window (Window): the current instance of the window class
    Contributors:
        Reed Hunsaker
    """
    def __init__(self, view, game, x = constants.PLAY_X, y = constants.BUTTON_Y,  text = "",
    normal_texture = None):
        """ Initalize the button view
        Arguments:
            self (Button): An instance of Button
            view (object): view in which the button will bring up
            game (Window): Current instance of the window
            x (integer): center x pixel of the button
            y (integer): center y pixel of the button
            text (str): text for button
            normal_texture (arcade.load_texture): loaded file path
        contributors:
            Reed Hunsaker
        """
        super().__init__(center_x= x, center_y= y,
        text = text, normal_texture = normal_texture)
        self.view = view
        self.center_x = x
        self.center_y = y
        self.window = game

    def on_click(self):
        """ Action that takes place on click
        Arguments:
            self (Button): An instance of Button
        contributors:
            Reed Hunsaker
        """
        self.view.setup()
        self.window.show_view(self.view)


class InstructionView(arcade.View):
    """ View to show instructions. The responsibility of this class is give
    information to the user in a window about how the game is played.
    Stereotype:
        Interfacer
    Attributes:
        texture (arcade.load_texture): Loads the texture in the background
        ui_manager (UIManager): Imports the user interface manager
    Contributors:
        Reed Hunsaker
        Isabel Aranguren
    """
    def __init__(self):
        """ Initalize the InstructionView class
        Arguments:
            self (InstructionView): An instance of InstructionView
        contributors:
            Reed Hunsaker
        """
        super().__init__()
        self.ui_manager = UIManager()
        self.texture = arcade.load_texture(constants.INSTRUCTION_BKG)

    def on_show(self):
        """ Run the setup menu on pop up
        Arguments:
            self (InstructionView): An instance of InstructionView
        contributors:
            Reed Hunsaker
        """
        self.setup()
    
    def on_hide_view(self):
        """ unregister ui handlers
        Arguments:
            self (InstructionView): An instance of InstructionView
        contributors:
            Reed Hunsaker
        """
        self.ui_manager.unregister_handlers()

    
    def on_draw(self):
        """ Draw the view
        Arguments:
            self (InstructionView): An instance of InstructionView
        contributors:
            Reed Hunsaker
            Isabel Aranguren
        """
        arcade.start_render()
        self.texture.draw_sized(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2,
                                constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)

    def setup(self):
        """ Setup elements in view
        Arguments:
            self (InstructionView): An instance of InstructionView
        contributors:
            Reed Hunsaker
            Isabel Aranguren
        """
        self.ui_manager.purge_ui_elements()

        self.back_texture = arcade.load_texture(constants.BACK_SPRITE)
        self.back_button = Button(MainView(), self.window, x = constants.BACK_X, y = constants.BACK_Y,
        normal_texture= self.back_texture)

        self.ui_manager.add_ui_element(self.back_button)
    
    def on_show_view(self):
        """ Load background texture
        Arguments:
            self (InstructionView): An instance of InstructionView
        contributors:
            Reed Hunsaker
            Isabel Aranguren
        """
        arcade.load_texture(constants.CAMO)

