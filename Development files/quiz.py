# Example file showing a basic pygame "game loop"
import pygame
import sys 

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1200, 700))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white") 

    # setting/changing icon & name of pygame window
    pygame.display.set_caption('St Augs Quiz')
    Icon = pygame.image.load('Staugs.jpeg')
    pygame.display.set_icon(Icon)


    # Load button images
    start_img = pygame.image.load('start_btn.png').convert_alpha
    exit_img = pygame.image.load('start_btn.png').convert_alpha

    # #set colour
    # colour = (5, 102, 8)

    # # creating 4 rectangles as question answer options 
    # pygame.draw.rect(screen, colour, pygame.Rect(100, 175, 400, 200),  100, 10)
    # pygame.draw.rect(screen, colour, pygame.Rect(700, 175, 400, 200),  100, 10)
    # pygame.draw.rect(screen, colour, pygame.Rect(100, 450, 400, 200),  100, 10)
    # pygame.draw.rect(screen, colour, pygame.Rect(700, 450, 400, 200),  100, 10)

    clock.tick(60)  # limits FPS to 60  

# flip() the display to put your work on screen
    pygame.display.flip()

    