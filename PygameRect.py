''' 
Pygame Rect 

1. Rect iss used to draw a rectangle in Pygame
2. Pygame uses rect objects to store and manipulate rectangle areas.
3. A Rect can be formed from a combination of left, Top, width, height values.
4. It can also created from python objects that are already a rect or have an attribute named "rect".

5. rect() function is used to perform changes in the position or size of rectangle
6. It returns the new copy of rect with affected changes.
7. No modification in the original rectangle

x,y
top, left, right, width
topleft, bottomleft, topright, bottomright
midtop, midleft, midbottom, midright 
center, centerx, centery
size, width, height
w, h

8. The dimension of the rectangle can be changed by assigning the size, width or height.
'''

import pygame

pygame.init()
screen = pygame.display.set_mode((600,400))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.rect(screen,(0,125,125), pygame.Rect(60,60,60,60))

    pygame.display.flip()
