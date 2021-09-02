"""
This code  is used for learning purpose.
I will tru to wirte a dinosaur jumping game.
I have used the code form https://github.com/dhhruv/Chrome-Dino-Runner for reference.
"""
# import libraries
import time
import pygame
import sys

# initilize pygame library
pygame.init()

# initilize global variables
size = width, height = 800, 350
# initilize screen
screen = pygame.display.set_mode(size)
# set title
pygame.display.set_caption("Jumping dinosaur")

# load images
WALL = pygame.image.load("./assets/DinoWallpaper.png")

# Dinosaur images
RUNNING = [pygame.image.load("./assets/Dino/DinoRun1.png"),
           pygame.image.load("./assets/Dino/DinoRun2.png")]
JUMPING = pygame.image.load("./assets/Dino/DinoJump.png")
START = pygame.image.load("./assets/Dino/DinoStart.png")
DEAD = pygame.image.load("./assets/Dino/DinoDead.png")

# Foreground images
ROAD = pygame.image.load("./assets/Other/Track.png")
CLOUD = pygame.image.load("./assets/Other/Cloud.png")
GAMEOVER = pygame.image.load("./assets/Other/GameOver.png")
RESET = pygame.image.load("./assets/Other/Reset.png")

# Cactus images
LARGE_CACTUS = [pygame.image.load("./assets/Cactus/LargeCactus1.png"),
                pygame.image.load("./assets/Cactus/LargeCactus2.png"),
                pygame.image.load("./assets/Cactus/LargeCactus3.png")]
SMALL_CACTUS = [pygame.image.load("./assets/Cactus/SmallCactus1.png"),
                pygame.image.load("./assets/Cactus/SmallCactus2.png"),
                pygame.image.load("./assets/Cactus/SmallCactus3.png")]

# Bird images
BIRD = [pygame.image.load("./assets/Bird/Bird1.png"),
        pygame.image.load("./assets/Bird/Bird2.png")]


class Dinosaur:
    def __init__(self):
        self.dino_runing = RUNNING
        self.s = time.time()
        self.x = 0

    def run(self, speed):
        screen.blit(self.dino_runing[self.x], (50, 180))
        # time used to define speed
        e = time.time()
        # loop through two images at constant speed
        if e - speed > self.s:
            self.x ^= 1
            self.s = e


class Obstacle:
    def __init__(self):
        pass


class Foreground:
    def __init__(self):
        self.road = ROAD
        self.t_pos_x = 0
        self.t_pos_y = 250

    def track(self, speed):
        # Runs track infinitly
        rwidth = self.road.get_width()  # get track width
        screen.blit(self.road, (self.t_pos_x, self.t_pos_y))  # draw starting image
        screen.blit(self.road, (self.t_pos_x + rwidth, self.t_pos_y))  # draw second image after first
        if self.t_pos_x <= -rwidth:  # check if first image is out of the screen
            screen.blit(self.road, (self.t_pos_x + rwidth, self.t_pos_y))  # draw 'second' image again if true
            self.t_pos_x = 0  # reinitilize x cordinates to create infinite loop
        self.t_pos_x -= speed  # speed of the track

    def clouds(self):
        pass


def start():
    # initlizing objects
    player = Dinosaur()
    foreground = Foreground()
    # Function controls the pygame screen
    while 1:
        # Keeps the screen running
        for event in pygame.event.get():
            # Closes the gui on close event
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(color='grey')  # background color
        foreground.track(0.5)
        player.run(0.5)
        pygame.display.flip()


if __name__ == "__main__":
    start()
