import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 400, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Multiple choice quiz")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Fonts
font = pygame.font.SysFont(None, 40)

# Button class
class Button:
    def __init__(self, text, pos):
        self.text = text
        self.pos = pos
        self.width, self.height = 200, 50
        self.rect = pygame.Rect(self.pos, (self.width, self.height))

    def draw(self):
        pygame.draw.rect(screen, GRAY, self.rect)
        text_surface = font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

# Create buttons
A_button = Button("Option A", (100, 100))
B_button = Button("Option B", (100, 200))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    A_button.draw()
    B_button.draw()
    pygame.display.flip()

pygame.quit()
sys.exit()

