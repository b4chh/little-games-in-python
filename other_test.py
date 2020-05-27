import pygame

pygame.init()

pygame.display.set_caption("test")
screen = pygame.display.set_mode((1080, 720))

background = pygame.image.load('assetss/bg.jpg')

running = True

while runnnig:

    screen.blit(background, (0, -200))

