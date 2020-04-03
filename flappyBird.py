import pygame
import random
pygame.init()

screenWidth = 450
screenHeight = 748

win = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("Flappy Bird")

birdImg = pygame.image.load('flappyBird.png')
bgImg = pygame.image.load('bg.jpg')
movingBgImg = pygame.image.load('movingBG.jpg')
pipeimg = pygame.image.load('pipe.png')
upsidepipeimg = pygame.transform.rotate(pipeimg, 180)

clock = pygame.time.Clock() 

class bird(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.yvel = 1
        self.dead = False
        self.isScoring = False


    def draw(self, win):    
        win.blit(birdImg, (self.x, self.y))

    def hit(self):
        self.isJump = False
        self.jumpCount = 10
        self.x = 0
        self.y = 325


class pipeGap(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, win):
        win.blit(upsidepipeimg, (self.x, self.y-334))
        win.blit(pipeimg, (self.x, self.y+self.height))


class movingBackground(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def draw(self, win):
        win.blit(movingBgImg, (self.x, self.y))


def redrawGameWindow():
    win.blit(bgImg, (0,0))
    for pipeGap in pipeGaps:
        pipeGap.draw(win)
    bird1.draw(win)
    bg1.draw(win)
    bg2.draw(win)
    win.blit(text, (340,700))
    pygame.display.update()


score = 0 
font = pygame.font.SysFont('comicsans', 30, True)
text = font.render('Score: ' + str(score), 1, (0,0,0))
bird1 = bird(screenWidth/2-34, 300, 68, 52)
pipeGaps = []
minPipeHeight = 100
maxPipeHeight = 325
pipeGap1 = pipeGap(450, random.randint(minPipeHeight,maxPipeHeight), 100, 200)
pipeGap2 = pipeGap(725, random.randint(minPipeHeight,maxPipeHeight), 100, 200)
pipeGaps.append(pipeGap1)
pipeGaps.append(pipeGap2)
bg1 = movingBackground(0, 633, screenWidth, 175)
bg2 = movingBackground(screenWidth, 633, screenWidth, 175)
run = True
while run:
    clock.tick(90) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()

    if bird1.dead ==  False:  

        for pipeGap in pipeGaps: 
            
            pipeGap.x -= 3

            if bird1.isScoring:
                if bird1.x + bird1.width > pipeGap.x and bird1.x < pipeGap.x + pipeGap.width:
                    if bird1.y < pipeGap.y or (bird1.y + bird1.height > pipeGap.y + pipeGap.height): 

                        bird1.dead = True
                        continue
                if (bird1.x > pipeGaps[0].x + pipeGaps[0].width and bird1.x + bird1.width < pipeGaps[1].x) or (bird1.x > pipeGaps[1].x + pipeGaps[1].width and bird1.x + bird1.width< pipeGaps[0].x):
                    bird1.isScoring = False
            else:
                if bird1.x + bird1.width > pipeGap.x and bird1.x < pipeGap.x + pipeGap.width:
                    bird1.isScoring = True
                    score += 1


        if bg1.x + bg1.width < 0:
            bg1.x = screenWidth
        if bg2.x + bg2.width < 0:
            bg2.x = screenWidth
        bg1.x -= 3
        bg2.x -= 3
 
        bird1.yvel += 9.8/30 
        bird1.y += bird1.yvel

        for pipeGap in pipeGaps:
            if pipeGap.x + pipeGap.width < 0:
                pipeGap.x = screenWidth
                pipeGap.y = random.randint(minPipeHeight,maxPipeHeight)

        if bird1.y > 580 or bird1.y < 0:
            bird1.dead = True

        if keys[pygame.K_SPACE]:
            bird1.yvel = -5


    else:
        if keys[pygame.K_RETURN]:
            score = 0
            pipeGaps[0].x = 450
            pipeGaps[1].x = 725
            bird1.dead = False
            bird1.isScoring = False
            bird1.yvel = 1
            bird1.y = 300
            
    redrawGameWindow()

pygame.quit()
