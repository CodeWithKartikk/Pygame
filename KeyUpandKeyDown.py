# Pygame KEYDOWN and KEYUP detect the event if a key is physically pressed and released.
# KEYDOWNN -> Detects the key press
# KEYUP    -> Detects the key Release.

# key -> key is an integer id that represents every key on the keyword.
# mod -> This is a bitmask of all modifier keys that were in the pressed state when event occured.

import pygame
pygame.init()

# Caption is used to set the title of the window
pygame.display.set_caption('KEYDOWN & KEYUP')

pygame.display.set_mode((600,400))

while True:
    event = pygame.event.wait()
    # if the close button of the window is pressed 
    if event.type == pygame.QUIT:
        # stops the application
        break
    if event.type in (pygame.KEYDOWN, pygame.KEYUP):
        # gets the key name
        keyName = pygame.key.name(event.key)
        # converts to uppercas the key name
        keyName = keyName.upper()
    # if any key is pressed or down
    if event.type == pygame.KEYDOWN:
        print(u'"{}"key pressed'.format(keyName))
    # if any key is released
    elif event.type == pygame.KEYUP:
        print(u'"{}"key released'.format(keyName))
