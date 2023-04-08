''' Creating gui for the game'''

import pygame
import ponies
from sys import exit

# makes pygame work
pygame.init()

# making window
width, height = 900, 675
screen = pygame.display.set_mode((width, height))

# setting title
pygame.display.set_caption("Racing Simmulator 9000")

# time object
clock = pygame.time.Clock()

# import and scale background serface object
grass_surface = pygame.image.load('images/grass.jpg')
grass_surface = pygame.transform.scale(grass_surface, (width, height))

# text objects
test_font = pygame.font.Font(None, 75)
text_surace = test_font.render("Pony Racing Time!!!!", False, 'Black')

start_line_txt = pygame.font.Font(None, 30)
start_line_txt = start_line_txt.render("Start", False, 'Black')

finish_line_txt = pygame.font.Font(None, 30)
finish_line_txt = finish_line_txt.render("Finish", False, 'Black')

# start line object
start_line = pygame.Surface((10,575))
start_line.fill('Black')

# finish line x coordanent
final_x = 750

# finish line object
finish_line = pygame.Surface((10,575))
start_line.fill('Black')

# make ponies and put them in a stable
pony_stable = ponies.make_ponies(final_x)

def main():
    ''' funtion for main game loop'''

    while True:
        
        for event in pygame.event.get():

            # close game
            if event.type == pygame.QUIT:
  
                pygame.quit() # exits pygame
                exit() # exits code

        # adds surface
        screen.blit(grass_surface,(0,0))

        # adds start line and text
        screen.blit(start_line, (105, 75))
        screen.blit(start_line_txt, (90, 50))

        # adds finishline and text
        screen.blit(finish_line, (final_x + 95,75))
        screen.blit(finish_line_txt, (final_x + 80, 50))

        # adds text
        screen.blit(text_surace, (200, 5))

        # adds ponies to screen
        for pony in pony_stable:

            screen.blit(pony.image, (pony.x, pony.y))

            # moove ponies toward starting line
            pony.move_x()
            pony.max_x()

        # updates display with new info
        pygame.display.update()

        # set max framerate to 60
        clock.tick(10)

if __name__ == '__main__':

    main()