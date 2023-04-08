''' contains Pony class and function make_ponies that makes a list of 6 ponies'''

import pygame
import random as r


class Pony:
    ''' creates pony objects with name, image, x coordanent, and y coordanent and final x coordanent
        poney objects can move toward thier final x coordanent and can reset thier x coordanent if they go past it
    '''

    # All ponies begin with a unique name and variable starting speed
    def __init__(self, name, image,  x, y, final_x):

        self.name = name
        self.image = image
        self.x = x
        self.y = y
        self.final_x = final_x


    # moves ponies toward finish line
    def move_x(self):

        self.x += r.randint(1,31)


    # stops ponies at finish line
    def max_x(self):

        if self.x > self.final_x:

            self.x = self.final_x


def make_ponies(final_x):
    ''' returns a list of poney objects'''

    # pony demintions
    width = 100
    height = 75

    # starting line
    start = 5

    # scaling pony images
    p1 = pygame.image.load('images/p1.jpg')
    p1 = pygame.transform.scale(p1, (width, height))

    p2 = pygame.image.load('images/p2.jpg')
    p2 = pygame.transform.scale(p2, (width, height))

    p3 = pygame.image.load('images/p3.jpg')
    p3 = pygame.transform.scale(p3, (width, height))

    p4 = pygame.image.load('images/p4.jpg')
    p4 = pygame.transform.scale(p4, (width, height))

    p5 = pygame.image.load('images/p5.jpg')
    p5 = pygame.transform.scale(p5, (width, height))

    p6 = pygame.image.load('images/p6.jpg')
    p6 = pygame.transform.scale(p6, (width, height))

    # making ponies in variables
    a = Pony("Shamrock", p1, start, 75, final_x)

    b = Pony("Constantine", p2, start, 175, final_x)

    c = Pony("StarScream", p3, start, 275, final_x)

    d = Pony("Maxi", p4, start, 375, final_x)

    e = Pony("Hoggle", p5, start, 475, final_x)

    f = Pony("Trogdor", p6, start, 575, final_x)

    # stableling ponies inside a list
    return [a, b, c, d, e, f]