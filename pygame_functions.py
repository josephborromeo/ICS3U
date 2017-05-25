import pygame, random, time, sys
from pygame.locals import *

#Initializes the Clock
clock = pygame.time.Clock()

# Sets the programs framerate
FPS = 60

# Initializes the fonts
pygame.font.init()

# Set text font
myfont = pygame.font.SysFont("Comic Sans MS", 30)

# Sets the screen Width and Height
SCREEN_WIDTH, SCREEN_HEIGHT = 350, 600

# Initialize Variables
x, y  = 50, (SCREEN_HEIGHT - 77)

# Opens a window with size 640x480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create variable for background color
bg_color = (80, 128, 255)

# Fills the screen with color defined above
screen.fill(bg_color)

# Sets the window name
pygame.display.set_caption("Adventure Prison Escape")

game_title = myfont.render("Adventure Prison Escape", 1, (0, 0, 0))
screen.blit(game_title, (50, 50))

# Draws all changes to the window
pygame.display.update()

def show_screen():
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
