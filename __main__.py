#NOTE TO SELF, TURN ALL ITEMS INTO SPRITES BECAUSE PYGAME.DRAW IS NOT AS WELL SUPPORTED AS PYGAME SPRITES

import pygame

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((400,300))
done = False
is_blue = False


class player_bot:
    def __init__(self,x,y):
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
        pygame.transform.rotate(self,10)


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
        test.moveForwards()
    if pressed[pygame.K_DOWN]:
        test.moveBackwards()
    if pressed[pygame.K_LEFT]:
        test.moveLeft()
    if pressed[pygame.K_RIGHT]:
        test.rotateClockwise()
    if is_blue:
        color = (0,128,255)
    else:
        color = (255,100,0)


#Refresh the screen and draw again
    screen.fill((0, 0, 0))
    defaultBall.update()
    test.update()
  #  pygame.draw.circle(screen, (0,255,0),(50,50),20)
   # pygame.draw.circle(screen, (255,255,25),(x,y),20)
    #pygame.draw.rect(screen, (255,0,0),pygame.Rect(x- 20,y - 20,40,5))
    


    pygame.display.flip()


