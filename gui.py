''' Creating gui for the game'''

import pygame
from sys import exit

# makes pygame work
pygame.init()

# making window
width, height = 900, 500
screen = pygame.display.set_mode((width, height))

# setting title
pygame.display.set_caption("Racing Simmulator 9000")

# time object
clock = pygame.time.Clock()

# import and scale background serface object
grass_surface = pygame.image.load('grass.jpg')
grass_surface = pygame.transform.scale(grass_surface, (width, height))


def main():
    ''' funtion for main game loop'''

   
    while True:

        # checks for iinout
        for event in pygame.event.get():

            # close game
            if event.type == pygame.QUIT:
                pygame.quit() # exits pygame
                exit() # exits code

        # adds surface
        screen.blit(grass_surface,(0,0))



        # updates display with new info
        pygame.display.update()

        # set max framerate to 60
        clock.tick(60)

if __name__ == '__main__':

    main()