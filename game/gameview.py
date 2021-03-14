import arcade
import game.constants as constants
from game.tanks import Run
from game.ground import Ground
from game.bullet import Bullet
from typing import Optional


class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        
        self.window.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.SMOKY_BLACK)
        self.physics_engine = None

        self.setup()
        self.up: bool = False
        self.down: bool = False
        self.right: bool = False
        self.left: bool = False

    
    def setup(self):
        # self.physics_engine = arcade.PymunkPhysicsEngine(damping = 1.0)
        self.tanks = Run()
        self.ground = Ground()
        self.bullet = Bullet()
        # self.physics_engine.add_sprite(self.bullet)
        self.bullet.shoot_bullet(constants.PLAYER1_X,constants.TANK_Y)

        self.physics_engine = arcade.PhysicsEngineSimple(self.tanks.player1, self.ground.ground_sprite_list)
    
    def on_draw(self):
        arcade.start_render()
        self.tanks.sprite_list.draw()
        self.ground.ground_sprite_list.draw()
        self.bullet.bullet_sprite_list.draw()

    def on_update(self, delta_time: float):
        
        self.physics_engine.update()

        
        if self.bullet.bullet.collides_with_sprite(self.tanks.player2) or self.bullet.bullet.collides_with_list(self.ground.ground_sprite_list):
            self.bullet.bullet.kill()
        
        self.tanks.player1.update()
        self.tanks.player2.update()
        self.bullet.bullet_sprite_list.update()
        self.bullet.bullet_sprite_list.update_animation()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        # Forward/back
        if key == arcade.key.DOWN:
            self.tanks.player1.speed = constants.TANK_SPEED
        elif key == arcade.key.UP:
            self.tanks.player1.speed = -constants.TANK_SPEED

        elif key == arcade.key.S:
            self.tanks.player2.speed = constants.TANK_SPEED
        elif key == arcade.key.W:
            self.tanks.player2.speed = -constants.TANK_SPEED

        # Rotate left/right
        elif key == arcade.key.LEFT:
            self.tanks.player1.change_angle = constants.TANK_ANGLE_SPEED
        elif key == arcade.key.RIGHT:
            self.tanks.player1.change_angle = -constants.TANK_ANGLE_SPEED
        
        elif key == arcade.key.A:
            self.tanks.player2.change_angle = constants.TANK_ANGLE_SPEED
        elif key == arcade.key.D:
            self.tanks.player2.change_angle = -constants.TANK_ANGLE_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.tanks.player1.speed = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.tanks.player1.change_angle = 0
        
        elif key == arcade.key.W or key == arcade.key.S:
            self.tanks.player2.speed = 0
        elif key == arcade.key.A or key == arcade.key.D:
            self.tanks.player2.change_angle = 0