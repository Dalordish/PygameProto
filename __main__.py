#NOTE TO SELF, TURN ALL ITEMS INTO SPRITES BECAUSE PYGAME.DRAW IS NOT AS WELL SUPPORTED AS PYGAME SPRITES

import pygame
import numpy as np
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((640,480))
done = False
is_blue = False

#Using three wheels



class player_bot:
    
    def __init__(self,x,y):
        self.const = np.matrix([ [np.sin(np.deg2rad(30)), np.sin(np.deg2rad(150)) , np.sin(np.deg2rad(270)) ] ,
        [np.cos(np.deg2rad(30)),np.cos(np.deg2rad(150)), np.cos(np.deg2rad(270))], [1,1,1] ])

        self.movementVector = [0,0,0]
        self.x = x
        self.y = y
        pygame.draw.circle(screen, (255,255,25),(x,y),20)
        pygame.draw.rect(screen, (255,0,0),pygame.Rect(x- 20,y - 20,40,5))
    def moveForwards(self):
        self.y -= 3
    def moveBackwards(self):
        self.y += 3

    def moveLeft(self):
        self.x -= 3

    def moveRight(self):
        self.x += 3
    def update(self):
        pygame.draw.circle(screen, (255,255,25),(self.x,self.y),20)
        pygame.draw.rect(screen, (255,0,0),pygame.Rect(self.x- 20,self.y - 20,40,5))
    def rotateClockwise(self):
        pygame.transform.rotate(screen,10)

    def moveMotA(self,speed):
        self.movementVector[0] = speed
    def moveMotB(self,speed):
        self.movementVector[1] = speed
    def moveMotC(self,speed):
        self.movementVector[2] = speed

    def resolvePosition(self):
        print("---------------------------")
        print(self.movementVector)
        print(self.const)

        moveXY = np.array(np.dot(np.matrix(self.movementVector) , self.const))[0]
        self.x += int(moveXY[0])
        self.y += int(moveXY[1])


class ball:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        pygame.draw.circle(screen,(0,255,0),(x,y),10)
    def update(self):
        pygame.draw.circle(screen,(0,255,0),(self.x,self.y),10)
test = player_bot(30,30)
defaultBall = ball(30,30)


while not done:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed() #placing pygame keypress into object


#Movement control
    if pressed[pygame.K_UP]:
        test.moveMotA(2)
    if pressed[pygame.K_DOWN]:
        test.moveMotC(2)
    if pressed[pygame.K_LEFT]:
        test.moveMotA(0)
        test.moveMotC(0)
        test.moveMotB(0)
    if pressed[pygame.K_RIGHT]:
        test.moveMotB(2)
    test.resolvePosition()
#Refresh the screen and draw again
    screen.fill((0, 0, 0))
    defaultBall.update()
    test.update()
  #  pygame.draw.circle(screen, (0,255,0),(50,50),20)
   # pygame.draw.circle(screen, (255,255,25),(x,y),20)
    #pygame.draw.rect(screen, (255,0,0),pygame.Rect(x- 20,y - 20,40,5))
    


    pygame.display.flip()


