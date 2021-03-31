import arcade
from time import sleep
from game.score import Score
import game.constants as constants
from game.tanks import Run
from game.ground import Ground
from game.bullet import Bullet
from game.powerups import SpawnRandom
from game.explosion import Explosion
from game.game_over_view import GameOverView
from typing import Optional
import math
import time


class GameView(arcade.View):
    """ Game view for Tank Wars. The responsibility of 
    this class of objects is to control the sequence of play
    Stereotype:
        Coordinator, Structurer, Service Provider
    Attributes:
        _score (Score): initalizes the score class
        texture (arcade.load_texture): load background texture
        game_ending (Boolean): triggers final game actions
        name (String): name of losing player
        physicis_engine (None): declares physics engine variable
        physics_engine2 (None): declares physics engine 2 variable
        physics_engine3 (None): declares physics engine 2 variable
        physics_engine4 (None): declares physics engine 2 variable
        bullet_list (None): declares bullet list variable
        explosion_list (None): declares explosion list variable
        explosion_texture_list (List): declares texture list used for explosion
    Contributors:
        Reed Hunsaker
        Adrianna Lund
        Isabel Aranguren
        Jordan McIntyre
    """

    def __init__(self):
        """ Declares variables for the GameView class
        Contributors:
            Reed Hunsaker
            Adrianna Lund
            Isabel Aranguren
            Jordan McIntyre
        """
        super().__init__()

        self._score = Score()
        self.texture = arcade.load_texture(constants.BACKGROUND)
        self.game_ending = False
        self.name = ""

        # physics engines
        self.physics_engine = None
        self.physics_engine2 = None
        self.physics_engine3 = None
        self.physics_engine4 = None

        # sprite lists
        self.bullet_list = None
        self.explosions_list = None
        self.explosion_texture_list = []

        # sounds
        self.powerup_sound = arcade.load_sound(constants.POWERUPS_SOUND)
        self.powerdown_sound = arcade.load_sound(constants.POWERDOWN_SOUND)
        self.tank_explode = arcade.load_sound(constants.EXPLOSION_SOUND)
        
        # explosion details
        self.columns = 16
        self.count = 8
        self.sprite_width = 256
        self.sprite_height = 256
        self.file_name = ":resources:images/spritesheets/explosion.png"
        self.explosion_texture_list = arcade.load_spritesheet(self.file_name, self.sprite_width, self.sprite_height,
                                                              self.columns, self.count)

    def setup(self):
        """ Set up the game and initializes variables.
        Contributors:
            Reed Hunsaker
            Adrianna Lund
            Isabel Aranguren
            Jordan McIntyre
        """
        self.tanks = Run()
        self.ground = Ground()
        self.bullet = Bullet()
        self.power = SpawnRandom()
        self.explosions_list = arcade.SpriteList()
        self.physics_engine = arcade.PhysicsEngineSimple(self.tanks.player1, self.ground.ground_sprite_list)
        self.physics_engine2 = arcade.PhysicsEngineSimple(self.tanks.player2, self.ground.ground_sprite_list)
        self.physics_engine3 = arcade.PhysicsEngineSimple(self.tanks.player1, self.tanks.sprite_list)
    
    def on_draw(self):
        """ Draws the game screen.
        Contributors:
            Reed Hunsaker
            Adrianna Lund
            Jordan McIntyre
            Isabel Aranguren
        """
        arcade.start_render()

        self.wrap()
        self.texture.draw_sized(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2,
                                constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        self.tanks.sprite_list.draw()

        for tank in self.tanks.sprite_list:
            tank.draw_life_bar()
            tank.draw_life_number()

        self.ground.ground_sprite_list.draw()
        self.power.sprite_list.draw()

        if self.bullet.bullet_sprite_list is not None:
            self.bullet.bullet_sprite_list.draw()
        if self.explosions_list is not None:
            self.explosions_list.draw()

    def on_update(self, delta_time: float):
        """ Updates the game screen.
        Contributors:
            Reed Hunsaker
            Adrianna Lund
            Isabel Aranguren
            Jordan McIntyre
        """
        # if game is ending - update the last explosion, then go to the game over view
        if self.game_ending:
            self.explosions_list.update()
            if not self.explosions_list:
                self.switch_game_over_view(self.name)
            return

        self.physics_engine.update()
        self.physics_engine2.update()
        self.physics_engine3.update()
        self.explosions_list.update()

        # handle bullet collisions
        bullets = len(self.bullet.bullet_sprite_list)

        if bullets > 0:
            for bullet in self.bullet.bullet_sprite_list:
                hit_list_wall = arcade.check_for_collision_with_list(bullet, self.ground.ground_sprite_list)
                hit_list_tank = arcade.check_for_collision_with_list(bullet, self.tanks.sprite_list)
                self.bullet_shooting_update(bullet, bullets, hit_list_tank, hit_list_wall)

        # powerups
        powers = len(self.power.sprite_list)

        if powers > 0:
            for power in self.power.sprite_list:
                hit_list_wall = arcade.check_for_collision_with_list(power, self.ground.ground_sprite_list)
                hit_list_tank = arcade.check_for_collision_with_list(power, self.tanks.sprite_list)
                hit_list_bullet = arcade.check_for_collision_with_list(power, self.bullet.bullet_sprite_list)

                if len(hit_list_wall) > 0:
                    power.kill()
                    powers -= 1
                    self.power = SpawnRandom()

                # Paired with checker above in bullet collision checks. should destroy/block bullet
                if len(hit_list_bullet) > 0:
                    if self.power.sprite_list[-1].get_value() == 2:
                        for angle in range(0, 360, 60):
                            self.bullet.shoot_bullet(self.power.sprite_list[-1]._get_center_x(),
                                                     self.power.sprite_list[-1]._get_center_y(), angle)

                    power.kill()
                    powers -= 1
                    self.power = SpawnRandom()

                for tank in hit_list_tank:
                    if self.power.sprite_list[-1].get_value() == 0:
                        tank.set_life(-25)
                        arcade.play_sound(self.powerdown_sound, .8)
                    elif self.power.sprite_list[-1].get_value() == 1:
                        tank.set_life(50)
                        arcade.play_sound(self.powerup_sound)
                        # this next if statement is still experimental. it needs delays between shots
                    elif self.power.sprite_list[-1].get_value() == 2:
                        # This stops the bullets from spawning if there are more than 30 on the map
                        for angle in range(0, 360, 60):
                            bullets += 1
                            self.bullet.shoot_bullet(tank._get_center_x(), tank._get_center_y(), (tank.angle + angle))

                    power.kill()
                    powers -= 1
                    self.power = SpawnRandom()         

    def bullet_shooting_update(self, bullet, bullets, hit_list_tank, hit_list_wall):
        '''
        TODO: WRITE COMMENT
        '''
        if len(hit_list_wall) > 0:
            self.bullet.bullet_bounce(bullet, bullet.angle)

        if len(hit_list_tank) > 0:
            for tank in self.tanks.sprite_list:
                life = tank.get_life()
                explosion = Explosion(self.explosion_texture_list)

            # set explosion center to location of first hit in list
            explosion.center_x = hit_list_tank[0].center_x
            explosion.center_y = hit_list_tank[0].center_y

            # update explosion (sets first image)
            explosion.update()
            self.explosions_list.append(explosion)

        # if bullet leaves screen, kill it
        elif bullet.bottom > constants.SCREEN_HEIGHT or bullet.top < 0 or bullet.right < 0 or bullet.left > constants.SCREEN_WIDTH:
            bullet.kill()
            bullets -= 1

        # play sound and kill bullet from hit lists
        for tank in hit_list_tank:
            tank.set_life(-25)
            arcade.play_sound(self.tank_explode, .5)
            bullet.kill()
            bullets -= 1
        
        # check tank health & set final explosion
        for tank in self.tanks.sprite_list:
            alive = tank.is_alive()
            if alive == False:
                self.game_ending = True
                self.count = 50
                self.explosion_texture_list = arcade.load_spritesheet(self.file_name, self.sprite_width, self.sprite_height, self.columns, self.count)
                explosion = Explosion(self.explosion_texture_list)

                # set explosion center to location of first hit in list
                explosion.center_x = tank.center_x
                explosion.center_y = tank.center_y

                # update explosion (sets first image)
                explosion.update()
                self.explosions_list.append(explosion)
                self.name = tank.name
                tank.kill()  

    def wrap(self):
        """Keeps players on screen and kills bullets off screen and updates sprite movement. 
        Contributors:
            Adrianna Lund
            Jordan McIntyre
        """
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

        # Update animations/sprites
        self.tanks.player1.update()
        self.tanks.player2.update()
        if self.bullet.bullet_sprite_list is not None:
            self.bullet.bullet_sprite_list.update()
            self.bullet.bullet_sprite_list.update_animation()
        if self.explosions_list is not None:
            self.explosions_list.update()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. 
        Contributors:
            Adrianna Lund
            Reed Hunsaker
        """
        # Forward/back - PLAYER 1
        if key == arcade.key.DOWN:
            self.tanks.player1.speed = constants.TANK_SPEED
        elif key == arcade.key.UP:
            self.tanks.player1.speed = -constants.TANK_SPEED
        elif key == arcade.key.SPACE:
            self.bullet.shoot_bullet(self.tanks.player1._get_center_x(), self.tanks.player1._get_center_y(),
                                     self.tanks.player1.angle)

        # Forward/back - PLAYER 2
        elif key == arcade.key.S:
            self.tanks.player2.speed = constants.TANK_SPEED
        elif key == arcade.key.W:
            self.tanks.player2.speed = -constants.TANK_SPEED
        elif key == arcade.key.Q:
            self.bullet.shoot_bullet(self.tanks.player2._get_center_x(), self.tanks.player2._get_center_y(),
                                     self.tanks.player2.angle)

        # Rotate left/right - PLAYER 1
        elif key == arcade.key.LEFT:
            self.tanks.player1.change_angle = constants.TANK_ANGLE_SPEED
        elif key == arcade.key.RIGHT:
            self.tanks.player1.change_angle = -constants.TANK_ANGLE_SPEED

        # Rotate left/right - PLAYER 2
        elif key == arcade.key.A:
            self.tanks.player2.change_angle = constants.TANK_ANGLE_SPEED
        elif key == arcade.key.D:
            self.tanks.player2.change_angle = -constants.TANK_ANGLE_SPEED

        # Quit key
        elif key == arcade.key.ESCAPE:
            quit()

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. 
        Contributors:
            Adrianna Lund
            Reed Hunsaker
        """
        # Resets speed/angle on key release - PLAYER 1
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.tanks.player1.speed = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.tanks.player1.change_angle = 0

        # Resets speed/angle on key release - PLAYER 2
        elif key == arcade.key.W or key == arcade.key.S:
            self.tanks.player2.speed = 0
        elif key == arcade.key.A or key == arcade.key.D:
            self.tanks.player2.change_angle = 0

    def switch_game_over_view(self, loser):
        """ Call the game over screen.
        Contributors:
            Reed Hunsaker
        """
        game_over = GameOverView(loser)
        self.window.show_view(game_over)
