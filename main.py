"""
This code  is used for learning purpose.
I will tru to wirte a dinosaur jumping game.
I have used the code form https://github.com/dhhruv/Chrome-Dino-Runner .
"""
# import libraries
import pygame
import sys

# initilize pygame library
pygame.init()

# initilize global variables
size = width, height = 800, 350
# initilize screen
screen = pygame.display.set_mode(size)


class Dinosaur:
    def __init__(self):
        pass


class Cactus:
    def __init__(self):
        pass


class Obstacle:
    def __init__(self):
        pass


class Background:
    def __init__(self):
        self.speed = 0.5
        pass


if __name__ == "__main__":
    # Function used to run the program
    t_pos_x, t_pos_y = 0, 250

    # Function controls the pygame screen
    def track(speed):
        # Runs track infinitly
        global t_pos_x, t_pos_y
        road = pygame.image.load("./assets/Other/Track.png")  # load track image
        rwidth = road.get_width()  # get track width
        screen.blit(road, (t_pos_x, t_pos_y))  # draw starting image
        screen.blit(road, (t_pos_x + rwidth, t_pos_y))  # draw second image after first
        if t_pos_x <= -rwidth:  # check if first image is out of the screen
            screen.blit(road, (t_pos_x + rwidth, t_pos_y))   # draw 'second' image again if true
            t_pos_x = 0  # reinitilize x cordinates to create infinite loop
        t_pos_x -= speed  # speed of the track


    while 1:
        # Keeps the screen running
        for event in pygame.event.get():
            # Closes the gui on close event
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(color='grey')
        track(0.5)
        pygame.display.flip()
