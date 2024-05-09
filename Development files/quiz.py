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
    colour = (5, 102, 8)

    # creating 4 rectangles as question answer options 
    pygame.draw.rect(screen, colour, pygame.Rect(100, 175, 400, 200),  100, 10)
    pygame.draw.rect(screen, colour, pygame.Rect(700, 175, 400, 200),  100, 10)
    pygame.draw.rect(screen, colour, pygame.Rect(100, 450, 400, 200),  100, 10)
    pygame.draw.rect(screen, colour, pygame.Rect(700, 450, 400, 200),  100, 10)

# white color 
color = (255,255,255) 
  
# light shade of the button 
color_light = (170,170,170) 
  
# dark shade of the button 
color_dark = (100,100,100) 

# defining a font 
smallfont = pygame.font.SysFont('Corbel',35) 

# rendering a text written in 
# this font 
text = smallfont.render('quit' , True , color) 
  
while True: 
      
    for ev in pygame.event.get(): 
          
        if ev.type == pygame.QUIT: 
            pygame.quit() 
              
        #checks if a mouse is clicked 
        if ev.type == pygame.MOUSEBUTTONDOWN: 

# flip() the display to put your work on screen
    pygame.display.flip()
