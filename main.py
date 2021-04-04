import pygame
import random


# initialize pygame
pygame.init()

WIDTH =  360
HEIGHT =  480
FPS = 30

# creating screen
screen = pygame.display.set_mode((WIDTH,HEIGHT))

# Title and Icon
pygame.display.set_caption("Space Invadors")
# icon = pygame.image.load("./images/ufo-4.png")
# pygame.display.set_icon(icon)

# Player 
playerImg = pygame.image.load("./images/player.png")
playerX = 150
playerY =370
playerX_change =  0

#Enemy
enemyImg = pygame.image.load("./images/enemy.png")
enemyX = random.randint(0, 150)
enemyY =random.randint(50,150)
enemyX_change =  2
enemyY_change =  40

def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x,y):
    screen.blit(enemyImg,(x,y))


#Game Loop
running = True
while running:
    # screen color
    screen.fill(( 0,0,0 ))

    # EVENT
    for event in pygame.event.get():
        #close window
        if event.type == pygame.QUIT:
          running = False
        #if the keystroke is presssed, check wheather it is right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerX_change = 2
            if event.key == pygame.K_LEFT:
                playerX_change = -2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                playerX_change = 0

    #player boundry limit algorithm
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 295:
        playerX = 295

    #enemy boundry algorithm
    enemyX += enemyX_change
    if enemyX <= 0:
       enemyX_change =  2
       enemyY += enemyY_change
    elif enemyX >= 295:
        enemyX_change =  -2
        enemyY += enemyY_change

    player(playerX,playerY) #call player
    enemy(enemyX, enemyY) #call enemy
    pygame.display.update()
