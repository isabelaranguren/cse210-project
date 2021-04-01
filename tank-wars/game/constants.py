from pathlib import Path
from random import randint

home = Path.home()
assets: Path = Path(__file__).parent / 'assets'

#Frame
SCREEN_WIDTH = 860
SCREEN_HEIGHT = 540
TITLE = "TANK WARS"
X_CONSTANT = 860
Y_CONSTANT = 540

#Sounds
TANK_FIRE = assets / 'sounds' / 'tank-fire.wav'
EXPLOSION_SOUND = assets / 'sounds' / 'Explosion+7.wav'
MAIN_SCREEN_SOUND = assets / 'sounds' / 'IntroScreen.mp3'
POWERUPS_SOUND = assets / 'sounds' / 'powerup.ogg'
POWERDOWN_SOUND = assets / 'sounds' / 'powerdown.flac'

DEFAULT_VOLUME = 0.2


#Sprites

#Ground
GROUND_SPRITE = f":resources:images/tiles/dirtRight.png"
GROUND_SCALE = 1
GROUND_Y = 32

#Tanks
TANK_Y = randint(0, 500)
TANK_SCALE = 0.85
TANK_SPEED = 2
TANK_ANGLE_SPEED = 2

#Player 1
PLAYER1_X = randint(450, 810)
PLAYER1_SPRITE = ":resources:images/topdown_tanks/tank_dark.png"
MAP = assets / 'map.tmx'

#Player 2
PLAYER2_SPRITE = ":resources:images/topdown_tanks/tank_green.png"
PLAYER2_X = randint(50, 450)

#Views
GAME_OVER = assets / 'game-over.jpg'
BACKGROUND = assets / 'background.png'
CAMO = assets / 'main-bkg.png'
WALLS = assets / '1bitpack' / 'Tilemap' / 'sample_urban2.tmx'
TILE_SCALING = 1.5
GRAVITY = 1

#Bullet
BULLET_SPRITE = assets/ 'tank-pack' / 'tank_bullet1.png'
BULLET_INITIAL_VELOCITY = (3,0)
BULLET_SCALE = 0.5
BULLET_SPEED = 5
BULLET_X_SCALE = 7
BULLET_Y_SCALE = 7

#Powers
HEALTH_POWER_UP_SPRITE = assets / 'tank-pack' / 'tanks_crateWood.png'
HEALTH_POWER_DOWN_SPRITE = assets / 'tank-pack' / 'tanks_crateRepair.png'
HEALTHBAR_WIDTH = 25
HEALTHBAR_HEIGHT = 3
HEALTHBAR_OFFSET_Y = -10
HEALTH_NUMBER_OFFSET_X = -10
HEALTH_NUMBER_OFFSET_Y = -25

#Buttons
BUTTON_Y = 175
BUTTON_WIDTH = 32
BUTTON_HEIGHT = 32

#Play Buttons
PLAY_X = 425
PLAY_SPRITE = assets / "startButton.png"
PLACEHOLDER = assets / 'bkg.png'

#instructions button
INSTRUCT_X = 100
INSTRUCTION_BKG = assets / 'instructions.png'
INSTRUCT_SPRITE = assets / "instructionsButton.png"

#Setting Buttons
SETTINGS_X = 815
SETTINGS_Y = 495
SETTINGS_SPRITE = assets / 'settings.png'
SETTINGS_WIDTH = 50
SETTINGS_HEIGHT = 50

#toggle defaluts
TOGGLE_X= SCREEN_WIDTH /3
TOGGLE_Y = SCREEN_HEIGHT /3
TOGGLE_ON_SPRITE = assets / "soundOn.png"
TOGGLE_OFF_SRITE =  assets / "soundOff.png"

#back button
BACK_SPRITE = assets / 'backButton.png'
BACK_X = 780
BACK_Y = 490

#time
FRAME_LENGTH = 0.1