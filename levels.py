# HackPHS 2019
# Irina Mukhametzhanova
# 11/3/19
# Find the Light - level generator

import random
import os


def generateLevel():
    os.remove("randLevel.txt") # Remove the old grid

    dirs = ['w', 'n', 'e', 's'] # List of directions (West, North, East, and Sount)

    startx = random.randint(1, 12) # Random starting position
    starty = random.randint(1, 12)

    finishx, finishy = 0, 0 # For final location

    curx = startx # Current location
    cury = starty

    # Current level grid (where the random walk goes, the W's will be changed to G's
    # W - wall, G - grass
    levelGrid = [['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
                 ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
                 ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
                 ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
                 ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
                 ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
                 ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
                 ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
                 ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
                 ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
                 ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
                 ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
                 ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
                 ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']]

    levelGrid[starty][startx] = 'G'

    # Take 150 steps
    for step in range(150):
        randDir = random.choice(dirs) # Pick a random direction until it does not go outside the border
        while (curx <= 1 and randDir == 'w') or (curx >= 12 and randDir == 'e') or (cury <= 1 and randDir == 'n') or (cury >= 12 and randDir == 's'):
            randDir = random.choice(dirs)

        if randDir == 'w':
            curx -= 1
        elif randDir == 'n':
            cury -= 1
        elif randDir == 'e':
            curx += 1
        elif randDir == 's':
            cury += 1

        levelGrid[cury][curx] = 'G'

        if step == 149: # For final location
            finishx = curx
            finishy = cury
            levelGrid[finishy][finishx] = 'G'

    levelStr = "" # For writing in the file

    for y in range(1, len(levelGrid)-1):
        for x in range(1, len(levelGrid[y])-1):
            if levelGrid[y][x] != 'G':
                # Going through all possible types of walls by checking each wall's neighbors
                # left wall
                if (levelGrid[y-1][x] != 'G') and (levelGrid[y][x+1] != 'G') and (levelGrid[y+1][x] != 'G') and (levelGrid[y][x-1] == 'G'):
                    levelGrid[y][x] = 'L'
                # right wall
                elif (levelGrid[y-1][x] != 'G') and (levelGrid[y][x-1] != 'G') and (levelGrid[y+1][x] != 'G') and (levelGrid[y][x+1] == 'G'):
                    levelGrid[y][x] = 'R'
                # bottom wall
                elif (levelGrid[y-1][x] != 'G') and (levelGrid[y][x-1] != 'G') and (levelGrid[y][x+1] != 'G') and (levelGrid[y+1][x] == 'G'):
                    levelGrid[y][x] = 'D'
                # upper wall
                elif (levelGrid[y+1][x] != 'G') and (levelGrid[y][x-1] != 'G') and (levelGrid[y][x+1] != 'G') and (levelGrid[y-1][x] == 'G'):
                    levelGrid[y][x] = 'U'
                # left bottom wall
                elif (levelGrid[y+1][x] == 'G') and (levelGrid[y][x-1] == 'G') and (levelGrid[y][x+1] != 'G') and (levelGrid[y-1][x] != 'G'):
                    levelGrid[y][x] = 'B'
                # right bottom wall
                elif (levelGrid[y+1][x] == 'G') and (levelGrid[y][x+1] == 'G') and (levelGrid[y][x-1] != 'G') and (levelGrid[y-1][x] != 'G'):
                    levelGrid[y][x] = 'F'
                # left upper wall
                elif (levelGrid[y+1][x] != 'G') and (levelGrid[y][x+1] != 'G') and (levelGrid[y][x-1] == 'G') and (levelGrid[y-1][x] == 'G'):
                    levelGrid[y][x] = 'C'
                # right upper wall
                elif (levelGrid[y+1][x] != 'G') and (levelGrid[y][x-1] != 'G') and (levelGrid[y][x+1] == 'G') and (levelGrid[y-1][x] == 'G'):
                    levelGrid[y][x] = 'T'
                # right closed
                elif (levelGrid[y+1][x] == 'G') and (levelGrid[y][x-1] == 'G') and (levelGrid[y][x+1] != 'G') and (levelGrid[y-1][x] == 'G'):
                    levelGrid[y][x] = 'V'
                # down closed
                elif (levelGrid[y+1][x] != 'G') and (levelGrid[y][x-1] == 'G') and (levelGrid[y][x+1] == 'G') and (levelGrid[y-1][x] == 'G'):
                    levelGrid[y][x] = 'Q'
                # left closed
                elif (levelGrid[y+1][x] == 'G') and (levelGrid[y][x-1] != 'G') and (levelGrid[y][x+1] == 'G') and (levelGrid[y-1][x] == 'G'):
                    levelGrid[y][x] = 'J'
                # up closed
                elif (levelGrid[y+1][x] == 'G') and (levelGrid[y][x-1] == 'G') and (levelGrid[y][x+1] == 'G') and (levelGrid[y-1][x] != 'G'):
                    levelGrid[y][x] = 'H'
                # left right wall
                elif (levelGrid[y+1][x] != 'G') and (levelGrid[y][x-1] == 'G') and (levelGrid[y][x+1] == 'G') and (levelGrid[y-1][x] != 'G'):
                    levelGrid[y][x] = 'P'
                # up down wall
                elif (levelGrid[y+1][x] == 'G') and (levelGrid[y][x-1] != 'G') and (levelGrid[y][x+1] != 'G') and (levelGrid[y-1][x] == 'G'):
                    levelGrid[y][x] = 'Z'
                # lone wall
                elif (levelGrid[y+1][x] == 'G') and (levelGrid[y][x-1] == 'G') and (levelGrid[y][x+1] == 'G') and (levelGrid[y-1][x] == 'G'):
                    levelGrid[y][x] = 'O'

            levelStr += levelGrid[y][x]
        levelStr += "/n"

    prevLevel = open("randLevel.txt", "a") # For drawing the grid

    # Write down the grid layout on the file
    for i in range(1,len(levelGrid)-1):
        tempLine = ""
        for j in range(1,len(levelGrid[i])-1):
            tempLine += levelGrid[i][j]
        prevLevel.write(tempLine + "\n")

    prevLevel.close()

    return startx, starty, finishx, finishy  # Return starting and finishing locations


