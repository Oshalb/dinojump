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
size = width, height = 1000, 600
# black = 0, 0, 0
# initilize screen
screen = pygame.display.set_mode(size)


def main():
    # Function controls the pygame screen
    while 1:
        # Keeps the screen running
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(color='white')
        pygame.display.flip()


if __name__ == "__main__":
    # Function used to run the program
    main()  # call the main function
