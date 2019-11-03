##generate random level
##solve the "maze" each time
##random start location
##x number of steps - finish is where the steps end
##reach the end object
import random, time
import os


def generateLevel():
    os.remove("randLevel.txt")

    dirs = ['w', 'n', 'e', 's']

    startx = random.randint(1, 12)
    starty = random.randint(1, 12)

    finishx, finishy = 0, 0

    curx = startx
    cury = starty

    coordinates = []

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

    for step in range(150):
        randDir = random.choice(dirs)
        while (curx == 1 and randDir == 'w') or (curx == 12 and randDir == 'e') or (cury == 1 and randDir == 'n') or (cury == 12 and randDir == 's'):
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

        if step == 149:
            finishx = curx
            finishy = cury

    levelStr = ""

    for y in range(1, len(levelGrid)-1):
        for x in range(1, len(levelGrid[y])-1):
            if levelGrid[y][x] != 'G':
                ##go through all patterns
                ##left wall
                if (levelGrid[y-1][x] != 'G') and (levelGrid[y][x+1] != 'G') and (levelGrid[y+1][x] != 'G') and (levelGrid[y][x-1] == 'G'):
                    levelGrid[y][x] = 'L'
                ##right wall
                elif (levelGrid[y-1][x] != 'G') and (levelGrid[y][x-1] != 'G') and (levelGrid[y+1][x] != 'G') and (levelGrid[y][x+1] == 'G'):
                    levelGrid[y][x] = 'R'
                ##bottom wall
                elif (levelGrid[y-1][x] != 'G') and (levelGrid[y][x-1] != 'G') and (levelGrid[y][x+1] != 'G') and (levelGrid[y+1][x] == 'G'):
                    levelGrid[y][x] = 'D'
                ##upper wall
                elif (levelGrid[y+1][x] != 'G') and (levelGrid[y][x-1] != 'G') and (levelGrid[y][x+1] != 'G') and (levelGrid[y-1][x] == 'G'):
                    levelGrid[y][x] = 'U'
                ##left bottom wall
                elif (levelGrid[y+1][x] == 'G') and (levelGrid[y][x-1] == 'G') and (levelGrid[y][x+1] != 'G') and (levelGrid[y-1][x] != 'G'):
                    levelGrid[y][x] = 'B'
                ##right bottom wall
                elif (levelGrid[y+1][x] == 'G') and (levelGrid[y][x+1] == 'G') and (levelGrid[y][x-1] != 'G') and (levelGrid[y-1][x] != 'G'):
                    levelGrid[y][x] = 'F'
                ##left upper wall
                elif (levelGrid[y+1][x] != 'G') and (levelGrid[y][x+1] != 'G') and (levelGrid[y][x-1] == 'G') and (levelGrid[y-1][x] == 'G'):
                    levelGrid[y][x] = 'C'
                ##right upper wall
                elif (levelGrid[y+1][x] != 'G') and (levelGrid[y][x-1] != 'G') and (levelGrid[y][x+1] == 'G') and (levelGrid[y-1][x] == 'G'):
                    levelGrid[y][x] = 'T'
                ##right closed
                elif (levelGrid[y+1][x] == 'G') and (levelGrid[y][x-1] == 'G') and (levelGrid[y][x+1] != 'G') and (levelGrid[y-1][x] == 'G'):
                    levelGrid[y][x] = 'V'
                ##down closed
                elif (levelGrid[y+1][x] != 'G') and (levelGrid[y][x-1] == 'G') and (levelGrid[y][x+1] == 'G') and (levelGrid[y-1][x] == 'G'):
                    levelGrid[y][x] = 'Q'
                ##left closed
                elif (levelGrid[y+1][x] == 'G') and (levelGrid[y][x-1] != 'G') and (levelGrid[y][x+1] == 'G') and (levelGrid[y-1][x] == 'G'):
                    levelGrid[y][x] = 'J'
                ##up closed
                elif (levelGrid[y+1][x] == 'G') and (levelGrid[y][x-1] == 'G') and (levelGrid[y][x+1] == 'G') and (levelGrid[y-1][x] != 'G'):
                    levelGrid[y][x] = 'H'
                ##left right
                elif (levelGrid[y+1][x] != 'G') and (levelGrid[y][x-1] == 'G') and (levelGrid[y][x+1] == 'G') and (levelGrid[y-1][x] != 'G'):
                    levelGrid[y][x] = 'P'
                ##up down
                elif (levelGrid[y+1][x] == 'G') and (levelGrid[y][x-1] != 'G') and (levelGrid[y][x+1] != 'G') and (levelGrid[y-1][x] == 'G'):
                    levelGrid[y][x] = 'Z'
                ##lone wall
                elif (levelGrid[y+1][x] == 'G') and (levelGrid[y][x-1] == 'G') and (levelGrid[y][x+1] == 'G') and (levelGrid[y-1][x] == 'G'):
                    levelGrid[y][x] = 'O'



            levelStr += levelGrid[y][x]
        levelStr += "/n"

    prevLevel = open("randLevel.txt", "a")

    for i in range(1,len(levelGrid)-1):
        tempLine = ""
        for j in range(1,len(levelGrid[i])-1):
            tempLine += levelGrid[i][j]
        prevLevel.write(tempLine + "\n")

    prevLevel.close()

    return startx, starty, finishx, finishy


def main():
    generateLevel()

main()


