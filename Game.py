import pygame
import math
import time

pygame.init()

WIDTH = 500
ROWS = 3

TIC_IMAGE = pygame.transform.scale(pygame.image.load("Images/tec.png"), (500, 500))
win = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Tic Tac Toe")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

Initiating_window = TIC_IMAGE
X_IMAGE = pygame.transform.scale(pygame.image.load("Images/X.png"), (150, 150))
O_IMAGE = pygame.transform.scale(pygame.image.load("Images/O.png"), (150, 150))

win.blit(Initiating_window, (0, 0))
pygame.display.update()
time.sleep(3)
win.fill(WHITE)

END_FONT = pygame.font.SysFont("courier", 40)
