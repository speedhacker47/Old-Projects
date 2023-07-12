import pygame
import random

pygame.init()
screen_width = 700

window = pygame.display.set_mode((screen_width,screen_width))
speed = 25

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

food_width = 25
snake_width = 25

font = pygame.font.SysFont('comicsans', 30, True)
tails = []

turns  = []

tail_passed = []


p=0

food_x = random.randrange(0,screen_width,food_width)
food_y = random.randrange(0,screen_width,food_width)


def food():
    pygame.draw.rect(window,blue,(food_x,food_y,food_width,food_width))

def collision():
    global food_x,food_y
    food_x = random.randrange(0,screen_width,food_width)
    food_y = random.randrange(0,screen_width,food_width)
    food()
    last = len(tails)-1
    head_x = tails[last].x
    head_y = tails[last].y
    tail_side = tails[last].side
    if tail_side == "right":
        tails.append(cube("right",head_x+25,head_y))
        f = 4
    elif tail_side == "down":
        tails.append(cube("down",head_x,head_y+25))
        f = 1
    elif tail_side == "up":
        tails.append(cube("up",head_x,head_y-25))
        f = 2
    elif tail_side == "left":
        tails.append(cube("left",head_x-25,head_y))
        f = 3
    last = len(tails)-1 
class cube():
    def __init__(self,tail_facing,head_pos_x,head_pos_y):
        self.side = tail_facing
        self.x = head_pos_x
        self.y = head_pos_y
    def draw():
        for tail in tails:
            if not(tails[0] is tail):
                for w in range(len(turns)):
                    if (tail.x,tail.y) == (turns[w][0],turns[w][1]):                            
                                if turns[w][2] == 1:
                                    tail.side = "down"
                                elif turns[w][2] == 2:
                                    tail.side = "up"
                                elif turns[w][2] == 3:
                                    tail.side = "left"
                                elif turns[w][2] == 4:
                                    tail.side = "right"               
                                last = len(tails)-1
                                if tails[last] is tail: 
                                    turns.pop(w)
                                    break
                            
                if tail.side == "left":
                    tail.x += speed
                elif tail.side == "right":
                    tail.x -= speed
                elif tail.side == "down":
                    tail.y -= speed
                elif tail.side == "up":
                    tail.y +=speed
                    
                        
                pygame.draw.rect(window,red,(tail.x,tail.y,25,25))
            
class snake():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def move(self):
        if right:
            sn.x += speed
            tails[0].x += speed
        if left:
            sn.x -= speed
            tails[0].x -= speed
        if up:
            sn.y -= speed
            tails[0].y -= speed
        if down:
            sn.y +=speed
            tails[0].y += speed
sn = snake(250,250)
flag = True

tail_side = "left"
tails.append(cube(tail_side,sn.x,sn.y))
snake_head = tails[0]

left,up,down = False,False,False
right = True

while flag:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.quit:
            flag = False
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN] and not(up) and not(down):
        left = False
        right = False
        up = False
        down = True
        tails[0].side = "up"
        if len(tails)>1:turns.append((sn.x,sn.y,2))
    elif keys[pygame.K_UP] and not(down) and not(up):
        left = False
        right = False
        up = True
        down = False
        tails[0].side = "down"
        if len(tails)>1:turns.append((sn.x,sn.y,1))
    elif keys[pygame.K_LEFT] and not(right) and not(left):
        left = True
        right = False
        up = False
        down = False
        tails[0].side = "right"
        if len(tails)>1:turns.append((sn.x,sn.y,4))            
    elif keys[pygame.K_RIGHT] and not(left) and not(right):
        left = False
        right = True
        up = False
        down = False
        tails[0].side = "left"
        if len(tails)>1:turns.append((sn.x,sn.y,3))
    if sn.y <= food_y + food_width and sn.y >= food_y and sn.x <= food_x + food_width and sn.x >= food_x:
            collision()
    
    window.fill((0,0,0))
    food()
    
    cube.draw()
    sn.move()
    text = font.render("Score "+str(len(tails)), 1,(255,255,255))
    window.blit(text, (550,0))
    pygame.draw.rect(window,(0,255,0),(sn.x,sn.y,snake_width,snake_width))
    pygame.display.update()
  
