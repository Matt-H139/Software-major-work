# Example file showing a basic pygame "game loop"
import pygame

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


    clock.tick(60)  # limits FPS to 60

    #set colour
    colour = (255, 0, 0)

    # creating 4 buttons as question answer options 
    pygame.draw.rect(screen, colour, pygame.Rect(500, 300, 200, 75),  3, 10)



# flip() the display to put your work on screen
    pygame.display.flip()

pygame.quit()