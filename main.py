import pygame
import math
import random
from pygame import mixer


# initialize pygame
pygame.init()

WIDTH =  360
HEIGHT =  480
FPS = 30

# creating screen
screen = pygame.display.set_mode((WIDTH,HEIGHT))

# background
background = pygame.image.load("./images/spaceship_background.png")

#Background Sound
mixer.music.load("./sounds/background_music.wav")
mixer.music.play()

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
enemyImg = []
enemyX  = []
enemyY = []
enemyX_change  = []
enemyY_change  = []
num_of_enemies = 6
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("./images/enemy.png"))
    enemyX.append(random.randint(0, 150) )
    enemyY.append(random.randint(50,150) )
    enemyX_change.append(4)
    enemyY_change.append(40)


#bullet
# ready -> you can't see the bullet on the screen
# fire -> the bullet is currently moveing
bulletImg = pygame.image.load("./images/bullet.png")
bulletX = 0
bulletY = 370
bulletX_change =  0
bulletY_change = 10
bullet_state = "ready"

#Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10

#game over text
game_over_font = pygame.font.Font('freesansbold.ttf',32)

def show_score(x,y):
    score = font.render("Score :" + str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))

def game_over_text():
    game_over_text = font.render("GAME OVER",True,(255,255,255))
    screen.blit(game_over_text,(100,150))



# blit() = drawing
def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))

def fire_bullet(x, y):
    # x= 150, y = 0
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x,y-32)) # draw the bullet on coordinates(x=x, y-y-32)

def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt(( math.pow(enemyX-bulletX, 2) )+(math.pow(enemyY-bulletY,2)))
    if distance < 27:
        return True
    else:
        return False


#Game Loop
running = True
while running:
    # screen color
    screen.fill(( 0,0,0 ))
    # fill background image
    screen.blit(background,(0,0))

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
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    # bullet sound
                    bullet_sound = mixer.Sound("./sounds/laser.wav")
                    bullet_sound.play()
                    # get the current x coordinates of spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                playerX_change = 0

    #player boundry limit algorithm
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 295:
        playerX = 295

    #enemy movement
    for i in range(num_of_enemies):
        #game over
        if enemyY[i] > 300:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
           enemyX_change[i] =  2
           enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 295:
            enemyX_change[i] =  -2
            enemyY[i] += enemyY_change[i]

        #collision
        collision = isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            explosion_sound = mixer.Sound("./sounds/gun.wav")
            explosion_sound.play()
            bulletY = 370
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 150)
            enemyY[i] =random.randint(50,150)
        enemy(enemyX[i], enemyY[i],i) #call enemy

    #bullet movement
    if bulletY <= 0:
        # if bulletY is less then 0 or equal to 0, bulletY = 370 AND bullet_state = "ready", which means the bullet stops moving
        bulletY = 370
        bullet_state = "ready"
    if bullet_state  == "fire":
        # if the bullet state is fire, then calling fire_bullet(playerX, bulletY)
        # changing the bulletY value by bulletY-BulletChange
        fire_bullet(bulletX,bulletY)
        bulletY -=   bulletY_change


    player(playerX,playerY) #call player
    show_score(textX, textY)
    pygame.display.update()
