# https://www.youtube.com/watch?v=NjvIooRpuH4&list=PLQVvvaa0QuDdLkP8MrOXLe_rKuf6r80KO&index=4

import pygame
import time

pygame.init()

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Test')
clock = pygame.time.Clock()

carImg = pygame.image.load('unnamed.jpg')

def text_objects(text, font):
    textSurface = font.render(text, True, black)  # what to render, anti-aliasing, colour
    return textSurface, textSurface

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (800/2, 600/2)
    gameDisplay.blit(TextSurf, TextRect)

    time.sleep(2)

    game_loop()

def crash():
    message_display('You crashed')

def car(x,y):  # car object
    gameDisplay.blit(carImg, (x,y)) # drawing carImg to x,y

def game_loop():

    x = (100)
    y = (100)
    x_change = 0

    gameExit = False

    while not gameExit:  # user controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -10
                elif event.key == pygame.K_RIGHT:
                    x_change = 10

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

            print(event)

        x += x_change

        gameDisplay.fill(white)
        car(x,y)

        if x > 800 or x < 0:  # boundaries
            crash()

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
