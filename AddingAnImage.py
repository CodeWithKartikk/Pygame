# surface = pygame.surface(100,100)
# surface = pygame.surface((100,100), pygame.SRCALPHA)

import pygame
pygame.init()
white = (255,255,255)

display_surface = pygame.display.set_mode((1600,600))

# set the pygame window name
pygame.display.set_caption('Pygame Adding An Image')

# Creating surface Object, image is drawn on it.
image = pygame.image.load(r'C:\Users\Kathu\OneDrive\Desktop\Pygame\py.png')

# infinite loop or game loop
while True:
    display_surface.fill(white)
    display_surface.blit(image,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()