import pygame
import random

# INITIAL
pygame.init()
screen_width = 500
window = pygame.display.set_mode((screen_width,screen_width))

#COLORS
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

#SOME F* VARIABLES
speed = 25
food_width = 25
snake_width = 25
font = pygame.font.SysFont('comicsans', 30, True)
tails = []
turns  = []
flag = True
high_score = 0

#ENDING FUNCTION
def End():
    global flag
    text = font.render("Game Will Restart in 3 seconds. Your Score is "+ str(score), 10,(255,255,255))
    keys = pygame.key.get_pressed()
    window.blit(text,(0,0))
    pygame.display.update()
    keys = pygame.key.get_pressed()
    pygame.time.delay(3000)
    flag = False
        
#STARTING FOOD
food_x = random.randrange(0,screen_width,food_width)
food_y = random.randrange(0,screen_width,food_width)
color = blue
previous_color = red

#COLOR RANDOM EFFECT
def random_color():
    global color
    while True:
        x = random.randint(0,255)
        y = random.randint(0,255)
        z = random.randint(0,255)
        color = (x,y,z)
        if color != (1,1,1):break
        
#DRAWING FOOD RECTANGLE
def food():
    pygame.draw.rect(window,color,(food_x,food_y,food_width,food_width))
'''
def pathfinder():
    _x = sn.x
    _y = sn.y
    path = []
    _up = up
    _down = down
    _left = left
    _right = right
    
    while not(_x,_y) == (food_x,food_y):
        e = list(map(valid,range(1,len(tails))))

        if _up:
            if _y - food_y > 0:
                while not _y == food_y:
                    _y -= speed
                    if (_x,_y) in e:
                        _y += speed
                if _x - food_x > 0:
                    path.append((_x,_y,"L"))
                    _left = True
                    _up  = False
                elif _x -food_x < 0:
                    path.append((_x,_y,"R"))
                    _up = False
                    _right = True
                elif _x == food_x:
                    pass
'''        
    #print(path)
# COLLISION 
def collision():
    global food_x,food_y,color,previous_color
    previous_color = color
    random_color()
    pygame.mixer.music.load('jump.wav')
    
    food_x = random.randrange(0+food_width,screen_width-food_width,food_width)
    food_y = random.randrange(0+food_width,screen_width-food_width,food_width)
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

#FUNCTION FOR MAP FUNCTION
def valid(f,dirct = "both"):
    while True:
        if tails[f] is not snake_head and dirct == "both":
            return (tails[f].x,tails[f].y)
            break
        else:
            continue
                

def valid_x(f):
     while True:
        if tails[f] is not snake_head:
            return tails[f].x
            break
        else:
            continue
def valid_y(f):
     while True:
        if tails[f] is not snake_head :
            return tails[f].y
            break
        else:
            continue

# CLASS OF EVERY CUBE
    
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
                                else:
                                    print("error")
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
                if tail.x < 0 : tail.x = tail.x + screen_width
                if tail.x > screen_width : tail.x = tail.x - screen_width - snake_width
                if tail.y < 0 : tail.y = tail.y + screen_width
                if tail.y > screen_width : tail.y = tail.y - screen_width - snake_width
                        
                pygame.draw.rect(window,previous_color,(tail.x,tail.y,snake_width-1,snake_width-1))
                pygame.draw.rect(window,color,(tail.x,tail.y,snake_width,snake_width),1)
dead = 0
# FUNCTIONS RELATED TO SNAKE HEAD IS INSIDE THIS CLASSS
class snake():
    def __init__(self,x,y):
        self.x = x
        self.y = y

#MOVEMENTS
    def move(self):
        global dead
        e = list(map(valid,range(1,len(tails))))
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
# LOOKING FOR DEATH
        if (sn.x,sn.y) in e:
            pygame.mixer.music.load('death.wav')
            print("died",dead)
            dead += 1

# PASSING THROUGH SCREEN
        if sn.x < 0 :               sn.x += screen_width
        if sn.x > screen_width :    sn.x -= screen_width + snake_width
        if sn.y < 0 :               sn.y += screen_width
        if sn.y > screen_width :    sn.y -= screen_width + snake_width

# MAKING A Horizontal Line
        pygame.draw.aaline(window,(200,200,200),(sn.x+(snake_width/2),sn.y+(snake_width/2)),(sn.x+(snake_width/2)+1000,sn.y+(snake_width/2)))
        pygame.draw.aaline(window,(200,200,200),(sn.x+(snake_width/2),sn.y+(snake_width/2)),(sn.x+(snake_width/2)-1000,sn.y+(snake_width/2)))

#Vertical Line
        pygame.draw.aaline(window,(200,200,200),(sn.x+(snake_width/2),sn.y+(snake_width/2)),(sn.x+(snake_width/2),sn.y+(snake_width/2)+1000))
        pygame.draw.aaline(window,(200,200,200),(sn.x+(snake_width/2),sn.y+(snake_width/2)),(sn.x+(snake_width/2),sn.y+(snake_width/2)-1000))

p=0

# LOOP TO KEEP ALIVE THE GAME
while True:
    tails = []
    number_turns = 0
    turns = []
    flag = True
    sn = snake(250,250)
    tail_side = "left"
    tails.append(cube(tail_side,sn.x,sn.y))
    snake_head = tails[0]
    left,up,down = False,False,False
    dir_l,dir_r,dir_u,dir_d = False,False,False,False
    right = True
    nummber_turns = 0
    
    while flag:
