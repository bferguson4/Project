from enum import Enum
import numpy as np
import random

# creates the directions for moving up, down, left, and right 
class Direction(Enum):
    Up = 1
    Right = 2
    Down = 3
    Left = 4


# picks a random number to represent the movement of the ship in any direction
def rand_direction():
    direction = random.randint(1, 4)
    
    if (direction == 1):
        return Direction.Up
    elif (direction == 2):
        return Direction.Right
    elif (direction == 3):
        return Direction.Down
    else:
        return Direction.Left
    
class Ship():
       
    def __init__(self, size):
        self.size = size
        self.body = [0] * size
        self.dir = rand_direction()
        self.unhit = size
        self.hit = 0
        self.isSunk = False
    
    # returns the size of the ship 
    def size(self):
        return self.size
    
    # If the ship is hit updates the ship variables and checks if the ship is still standing
    def hit(self):
        self.unhit -= 1
        self.hit += 1
        if (self.unhit == 0):
            self.isSunk = True
        
        return self.isSunk
    
    # returns how many ships are left on the board
    def ships_left():
        return Ship.unhit
    
            

    