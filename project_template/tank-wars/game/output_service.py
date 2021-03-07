import arcade
from game import constants

class Output_service(arcade.Window):
    def __init__(self):
        super().__init__(constants.X_CONSTANT, constants.Y_CONSTANT, constants.SCREEN_TITLE)

        self.player_list = None
        self.wall_list = None
        self.cactus_list = None
        self.enemy_list = None
        self.sprite_list = None


        self.player_sprite = None

        arcade.set_background_color(arcade.color.SMOKY_BLACK)

    def setup(self,cast, bullet):
        """
        Set up the game/ restart
        """
        self.bullet = bullet
        if type(cast) != list:
            self.sprite_list = arcade.SpriteList()
            self.sprite_list.append(cast)
        else:
            for x in cast:
                self.sprite_list.append(x)

        
        # #Sprite lists
        # self.player_list = arcade.SpriteList()
        # self.enemy_list = arcade.SpriteList()
        # self.wall_list = arcade.SpriteList(use_spatial_hash= True)
        # self.cactus_list = arcade.SpriteList()

        # #player sprite
        # self.player_sprite = arcade.Sprite("assets/Tankbg.png", scale = 0.65)
        # self.player_sprite.center_x = 150
        # self.player_sprite.center_y = 125
        # self.player_list.append(self.player_sprite)

        # #enemy sprite
        # self.enemy_sprite = arcade.Sprite("assets/Tankrbg.png", scale = 0.65)
        # self.enemy_sprite.center_x = 650
        # self.enemy_sprite.center_y = 125
        # self.enemy_list.append(self.enemy_sprite)



        # #cactus sprite
        # self.cactus_sprite = arcade.Sprite(":resources:images/tiles/cactus.png")
        # self.cactus_sprite.center_x = 385
        # self.cactus_sprite.center_y = 150
        # self.cactus_list.append(self.cactus_sprite)


        #bullet sprites
        """
        select type of bullet and set sprite accordingly
        get xy of end of barrel to shoot from
        determine velocity and trajectory
        """
        self.bullet_sprite = arcade.Sprite("assets/tank-pack/tank_bulletFly6.png")
        # self.bullet_sprite.center_x = #TODO
        # self.bullet_sprite.center_y = #TODO
        #TODO add to bullet sprite list - create list

        #ground sprite
        # for x in range(0, 1250, 64):
        #     wall = arcade.Sprite(":resources:images/tiles/dirtRight.png")
        #     wall.center_x = x
        #     wall.center_y = 32
        #     self.wall_list.append(wall)

    def shoot(self):
        """shoot bullet"""


    def on_draw(self):
        """ Render the Screen """
        arcade.start_render()
        self.sprite_list.draw()

    def on_update(self, delta_time: float):
        """Update the positions and statuses of all game objects
        If paused, do nothing
        Arguments:
            delta_time {float} -- Time since the last update
        """

        # If paused, don't update anything
        # if self.paused:
        #     return
        # Did you hit anything? If so, end the game
        if self.bullet.collides_with_list(self.sprite_list):
            # arcade.close_window()
            # self.explosion = arcade.Sprite(r"cse210-project\project_template\tank-wars\assets\tank-pack\tank_explosion2.png",1)
            # self.explosion.center_x = self.bullet.right
            # self.explosion.center_y = self.bullet.center_y
            # self.explosions.append(self.explosion)
            # self.explosions.update()
            # self.explosions.update_animation()
            self.bullet.kill()
        
        self.sprite_list.update()
        self.sprite_list.update_animation()
