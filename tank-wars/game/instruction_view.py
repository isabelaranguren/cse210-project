import arcade
from arcade.gui import UIImageButton, UIManager, UIToggle
import game.constants as constants
from game.gameview import GameView

class MainView(arcade.View):
    """ View to show instructions """
    
    def __init__(self):
        super().__init__()

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

        self.normal_sound_texture = arcade.load_texture(constants.TOGGLE_ON_SPRITE)
        self.pressed_sound_texture = arcade.load_texture(constants.TOGGLE_OFF_SRITE)
        self.sound_toggle = SoundToggle(normal = self.normal_sound_texture, pressed = self.pressed_sound_texture,
        game = self.window)


        self.play_texture = arcade.load_texture(constants.PLAY_SPRITE)
        self.play_button = Button(GameView(), self.window, normal_texture= self.play_texture)


        self.instruct_texture = arcade.load_texture(constants.INSTRUCT_SPRITE)
        self.instruct_button = Button(InstructionView(), self.window, normal_texture = self.instruct_texture, 
        y = constants.BUTTON_Y - 100)

        # self.ui_manager.add_ui_element(self.settings_button)
        self.ui_manager.add_ui_element(self.sound_toggle)
        self.ui_manager.add_ui_element(self.play_button)
        self.ui_manager.add_ui_element(self.instruct_button)
        

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        self.texture.draw_sized(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2,
                                constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        arcade.draw_text("Tank Wars", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        # arcade.draw_text("Click to advance", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2-75,
        #                  arcade.color.WHITE, font_size=20, anchor_x="center")


class Button(UIImageButton):
    def __init__(self, view, game, x = constants.PLAY_X, y = constants.BUTTON_Y,
    height = constants.BUTTON_HEIGHT, width = constants.BUTTON_WIDTH, text = "",
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


class Settings_Button(UIImageButton):
    def __init__(self, game, x = constants.SETTINGS_X, y = constants.SETTINGS_Y,
    height = constants.BUTTON_HEIGHT + 50, width = constants.BUTTON_WIDTH + 50, normal_texture = None):
        super().__init__(center_x= x, center_y= y, normal_texture= normal_texture)
        self.center_x = x
        self.center_y = y
        self.window = game


    def on_click(self):
        view = SettingsView()
        view.setup()
        self.window.show_view(view)


class InstructionView(arcade.View):
    def __init__(self):
        super().__init__()
        self.ui_manager = UIManager()

    def on_show(self):
        self.setup()
    
    def on_hide_view(self):
        self.ui_manager.unregister_handlers()

    
    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        arcade.draw_text("instructions text", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2, 
                        color = arcade.color.AERO_BLUE, anchor_x= 'center')
    
    def setup(self):
        self.ui_manager.purge_ui_elements()

        self.back_texture = arcade.load_texture(constants.BACK_SPRITE)
        self.back_button = Button(MainView(), self.window, x = constants.BACK_X, y = constants.BACK_Y,
        normal_texture= self.back_texture)

        self.ui_manager.add_ui_element(self.back_button)
    
    def on_show_view(self):
        arcade.set_background_color(arcade.color.ANTIQUE_BRONZE)


class SettingsView(arcade.View):
    def __init__(self):
        super().__init__()
        self.ui_manager = UIManager()

    def on_show(self):
        self.setup()
        self.texture = arcade.load_texture(constants.CAMO)
    
    def on_hide_view(self):
        self.ui_manager.unregister_handlers()
    
    def setup(self):
        self.ui_manager.purge_ui_elements()

        self.back_texture = arcade.load_texture(constants.BACK_SPRITE)
        self.back_button = Button(MainView(), self.window, x = constants.BACK_X, y = constants.BACK_Y,
        normal_texture= self.back_texture)


        self.normal_sound_texture = arcade.load_texture(constants.TOGGLE_ON_SPRITE)
        self.pressed_sound_texture = arcade.load_texture(constants.TOGGLE_OFF_SRITE)
        self.sound_toggle = SoundToggle(normal = self.normal_sound_texture, pressed = self.pressed_sound_texture,
        game = self.window)

        self.ui_manager.add_ui_element(self.back_button)
        self.ui_manager.add_ui_element(self.sound_toggle)
    
    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        self.texture.draw_sized(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2,
                                constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        arcade.draw_text("Settings text", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2, 
                        color = arcade.color.AERO_BLUE, anchor_x= 'center')
        
    
    # def on_show_view(self):
    #     arcade.set_background_color(arcade.color.ANTIQUE_BRONZE)

class SoundToggle(UIImageButton):
    #TODO: resize and fix one click problem
    def __init__(self, normal, pressed, game):
        super().__init__(center_x=constants.SETTINGS_X, center_y= constants.SETTINGS_Y,
        normal_texture= normal)
        self.normal = normal
        self.new_normal = pressed
        self.window = game
    
    def on_click(self):
        if self.window.master_volume != 0.0:
            self.normal_texture = self.new_normal
            self.window.master_volume = 0.0
        elif self.window.master_volume != 0.5:
            self.normal_texture = self.new_normal
            self.window.master_volume = 0.5