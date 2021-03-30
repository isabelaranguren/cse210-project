import arcade
from arcade.gui import UIImageButton, UIManager
import game.constants as constants
from game.gameview import GameView

class MainView(arcade.View):
    """ View to show instructions """
    
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture(constants.CAMO)
        self.ui_manager = UIManager()
        

    def on_show(self):
        """ This is run once when we switch to this view """
        self.setup()
        self.texture = arcade.load_texture(constants.CAMO)
    
    def on_hide_view(self):
        self.ui_manager.unregister_handlers()
            
    def setup(self):
        self.ui_manager.purge_ui_elements()

        y_slot = self.window.height // 4
        left_column_x = self.window.width // 4
        right_column_x = 3 * self.window.width // 4

        # self.settings_texture = arcade.load_texture(constants.SETTINGS_SPRITE)
        # self.settings_button = Settings_Button(game = self.window, normal_texture= self.settings_texture)

        self.play_texture = arcade.load_texture(constants.PLAY_SPRITE)
        self.play_button = Button(GameView(), self.window, normal_texture= self.play_texture, y = constants.BUTTON_Y + 20)


        self.instruct_texture = arcade.load_texture(constants.INSTRUCT_SPRITE)
        self.instruct_button = Button(InstructionView(), self.window, normal_texture = self.instruct_texture, 
        y = constants.BUTTON_Y - 70)

        # self.ui_manager.add_ui_element(self.settings_button)
        self.ui_manager.add_ui_element(self.play_button)
        self.ui_manager.add_ui_element(self.instruct_button)
        

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        self.texture.draw_sized(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2,
                                constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        # arcade.draw_text("Tank Wars", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2,
        #                  arcade.color.WHITE, font_size=50, anchor_x="center")

class Button(UIImageButton):
    def __init__(self, view, game, x = constants.PLAY_X, y = constants.BUTTON_Y,  text = "",
    normal_texture = None):
        super().__init__(center_x= x, center_y= y,
        text = text, normal_texture = normal_texture)
        self.view = view
        self.center_x = x
        self.center_y = y
        self.window = game

    def on_click(self):
        self.view.setup()
        self.window.show_view(self.view)


# class Settings_Button(UIImageButton):
#     def __init__(self, game, x = constants.SETTINGS_X, y = constants.SETTINGS_Y, normal_texture = None):
#         super().__init__(center_x= x, center_y= y, normal_texture= normal_texture)
#         self.center_x = x
#         self.center_y = y
#         self.window = game


#     def on_click(self):
#         view = SettingsView()
#         view.setup()
#         self.window.show_view(view)


class InstructionView(arcade.View):
    def __init__(self):
        super().__init__()
        self.ui_manager = UIManager()
        self.texture = arcade.load_texture(constants.INSTRUCTION_BKG)

    def on_show(self):
        self.setup()
    
    def on_hide_view(self):
        self.ui_manager.unregister_handlers()

    
    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        self.texture.draw_sized(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2,
                                constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)

    def setup(self):
        self.ui_manager.purge_ui_elements()

        self.back_texture = arcade.load_texture(constants.BACK_SPRITE)
        self.back_button = Button(MainView(), self.window, x = constants.BACK_X, y = constants.BACK_Y,
        normal_texture= self.back_texture)

        self.ui_manager.add_ui_element(self.back_button)
    
    def on_show_view(self):
        arcade.load_texture(constants.CAMO)


class SettingsView(arcade.View):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture(constants.PLACEHOLDER)

        self.ui_manager = UIManager()

#     def on_show(self):
#         self.setup()
    
#     def on_hide_view(self):
#         self.ui_manager.unregister_handlers()
    
#     def setup(self):
#         self.ui_manager.purge_ui_elements()

#         self.back_texture = arcade.load_texture(constants.BACK_SPRITE)
#         self.back_button = Button(MainView(), self.window, x = constants.BACK_X, y = constants.BACK_Y,
#         normal_texture= self.back_texture)

#         self.ui_manager.add_ui_element(self.back_button)
    
