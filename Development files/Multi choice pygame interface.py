import pygame 

pygame.init() 

screen_width = 800
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))

run = True
while run == True:

    for event in pygame.event.get():
        if event.type == pygame.quit:
            run = False

pygame.quit()