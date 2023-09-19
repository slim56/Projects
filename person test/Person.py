#####################################################################
# author:  udell worley jr.    
# date: 3/13/23        
# description: uses a class to create 
#####################################################################
import math
# global Constants to restrict the maximum x and y values that a person object
# can have.
MAX_X = 800
MAX_Y = 600

# A class representing a person. A person can be initialized with a
# name, as well as x and y coordinates. However, there are default
# values for all those (i.e. player 1, 0 and 0 respectively). A person
# also has a size which is set to 1 by default. A person can go left, 
# go right, go up and go down. A person also has a string function 
# that prints out their name location, and size. A person also has a 
# function that calculates the euclidean distance from another person 
# object.
class Person:
    def __init__(self, name="player 1", x=0, y=0):
        self.name = name
        self.x = x
        self.y = y
        self.size = 1
        
    # getter for name 
    @property
    def name(self):
        return self._name
    
    # setter for name
    @name.setter
    def name(self, value):
        if len(value) >= 2:
            self._name = value
        else:
            self._name = "player 1"

    # getter for x 
    @property
    def x(self):
        return self._x
    
    # setter for x
    @x.setter
    def x(self, value):
        if value > MAX_X:
            self._x = MAX_X
        elif value < 0:
            self._x = 0
        else:
            self._x = value

    # getter for y
    @property
    def y(self):
        return self._y
    
    # setter for y
    @y.setter
    def y(self, value):
        if value > MAX_Y:
            self._y = MAX_Y
        elif value < 0:
            self._y = 0
        else:
            self._y = value

    # getter for size
    @property
    def size(self):
        return self._size

    # setter for size
    @size.setter
    def size(self, value):
        if value >= 1:
            self._size = value
        else:
            self._size = 1

    def goLeft(self, value=1):
        self.x -= value

    def goRight(self, value=1):
        self.x += value

    def goUp(self, value=1):
        self.y -= value

    def goDown(self, value=1):
        self.y += value

    def getDistance(self, other):
        dist = math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)
        return dist
    
    def __str__(self):
        return f"Person({self.name}):\tsize = {self.size},\tx = {self.x},\ty = {self.y}"
    