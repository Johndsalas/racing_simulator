''' Creating gui for the game'''

import pygame
from sys import exit
import random as r
import operator
import ponies

# makes pygame work
pygame.init()

# making window
width, height = 900, 675
screen = pygame.display.set_mode((width, height))

# setting title
pygame.display.set_caption("Pony Racing Simulator")

# time object
clock = pygame.time.Clock()

# import and scale background serface objects
grass_surface = pygame.image.load('images/grass.jpg')
grass_surface = pygame.transform.scale(grass_surface, (width, height))

title_screen = pygame.image.load('images/menu_pony.jpg')
title_screen = pygame.transform.scale(title_screen, (width, height))

# text objects
test_font = pygame.font.Font(None, 75)
text_surace = test_font.render("Pony Racing Time!!!!", False, 'Black')

start_line_txt = pygame.font.Font(None, 30)
start_line_txt = start_line_txt.render("Start", False, 'Black')

finish_line_txt = pygame.font.Font(None, 30)
finish_line_txt = finish_line_txt.render("Finish", False, 'Black')

menu_title = pygame.font.Font(None, 90)
menu_title = menu_title.render("PONY RACING SIMULATOR!!!", False, 'white')

menu_text = pygame.font.Font(None, 75)
menu_text = menu_text.render("Press ENTER to Begin the Race!", False, 'Black')

race_again = pygame.font.Font(None, 50)
race_again = race_again.render("Press ENTER to Begin Another Race!", False, 'Black')

# start and finish line objects
start_line = pygame.Surface((10,575))
start_line.fill('Black')

finish_line = pygame.Surface((10,575))
start_line.fill('Black')

# beginning and ending x coordanent for ponies in the race
starting_x = 5
final_x = 750

# make ponies and put them in a stable
pony_stable = ponies.make_ponies(starting_x, final_x)


def menu():
    ''' blits images for menu screen '''

    screen.blit(title_screen, (0,0))
    screen.blit(menu_title, (10,20))
    screen.blit(menu_text, (20,600))


def racing():  
    ''' blits and moves images in racing screen'''

    # adds background surface
    screen.blit(grass_surface,(0,0))

    # adds start line and text
    screen.blit(start_line, (105, 75))
    screen.blit(start_line_txt, (90, 35))

    # adds finishline and text
    screen.blit(finish_line, (final_x + 95,75))
    screen.blit(finish_line_txt, (final_x + 75, 35))

    # adds title text
    screen.blit(text_surace, (200, 5))

    # adds ponies to screen
    for pony in pony_stable:

        # render text
        name_text = pygame.font.Font(None, 20)
        name_text = name_text.render(f"{pony.name}", False, 'Black')

        # blit pony image and name
        screen.blit(pony.image, (pony.x, pony.y))

        screen.blit(name_text, (pony.x,pony.y - 15))

        # move ponies 1-10 pixals toward the starting line
        movement = r.randint(1,10)

        pony.move_x(movement)
        pony.max_x()


def conclusion():
    '''displays ribbons next to ponies marking thier placing at the conclution of the race
       prompts user to press enter to see another race'''

    # adds surface
    screen.blit(grass_surface,(0,0))

    # adds start line and text
    screen.blit(start_line, (105, 75))
    screen.blit(start_line_txt, (90, 35))

    # adds finishline and text
    screen.blit(finish_line, (final_x + 95,75))
    screen.blit(finish_line_txt, (final_x + 75, 35))

    # adds text
    screen.blit(race_again, (170, 10))


    # adds ponies name and image to the screen
    for pony in pony_stable:

        # render text
        name_text = pygame.font.Font(None, 25)
        name_text = name_text.render(f"{pony.name}", False, 'Black')

        # display pony image and name
        screen.blit(pony.image, (pony.x, pony.y))
        screen.blit(name_text, (pony.x, pony.y - 15))

    # get a list of the pony objects in order of placing
    placings = sorted(pony_stable, key=operator.attrgetter('x'))

    placings.reverse()

    # set placing index to 0
    p_index = 0

    # display placing ribbon next to each pony according to thier placing
    for pony in placings:

        # create list of placing ribbon images in order of placing
        placing_images = ["a_1.jpg","a_2.jpg","a_3.jpg","a_4.jpg","a_5.jpg","a_6.jpg"]

        # display display ribbon image by index number next to the pony in the itteration
        placing= pygame.image.load(f"images/{placing_images[p_index]}")
        placing = pygame.transform.scale(placing, (100, 75))

        screen.blit(placing, (pony.x - 100, pony.y))

        # augment p_index by 1 if it is grater than the number of ponies reset it to 1
        p_index += 1

        if p_index > len(placing_images):

            p_index = 1


def main():
    ''' funtion for game loop'''

    # tracks stage the game is at begin game at menu
    game_at = "menu"


    # game loop
    while True:

        for event in pygame.event.get():

            # close game
            if event.type == pygame.QUIT:
  
                pygame.quit() # exits pygame
                exit() # exits code

            # begin new race by pressing enter
            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:

                    if game_at == "conclusion":

                        for pony in pony_stable:

                            pony.set_x(starting_x)
                   
                    game_at = "racing"

        # begin conclution when a poney has finished a race
        for pony in pony_stable:

            if pony.x == final_x:

                game_at = "conclusion"

        # check for game stage and run corresoponding images
        if game_at == "menu":

            menu()

        elif game_at == "racing":

            racing()

        elif game_at == "conclusion":

            conclusion()

        # updates display with new info
        pygame.display.update()

        # set max framerate to 30
        clock.tick(30)


if __name__ == '__main__':

    main()