# LOWER THIS VALUE TO INCREASE SMOOTHNESS(AS WELL AS SPEED)
        pygame.time.delay(50)
#////////////////////////////////////
        for event in pygame.event.get():
            if event.type == pygame.quit:
                flag = False
        keys = pygame.key.get_pressed()


#PHASE IS POSITION OF FOOD L ,R DEFINES RIGHT OR LEFT FROM THE SNAKE FOOD
#AND L1 L2 DEFINES UPPER OR LOWER PART

        if food_x < sn.x and food_y < sn.y:
            phase = "L1"
        if food_x > sn.x and food_y > sn.y:
            phase = "R2"
        if food_x < sn.x and food_y > sn.y:
            phase = "L2"
        if food_x > sn.x and food_y < sn.y:
            phase = "R1"

# DEFINING WHERE TO MOVE ACCORDING TO PHASE
        if phase == "L1" and up or phase == "L2" and down:
            if sn.y == food_y:
                dir_l = True
                dir_r = False
                dir_d = False
                dir_u = False
                #print("done")
        elif phase == "L1" and left or phase == "R1" and right:
            if sn.x == food_x:
                dir_l = False
                dir_r = False
                dir_d = False
                dir_u = True
        elif phase == "R1" and up or phase == "R2" and down:
            if sn.y == food_y:
                dir_l,dir_u,dir_d = False,False,False
                dir_r = True
        elif phase == "R2" and right or phase == "L2" and left:
            if sn.x == food_x:
                dir_d = True
                dir_u,dir_r,dir_l = False,False,False

# SECONDARY CONTROLS (THESE ARE FOR LOOK GAME MORE COOL)
# YOU CAN REMOVE IT IF YOU WANT.

        if phase == "L1":
            if down:
                    dir_r,dir_u,dir_d = False,False,False
                    dir_l = True
            if right:
                dir_r,dir_l,dir_d = False,False,False
                dir_u = True

        if phase == "L2":
            if up:
                dir_r,dir_u,dir_d = False,False,False
                dir_l = True
                
            if right:
                dir_r,dir_l,dir_d = False,False,False
                dir_d = True

        if phase == "R1":
            if down:
                    dir_l,dir_u,dir_d = False,False,False
                    dir_r = True
            
            if left:
                dir_r,dir_d,dir_l = False,False,False
                dir_u = True
    

        if phase == "R2":
            if up:
                    dir_l,dir_u,dir_d = False,False,False
                    dir_r = True
            if left:
                dir_r,dir_l,dir_u = False,False,False
                dir_d = True
# AVOIDING FROM SELF F*
        e_x = list(map(valid_x,range(1,len(tails))))
        e_y = list(map(valid_y,range(1,len(tails))))
        e = list(map(valid,range(1,len(tails))))
        #print(sn.x,sn.y)
        if up and down:
            for p in e:
                   if p[1] == sn.y:
                     if p[0] < sn.x:
                         l = True
                         if dir_l:
                             dir_l = False
                             print("left")
                     if p[0] > sn.x:
                         r = True
                         if dir_r:
                             dir_r = False
                             print("right")
    
        
        if right and left:
            for p in e:
                   if p[0] == sn.x:
                     if p[1] < sn.y:
                         print('On down')
                         if dir_d:
                             dir_d = False
                     elif p[1] > sn.y:
                         print('On up')
                         if dir_u:
                             dir_u = False
                     if p[1] == sn.y:
                         dir_r = True
                         print('down')
        
# DOING ACTUAL MOVEMENT TO SNAKE HEAD WHICH IS DEFINED ABOVE
        if dir_d and not(up) and not(down):
            left = False
            right = False
            up = False
            down = True
            tails[0].side = "up"
            
            if len(tails)>1:
                number_turns += 1
                turns.append((sn.x,sn.y,2))
                
        elif dir_u and not(down) and not(up):
            left = False
            right = False
            up = True
            down = False
            tails[0].side = "down"
            dir_u = False
            #pathfinder()
            
            if len(tails)>1:
                number_turns += 1
                turns.append((sn.x,sn.y,1))
                

        elif dir_l and not(right) and not(left):
            left = True
            right = False
            up = False
            down = False
            tails[0].side = "right"
            
            if len(tails)>1:
                number_turns += 1
                turns.append((sn.x,sn.y,4))
                
        elif dir_r and not(left) and not(right):
            left = False
            right = True
            up = False
            down = False
            tails[0].side = "left"
            
            if len(tails)>1:
                turns.append((sn.x,sn.y,3))
                number_turns += 1

# LOOKING IF SNAKE EATS FOOD
        if sn.y <= food_y + food_width and sn.y >= food_y and sn.x <= food_x + food_width and sn.x >= food_x:
                collision()
        
# AVOIDING FROM REDRAWING ON EXISTING
        window.fill((0,0,0))
        food()
        score = len(tails)*100-number_turns*10
        score = score - 100

        if score > high_score:high_score = score

        cube.draw()
        sn.move()

        text = font.render("Eaten "+str(len(tails)), 1,color)
        text_2 = font.render("Turns "+str(number_turns), 1,color)
        text_3 = font.render("Total Score "+str(score),1,color)
        text_4 = font.render("High Score "+str(high_score),1,color) 

        window.blit(text, (5,0))
        window.blit(text_2,(140,0))
        window.blit(text_3,(270,0))
        window.blit(text_4,(5,20))

        pygame.draw.rect(window,green,(sn.x,sn.y,snake_width,snake_width))
        pygame.display.update()
      
