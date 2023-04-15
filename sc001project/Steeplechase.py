"""
File: Steeplechase.py
Name: chiwen
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
   for i in range(11):
       if front_is_clear():
           move()
       else:
           jump()


def jump():
    """
     pre-condition: karel is on the left, facing east
     post-condition:karel is on the right
    """
    up()
    cross()
    down()


def up():
    """
    pre-condition:karel is on the right
    post-condition:karel is at the upper left, facing north
    """
    turn_left()
    # karel is facing north, wall is on the right
    while not right_is_clear():
        move()


def turn_right():
    for i in range(3):
        turn_left()


def cross():
    """
    pre-condition:karel is at the upper left, facing north
    post-condition:kare is at the upper right, facing south
    """
    turn_right()
    move()
    turn_right()


def down():
    while front_is_clear():
        move()
    turn_left()

# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
