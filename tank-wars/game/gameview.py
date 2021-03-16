import arcade
from game.score import Score
import game.constants as constants
from game.tanks import Run
from game.ground import Ground
from game.bullet import Bullet
from game.explosion import Explosion
from typing import Optional
import math

class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        
        self._score = Score()
        self.texture = arcade.load_texture(constants.BACKGROUND)
        
        self.window.set_mouse_visible(False)
        self.physics_engine = None
        self.physics_engine2 = None
        self.bullet_list = None
        self.explosion_list = None

        self.setup()

    
    def setup(self):
        self.tanks = Run()
        self.ground = Ground()
        self.bullet = Bullet()
        self.explosion_list = arcade.SpriteList()
        self.physics_engine = arcade.PhysicsEngineSimple(self.tanks.player1, self.ground.ground_sprite_list)
        self.physics_engine2 = arcade.PhysicsEngineSimple(self.tanks.player2, self.ground.ground_sprite_list)
    
    def on_draw(self):
        arcade.start_render()
        self.texture.draw_sized(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2,
                                constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        self.tanks.sprite_list.draw()
        self.ground.ground_sprite_list.draw()

        if self.bullet.bullet_sprite_list is not None:
            self.bullet.bullet_sprite_list.draw()
        if self.explosion_list is not None:
            self.explosion_list.draw()

    def on_update(self, delta_time: float):
        
        self.physics_engine.update()
        self.physics_engine2.update()
    

        try:
            if self.bullet.bullet.collides_with_list(self.ground.ground_sprite_list):
                # explosion = Explosion()
                # explosion.center_x = self.bullet.bullet.center_X
                # explosion.center_y = self.bullet.bullet.center_y
                # # explosion.update()
                # self.explosion_list.append(explosion)
                self.bullet.bullet.kill()
            elif self.bullet.bullet.collides_with_list(self.tanks.sprite_list):
                self.bullet.bullet.kill()
        except AttributeError:
            pass
        
        # Check player1 for out-of-bounds
        if self.tanks.player1.left < 0:
            self.tanks.player1.left = 0
        elif self.tanks.player1.right > constants.SCREEN_WIDTH - 1:
            self.tanks.player1.right = constants.SCREEN_WIDTH - 1

        if self.tanks.player1.bottom < 0:
            self.tanks.player1.bottom = 0
        elif self.tanks.player1.top > constants.SCREEN_HEIGHT - 1:
            self.tanks.player1.top = constants.SCREEN_HEIGHT - 1

        # Check player2 for out of bounds    
        if self.tanks.player2.left < 0:
            self.tanks.player2.left = 0
        elif self.tanks.player2.right > constants.SCREEN_WIDTH - 1:
            self.tanks.player2.right = constants.SCREEN_WIDTH - 1

        if self.tanks.player2.bottom < 0:
            self.tanks.player2.bottom = 0
        elif self.tanks.player2.top > constants.SCREEN_HEIGHT - 1:
            self.tanks.player2.top = constants.SCREEN_HEIGHT - 1

        self.tanks.player1.update()
        self.tanks.player2.update()
        if self.bullet.bullet_sprite_list is not None:
            self.bullet.bullet_sprite_list.update()
            self.bullet.bullet_sprite_list.update_animation()
        if self.explosion_list is not None:
            self.explosion_list.update()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        # Forward/back
        if key == arcade.key.DOWN:
            self.tanks.player1.speed = constants.TANK_SPEED
        elif key == arcade.key.UP:
            self.tanks.player1.speed = -constants.TANK_SPEED
        elif key == arcade.key.SPACE:
            self.bullet.shoot_bullet(self.tanks.player1._get_center_x(), self.tanks.player1._get_center_y(), self.tanks.player1.angle)


        elif key == arcade.key.S:
            self.tanks.player2.speed = constants.TANK_SPEED
        elif key == arcade.key.W:
            self.tanks.player2.speed = -constants.TANK_SPEED
        elif key == arcade.key.Q:
            self.bullet.shoot_bullet(self.tanks.player2._get_center_x(), self.tanks.player2._get_center_y(), self.tanks.player2.angle)

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
    
        