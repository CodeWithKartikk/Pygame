import pygame
import time
import random

pygame.init()

width = 800
height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

car_width = 73

gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption('A Car racey game')
clock = pygame.time.Clock()

carImg = pygame.image.load(r'C:\Users\Lenovo\OneDrive\Desktop\Pygame\racecar.png')

def things(thingx, thingy, thinkw, thinkh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thinkw, thinkh])

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def textObjects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def messageDisplay(text):
    largeText = pygame.font.Font('freesanbold.ttf',115)
    TextSurf, TextRect = textObjects(text, largeText)
    TextRect.center = ((width/2), (height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    gameLoop()

def crash():
    messageDisplay('You Crashed')

def gameLoop():
    x = (width * 0.45)
    y = (height * 0.8)

    x_change = 0

    thing_startx = random.randrange(0,width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change=0
        x += x_change
        gameDisplay.fill(white)

        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed
        car(x,y) 

        if x >= width - car_width or x < 0:
            crash()
        if thing_starty > height:
            thing_starty =  - thing_height
            thing_startx = random.randrange(0, width)

        if y < thing_starty+thing_height:
            print('y crossover')
        
            if x > thing_startx and x < thing_startx + thing_width or x +car_width > thing_startx and x + car_width < thing_startx + thing_width:
                print('x crossover')
                crash()

        
        pygame.display.update()
        clock.tick(60)

gameLoop()
pygame.quit()
quit()