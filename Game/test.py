import pygame

pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("GAME")

WalkLeft = [pygame.image.load("L1.png"),pygame.image.load("L2.png"),pygame.image.load("L3.png"),pygame.image.load("L4.png"),pygame.image.load("L5.png"),pygame.image.load("L6.png"),pygame.image.load("L7.png"),pygame.image.load("L8.png"),pygame.image.load("L9.png")]
WalkRight = [pygame.image.load("R1.png"),pygame.image.load("R2.png"),pygame.image.load("R3.png"),pygame.image.load("R4.png"),pygame.image.load("R5.png"),pygame.image.load("R6.png"),pygame.image.load("R7.png"),pygame.image.load("R8.png"),pygame.image.load("R9.png")]
enemy_left = [pygame.image.load("L1E.png"),pygame.image.load("L2E.png"),pygame.image.load("L3E.png"),pygame.image.load("L4E.png"),pygame.image.load("L5E.png"),pygame.image.load("L6E.png"),pygame.image.load("L7E.png"),pygame.image.load("L8E.png"),pygame.image.load("L9E.png"),pygame.image.load("L10E.png"),pygame.image.load("L11E.png")]
enemy_right = [pygame.image.load("R1E.png"),pygame.image.load("R2E.png"),pygame.image.load("R3E.png"),pygame.image.load("R1E.png"),pygame.image.load("R5E.png"),pygame.image.load("R6E.png"),pygame.image.load("R7E.png"),pygame.image.load("R8E.png"),pygame.image.load("R9E.png"),pygame.image.load("R10E.png"),pygame.image.load("R11E.png")]
bg = pygame.image.load("bg.jpg")
char  = pygame.image.load("standing.png")

class Character(object):
    def __init__(self,x,y,h,w):
        self.x = x
        self.y = y
        self.height = h
        self.width = w
        self.vel = 2
        self.isJump = False
        self.walk = 0
        self.jumpcount = 10
        self.right_stop = True
        self.left_stop =False
        self.right = False
        self.left = False
        self.move = False
        self.facing = 1 #FACING RIGHT SIDE
        self.hitbox = (self.x + 17,self.y +2,31,57)

    def draw(self,win):
        pygame.display.update()
        win.blit(bg,(0,0))
        self.hitbox = (self.x + 17,self.y +2,31,57)
        pygame.draw.rect(win,(255,0,0),self.hitbox,2)
        if self.walk + 1>= 27:
            self.walk = 0
    
        if self.left and self.move:
            win.blit(WalkLeft[self.walk//3],(self.x,self.y))
            self.walk += 1
        elif self.right and self.move:
            win.blit(WalkRight[self.walk//3],(self.x,self.y))
            self.walk +=1
        else:
             if self.right_stop:
                win.blit(WalkRight[0],(self.x,self.y))
                self.right = False
                self.left = False

             elif self.left_stop:
                win.blit(WalkLeft[0],(self.x,self.y))
                self.left=False
                self.right = False

    def enemy_ai(self,vel):
        self.hitbox = (self.x + 18,self.y + 2,31,57)
        pygame.draw.rect(win,(255,0,0),self.hitbox,3)
        if self.walk >= 32:
            self.walk = 0

        if not(self.right):
            win.blit(enemy_left[self.walk//3],(self.x,self.y))
            self.walk += 1
            self.x += vel

        elif self.right:
            win.blit(enemy_right[self.walk//3],(self.x,self.y))
            self.walk +=1
            self.x -= vel

        if enemy.x == 20:
            enemy.right = True

        if enemy.x == 400:
            enemy.right = False            
class Gun(object):
    def __init__(self,x,y,rad,color,facing):
        self.x = x
        self.y = y
        self.radius = rad
        self.color = color
        self.facing = facing
        self.vel = 8 * facing
 
    def draw(self,win):
        pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)

face = 1
    
run = True 

player = Character(300,420,64,64)
enemy = Character(300,420,64,64)
enemy.left = True
d = 1

font = pygame.font.SysFont('comicsans', 30, True)

clock = pygame.time.Clock()
bullets = []
Num_bullets = 0
    
while run:
    text = font.render('game"new"', 1, (0,0,0))
    win.blit(text, (350, 10))
    clock.tick(27)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event == pygame.QUIT:
            run = False

    for bullet in bullets:

        bullet_y = bullet.y > enemy.hitbox[1] and bullet.y < enemy.hitbox[1] + enemy.hitbox[3]
        bullet_x = bullet.x > enemy.hitbox[0] and bullet.x < enemy.hitbox[0]+enemy.hitbox[2]

        if bullet_x and bullet_y:
            print("collision")
            bullets.pop(bullets.index(bullet))
            if enemy.right and bullet.facing == 1 :
                enemy.right = False
            elif enemy.left and bullet.facing == -1:
                enemy.right = True
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
            Gun.draw(bullet,win)
            Num_bullets +=1
        
        else:
            bullets.pop(bullets.index(bullet))
            Num_bullets -=1

    #COLLISION

    if player.hitbox[0] > enemy.hitbox[0] and player.hitbox[0] < enemy.hitbox[0] + enemy.hitbox[2]:
        print("hit")
    
    #MOVEMENTS
 
    if keys[pygame.K_LEFT] and player.x > player.vel :
        player.x -= player.vel
        player.left = True
        player.right = False
        player.right_stop = False
        player.left_stop = True
        player.move = True
        player.facing = -1

    elif keys[pygame.K_RIGHT] and player.x < 500-player.width-player.vel:
        player.x += player.vel
        player.right = True
        player.left = False
        player.right_stop = True
        player.left_stop = False
        player.move  = True
        player.facing = 1

    if not(keys[pygame.K_RIGHT]) and not(keys[pygame.K_LEFT]):
        player.move = False
    #JUMPING

    if not(player.isJump):
        if keys[pygame.K_UP]: 
                player.isJump= True
                player.right = False
    
    else:
        
        if player.jumpcount >= -10:
            neg = 1
            if player.jumpcount < 0:
                neg = -1
            player.y -= player.jumpcount ** 2 * 0.5 * neg
            player.jumpcount -= 1
        
        else:
            player.isJump= False
            player.jumpcount = 10

    #FIRING
    Character.enemy_ai(enemy,-1)

    if keys[pygame.K_SPACE]:
        if len(bullets) < 6:
            bullets.append(Gun(player.x + 40,round(player.y + 40),6,(0,0,0),player.facing))
        
    
    Character.draw(player,win)
    
pygame.quit()

