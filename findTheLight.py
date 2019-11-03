# HackPHS 2019
# Irina Mukhametzhanova
# 11/3/19
# Find the Light - the main game program

import pygame, sys, time, random
from pygame.locals import *
from levels import generateLevel

WINDOWWIDTH = 600
WINDOWHEIGHT = 600


# This function loads in the initial images for the player
def loadPlayer():
    downimg = pygame.image.load('humandown.png')
    downStretchedimg = pygame.transform.scale(downimg, (40, 40))
    upimg = pygame.image.load('humanup.png')
    upStretchedimg = pygame.transform.scale(upimg, (40, 40))
    leftimg = pygame.image.load('humanleft.png')
    leftStretchedimg = pygame.transform.scale(leftimg, (40, 40))
    rightimg = pygame.image.load('humanright.png')
    rightStretchedimg = pygame.transform.scale(rightimg, (40, 40))
    return downStretchedimg, upStretchedimg, leftStretchedimg, rightStretchedimg


# This function takes in a text file that represents a grid of grass and walls, and draws it with
# necessary images
def makeWalls(txtFile):
    level = open(txtFile).read() #String that represents the level grid
    walls = [] # List of walls (rectangles)
    line = 0
    offset = 0
    count = 0

    #Load in all of the images of different types of walls
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

    # For every square in the grid
    for x in range(len(level)):
        if count > 11:
            line += 1
            offset += 1
            count = -1
        # Different types of walls appended
        elif level[x] == 'W':
            walls.append({'img': wall, 'rect': pygame.Rect(50 * ((x - offset) % 12), 50 * line, 50, 50)})
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


# The main function
def main():
    pygame.init()
    mainClock = pygame.time.Clock()

    screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
    pygame.display.set_caption('Find the Light - HackPHS 2019 - Irina Mukhametzhanova')

    # player's starting coordinates, and the star's coordinates
    startx, starty, finishx, finishy = generateLevel()
    walls = makeWalls("randLevel.txt")

    # For moving the player
    moveUp = False
    moveDown = False
    moveLeft = False
    moveRight = False

    # For checking wall collisions
    collideUp = False
    collideRight = False
    collideLeft = False
    collideDown = False

    # For the player and star's animations
    iter = 0
    stariter = 0

    # Put player and star in their respective positions
    player = pygame.Rect((startx - 1) * 50 + 5, (starty - 1) * 50 + 5, 40, 40)
    star = pygame.Rect((finishx - 1) * 50 + 9, (finishy - 1) * 50 + 9, 32, 32)

    downStretchedimg, upStretchedimg, leftStretchedimg, rightStretchedimg = loadPlayer()
    curimg = downStretchedimg # Player's starting image

    # For animations of walking in different directions
    downimages = [pygame.image.load('humandown.png'), pygame.image.load('humandown2.png'),
                  pygame.image.load('humandown3.png'), pygame.image.load('humandown4.png')]
    upimages = [pygame.image.load('humanup.png'), pygame.image.load('humanup2.png'), pygame.image.load('humanup3.png'),
                pygame.image.load('humanup4.png')]
    leftimages = [pygame.image.load('humanleft.png'), pygame.image.load('humanleft2.png'),
                  pygame.image.load('humanleft3.png'), pygame.image.load('humanleft4.png')]
    rightimages = [pygame.image.load('humanright.png'), pygame.image.load('humanright2.png'),
                   pygame.image.load('humanright3.png'), pygame.image.load('humanright4.png')]

    # For the animation of the star
    starimages = [pygame.image.load('star1.png'), pygame.image.load('star2.png')]
    curstarimage = starimages[0]

    # The grass background
    bg = pygame.image.load('bg2.png').convert()

    # Game loop
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
                iter = 0

        screen.blit(bg, (0, 0))
        flag = False # For checking if the player reached the star

        if player.colliderect(star):
            flag = True

        for wall in walls:
            screen.blit(wall['img'], wall['rect'])

        # Wall collision check
        collision = False
        for wall in walls:
            if player.colliderect(wall['rect']):
                collision = True
                if (player.top > wall['rect'].top and player.top < wall['rect'].bottom) or (
                        player.bottom > wall['rect'].top and player.bottom < wall['rect'].bottom):
                    if player.right > wall['rect'].left and player.left < wall['rect'].left:
                        collideRight = True
                        collideLeft = False
                    if player.left < wall['rect'].right and player.right > wall['rect'].right:
                        collideLeft = True
                        collideRight = False
                if (player.left > wall['rect'].left and player.left < wall['rect'].right) or (
                        player.right > wall['rect'].left and player.right < wall['rect'].right):
                    if player.top < wall['rect'].bottom and player.bottom > wall['rect'].bottom:
                        collideUp = True
                        collideDown = False
                    if player.bottom > wall['rect'].top and player.top < wall['rect'].top:
                        collideDown = True
                        collideUp = False

        # If no collisions
        if collision is False:
            collideRight = False
            collideLeft = False
            collideUp = False
            collideDown = False

        # If free to move up
        if moveUp and player.top > 0 and (collideUp is False):
            # Change the image based on number of iterations walked (every 50)
            if iter == 0:
                curimg = upStretchedimg
            elif iter % 50 == 0:
                curimg = upimages[int(int(iter) / 50)]
            if iter > 198:
                iter = -1
            iter += 1
            player.top -= 1
        # If free to move down
        if moveDown and player.bottom < WINDOWHEIGHT and (collideDown is False):
            # Change the image based on number of iterations walked (every 50)
            if iter == 0:
                curimg = downStretchedimg
            elif iter % 50 == 0:
                curimg = downimages[int(int(iter) / 50)]
            if iter > 198:
                iter = -1
            iter += 1
            player.bottom += 1
        # If free to move left
        if moveLeft and player.left > 0 and (collideLeft is False):
            # Change the image based on number of iterations walked (every 50)
            if iter == 0:
                curimg = leftStretchedimg
            elif iter % 50 == 0:
                curimg = leftimages[int(int(iter) / 50)]
            if iter > 198:
                iter = -1
            iter += 1
            player.left -= 1
        # If free to move right
        if moveRight and player.right < WINDOWWIDTH and (collideRight is False):
            # Change the image based on number of iterations walked (every 50)
            if iter == 0:
                curimg = rightStretchedimg
            elif iter % 50 == 0:
                curimg = rightimages[int(int(iter) / 50)]
            if iter > 198:
                iter = -1
            iter += 1
            player.left += 1

        # Change the star's image every 25 iterations
        if stariter % 25 == 0:
            curstarimage = starimages[int(stariter / 25)]
        if stariter > 48:
            stariter = -1
        stariter += 1

        # If the player didn't reach the star yet
        if not flag:
            screen.blit(curimg, player)
            screen.blit(curstarimage, star)
        # If the level is finished
        else:
            # Generate new locations for the player, the star, and the walls
            left, top, sleft, stop = generateLevel()
            player = pygame.Rect((left - 1) * 50 + 5, (top - 1) * 50 + 5, 40, 40)
            star = pygame.Rect((sleft - 1) * 50 + 9, (stop - 1) * 50 + 9, 32, 32)
            walls = makeWalls("randLevel.txt")
            flag = False

        # Update the screen
        pygame.display.update()
        mainClock.tick(400)


main()
