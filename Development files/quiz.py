# Example file showing a basic pygame "game loop"
import pygame
import sys 

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1200, 700))
clock = pygame.time.Clock()
running = True


  # setting/changing icon & name of pygame window
pygame.display.set_caption('St Augs Quiz')
Icon = pygame.image.load('Staugs.jpeg')
pygame.display.set_icon(Icon)


    # Load button images
start_img = pygame.image.load('start_btn.png').convert_alpha
exit_img = pygame.image.load('exit_btn.png').convert_alpha

    # button class 
class button(): 
        def __init__(self, x, y, image):
            self.image = image
            self.rect = self.image.get_rect() 
            self.rect.topleft = (x, y)

        
        def draw(self):
            #draw button on screen
            screen.blit(self.image, (self.rect.x, self.rect.y))

    #create button instances 
start_button = button(100, 200, start_img)  
exit_button = button(450, 200, exit_img) 

#game loop
run = True
while run:

    screen.fill((202, 228, 241)) 
    
    start_button.draw()
    exit_button.draw()
    
    #event handler
    for event in pygame.event.get():
         #quit game
         if event.type == pygame.QUIT:
              run = False



    # #set colour
    # colour = (5, 102, 8)

    # # creating 4 rectangles as question answer options 
    # pygame.draw.rect(screen, colour, pygame.Rect(100, 175, 400, 200),  100, 10)
    # pygame.draw.rect(screen, colour, pygame.Rect(700, 175, 400, 200),  100, 10)
    # pygame.draw.rect(screen, colour, pygame.Rect(100, 450, 400, 200),  100, 10)
    # pygame.draw.rect(screen, colour, pygame.Rect(700, 450, 400, 200),  100, 10)

#     clock.tick(60)  # limits FPS to 60  

# # flip() the display to put your work on screen
#     pygame.display.flip()