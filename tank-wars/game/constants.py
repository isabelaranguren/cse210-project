from pathlib import Path

home = Path.home()
assets: Path = Path(__file__).parent / 'assets'

#frame
SCREEN_WIDTH = 860
SCREEN_HEIGHT = 540
TITLE = "TANK WARS"

X_CONSTANT = 860
Y_CONSTANT = 540

#sounds
TANK_FIRE = assets / 'sounds' / 'tank-fire.wav'

#sprites
#ground
GROUND_SPRITE = f":resources:images/tiles/dirtRight.png"
GROUND_SCALE = 1
GROUND_Y = 32


#Tanks
TANK_Y = 125
TANK_SCALE = 0.85
TANK_SPEED = 5
TANK_ANGLE_SPEED = 5
#Player 1
PLAYER1_X = 150
PLAYER1_SPRITE = ":resources:images/topdown_tanks/tank_blue.png"
# PLAYER1_SPRITE = assets / 'tank-pack' / 'tanks_tankGrey1.png'
MAP = assets / 'map.tmx'
#player 2
# PLAYER2_SPRITE = assets / 'tank-pack' / 'tanks_tankGreen1.png'
PLAYER2_SPRITE = ":resources:images/topdown_tanks/tank_red.png"
PLAYER2_X = 600

GAME_OVER = assets / 'game-over.jpg'
BACKGROUND = assets / 'background.png'
CAMO = assets / 'camo.jpg'

WALLS = assets / '1bitpack' / 'Tilemap' / 'sample_urban2.tmx'
TILE_SCALING = 1.5
GRAVITY = 1

#bullet
BULLET_SPRITE = assets/ 'tank-pack' / 'tank_bullet1.png'
BULLET_INITIAL_VELOCITY = (3,0)
BULLET_SCALE = 0.5
BULLET_SPEED = 5

#explosion
EXPLOSION_TEXTURE_LIST = []
for i in range(1, 13):
    ex_tex = assets / 'tank-pack' / f'tank_explosion{i}.png'
    EXPLOSION_TEXTURE_LIST.append(ex_tex)
EXPLOSION_4 = assets / 'tank-pack' / 'tank_explosion4.png'

#time
FRAME_LENGTH = 0.1