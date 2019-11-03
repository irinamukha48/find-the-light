import pygame, sys, time, random
from pygame.locals import *
from levels import generateLevel

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

WINDOWWIDTH = 600
WINDOWHEIGHT = 600


def loadPlayer():
    downimg = pygame.image.load('humandown.png')
    upimg = pygame.image.load('humanup.png')
    leftimg = pygame.image.load('humanleft.png')
    rightimg = pygame.image.load('humanright.png')
    return downimg, upimg, leftimg, rightimg


def makeWalls(txtFile):
    level = open(txtFile).read()
    walls = []
    line = 0
    offset = 0
    count = 0

    wall = pygame.image.load('wall.png')
    walld = pygame.image.load('walld.png')
    walll = pygame.image.load('walll.png')
    wallu = pygame.image.load('wallu.png')
    walllu = pygame.image.load('walllu.png')
    wallld = pygame.image.load('wallld.png')
    wallr = pygame.image.load('wallr.png')
    wallrd = pygame.image.load('wallrd.png')
    wallru = pygame.image.load('wallru.png')
    wallrc = pygame.image.load('wallrc.png')
    walldc = pygame.image.load('walldc.png')
    walllc = pygame.image.load('walllc.png')
    walluc = pygame.image.load('walluc.png')
    walllr = pygame.image.load('walllr.png')
    wallud = pygame.image.load('wallud.png')
    wallc = pygame.image.load('wallc.png')

    for x in range(len(level)):
        if count > 11:
            line += 1
            offset += 1
            count = -1
        elif level[x] == 'W':
            walls.append({'img': wall, 'rect': pygame.Rect(50*((x-offset)%12), 50*line, 50, 50)})
        elif level[x] == 'L':
            walls.append({'img': walll, 'rect': pygame.Rect(50 * ((x - offset) % 12), 50 * line, 50, 50)})
        elif level[x] == 'D':
            walls.append({'img': walld, 'rect': pygame.Rect(50 * ((x - offset) % 12), 50 * line, 50, 50)})
        elif level[x] == 'B':
            walls.append({'img': wallld, 'rect': pygame.Rect(50 * ((x - offset) % 12), 50 * line, 50, 50)})
        elif level[x] == 'F':
            walls.append({'img': wallrd, 'rect': pygame.Rect(50 * ((x - offset) % 12), 50 * line, 50, 50)})
        elif level[x] == 'R':
            walls.append({'img': wallr, 'rect': pygame.Rect(50 * ((x - offset) % 12), 50 * line, 50, 50)})
        elif level[x] == 'U':
            walls.append({'img': wallu, 'rect': pygame.Rect(50 * ((x - offset) % 12), 50 * line, 50, 50)})
        elif level[x] == 'C':
            walls.append({'img': walllu, 'rect': pygame.Rect(50 * ((x - offset) % 12), 50 * line, 50, 50)})
        elif level[x] == 'T':
            walls.append({'img': wallru, 'rect': pygame.Rect(50 * ((x - offset) % 12), 50 * line, 50, 50)})
        elif level[x] == 'V':
            walls.append({'img': wallrc, 'rect': pygame.Rect(50 * ((x - offset) % 12), 50 * line, 50, 50)})
        elif level[x] == 'Q':
            walls.append({'img': walldc, 'rect': pygame.Rect(50 * ((x - offset) % 12), 50 * line, 50, 50)})
        elif level[x] == 'J':
            walls.append({'img': walllc, 'rect': pygame.Rect(50 * ((x - offset) % 12), 50 * line, 50, 50)})
        elif level[x] == 'H':
            walls.append({'img': walluc, 'rect': pygame.Rect(50 * ((x - offset) % 12), 50 * line, 50, 50)})
        elif level[x] == 'P':
            walls.append({'img': walllr, 'rect': pygame.Rect(50 * ((x - offset) % 12), 50 * line, 50, 50)})
        elif level[x] == 'Z':
            walls.append({'img': wallud, 'rect': pygame.Rect(50 * ((x - offset) % 12), 50 * line, 50, 50)})
        elif level[x] == 'O':
            walls.append({'img': wallc, 'rect': pygame.Rect(50 * ((x - offset) % 12), 50 * line, 50, 50)})
        count += 1

    return walls


def main():
    pygame.init()
    mainClock = pygame.time.Clock()

    screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
    pygame.display.set_caption('haha gaem')

    startx, starty, finishx, finishy = generateLevel()
    walls = makeWalls("randLevel.txt")

    moveUp = False
    moveDown = False
    moveLeft = False
    moveRight = False

    collideUp = False

    iter = 0

    player = pygame.Rect(startx*50, starty*50, 50, 50)

    downStretchedimg, upStretchedimg, leftStretchedimg, rightStretchedimg = loadPlayer()
    curimg = downStretchedimg
    bg = pygame.image.load('bg.png').convert()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_UP:
                    moveUp = True
                    moveDown = False
                if event.key == K_DOWN:
                    moveDown = True
                    moveUp = False
                if event.key == K_LEFT:
                    moveLeft = True
                    moveRight = False
                if event.key == K_RIGHT:
                    moveRight = True
                    moveLeft = False

            if event.type == KEYUP:
                if event.key == K_UP:
                    moveUp = False
                if event.key == K_DOWN:
                    moveDown = False
                if event.key == K_LEFT:
                    moveLeft = False
                if event.key == K_RIGHT:
                    moveRight = False

        screen.blit(bg, (0, 0))

        for wall in walls:
            screen.blit(wall['img'], wall['rect'])
            ##check collision - doesnt reset to false
            if player.colliderect(wall['rect']):
                if player.top < wall['rect'].bottom - 70:
                    collideUp = True
                else:
                    collideUp = False

        if moveUp and player.top > 0 and collideUp is False:
            curimg = upStretchedimg
            player.top -= 2
        if moveDown and player.bottom < WINDOWHEIGHT:
            curimg = downStretchedimg
            player.bottom += 2

        if moveLeft and player.left > 0:
            curimg = leftStretchedimg
            player.left -= 2
        if moveRight and player.right < WINDOWWIDTH:
            curimg = rightStretchedimg
            player.left += 2

        screen.blit(curimg, player)

        pygame.display.update()
        mainClock.tick(400)


main()

