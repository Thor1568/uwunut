import pygame
import math
from os import path

pygame.init()
pygame.font.init()

displayWidth = 800
displayHeight = 600


SCREEN_SIZE = (displayWidth, displayHeight)
gameWin = pygame.display.set_mode(SCREEN_SIZE)
gClock = pygame.time.Clock()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 0, 255)
BLUE = (0, 255, 0)
FPS = 60
BG_COLOR = WHITE

class Bumper(pygame.sprite.Sprite):
    """docstring forBumper."""
    def __init__(self, pos, radius, color):
        pygame.sprite.Sprite.__init__(self)
        self.pos = pos
        self.radius = radius
        self.image = pygame.Surface((radius*2, radius*2))
        self.image.fill(BG_COLOR)
        pygame.draw.circle(self.image, color, (radius,radius), radius)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]; self.rect.y = pos[1];

    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y
        self.pos = (self.rect.x, self.rect.y)

    def update(self):
        pass


class Pinball(pygame.sprite.Sprite):
    """docstring forBumper."""
    def __init__(self, pos, radius, color):
        pygame.sprite.Sprite.__init__(self)
        self.pos = pos
        self.radius = radius
        self.image = pygame.Surface((radius*2, radius*2))
        self.image.fill(BG_COLOR)
        pygame.draw.circle(self.image, color, (radius,radius), radius)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]; self.rect.y = pos[1];

    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y
        self.pos = (self.rect.x, self.rect.y)

    def setVector(self, vector):
        self.vector = vector

    def update(self):
        pass



ORIGIN = (displayWidth//2, displayHeight//2)
pinball_rad = 20
firstPinVec = (5, 5)
mypinball = Pinball(ORIGIN, pinball_rad, RED)
mypinball.setVector(firstPinVec)
mybumper = Bumper((displayWidth//2+200, displayHeight//2+150), pinball_rad*2, BLUE)

all_sprites = pygame.sprite.Group()
bumpers = pygame.sprite.Group
all_sprites.add(mybumper, mypinball)
vMove = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                break
            if event.key == pygame.K_SPACE:
                if vMove == True:
                    vMove = False
                else:
                    vMove = True

    if vMove == True:
        mypinball.move(mypinball.vector[0], mypinball.vector[1])

    gameWin.fill(BG_COLOR)
    all_sprites.draw(gameWin)
    pygame.display.update()
    gClock.tick(FPS)
