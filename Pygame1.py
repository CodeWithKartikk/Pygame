''' 

1. First Requirement - Pygame Library in Python
2. Import Pygame Library in the python file (import means to fetch the modules of pygame)
3. pygame.init() --> This will initiate Pygame and allow us to write various commands with pyagame.
4. You have to define our game's display which is going to be the main display of our game
5. You have to display our screen with the help of display method/function.
6. Now You have to set the width and height of the screen with the help of set_mode(width, height) function.
7. Simply, this is our game clock. You generally use clock to track within the game, and this is 
   basically used in FPS (Frames per second).
8. Game Loop - While -> For -> If -> crashed = True 
9. pygame.quit() - We have to break our game loop. This will end our pygame instance.
10. quit() - It will exit python and the application

'''

import pygame # Imported Pygame library which is compulsory to make use of modules of pygame

pygame.init() # Initializing Pygame and now i am ready to create any application

# variable = pygame.func()
screenDisplay = pygame.display.set_mode((600,500))
clock = pygame.time.Clock()
crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        print(event)
    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()