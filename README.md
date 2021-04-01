# Tank Wars 

Tank Wars is a fast-moving two-player game. While moving around the map be sure
to avoid enemy fire! Watch for wood crates for a random surprise - it could be
an increase or decrease of life or something entirely different!

```
python3 -m pip install arcade
```
After you've installed the required libraries, open a terminal and browse to the 
project's root folder. Start the program by running the following command.

```
python3 tank-wars
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE 
and open the project folder. Select the main module inside the hunter folder and 
click the "run" icon.


## How to play

Goal 1: Don't get shot.
Goal 2: Shoot your opponent.

Player 1 will use the arrow keys to move their tank and Space to shoot.
Player 2 will use the A, S, D, W keys to move and Q to shoot

## Project Structure
---
The project files and folders are organized as follows:
```
root                           (project root folder)
.gihub                         (general info) 
+-- tank-wars                  (source code for game)
  +-- data                     (source files)
  +-- docs                     (general info)
  +-- game                     (specific game classes)
    +-- assets                 (game source) 
      +-- bullet.py
      +-- constants.py 
      +-- explosion.py
      +-- game_over_view.py
      +-- gameview.py
      +-- ground.py
      +-- instruction_view.py
      +-- powerups.py
      +-- score.py
      +-- tanks.py   
  +-- __init__.py              (python package file)
  +-- __main__.py              (entry point for program)
+-- LICENSE                    (License info)
+-- README.md                  (general info)

```

## Required Technologies
---
* Python 3.8.0
* Arcade 2.5.5

## Authors
---
* Reed Hunsaker | hun20010@byui.edu

* Jordan McIntyre | mci20007@byui.edu

* Juliano Nascimento | nas19008@byui.edu

* Adrianna Lund | ran08001@byui.edu

* Isabel Aranguren | lar19030@byui.edu
