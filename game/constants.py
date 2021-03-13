import os
cwd = os.getcwd()
#frame
X_CONSTANT = 800
Y_CONSTANT = 600
SCREEN_TITLE = "TANK WARS"

#sprites

#ground
GROUND_SPRITE = f":resources:images/tiles/dirtRight.png"
GROUND_SCALE = 1
GROUND_Y = 32

#Tanks
TANK_Y = 125
TANK_SCALE = 0.85
#Player 1
PLAYER1_X = 150

PLAYER1_SPRITE = f"{cwd}/assets/tank-pack/tanks_tankGrey1.png"

#player 2
PLAYER2_SPRITE = f"{cwd}/assets/tank-pack/tanks_tankGreen1.png"

PLAYER2_X = 600 

#bullet

BULLET_SPRITE = f"{cwd}assets/tank-pack/tank_bulletFly4.png"


#time

FRAME_LENGTH = 0.1