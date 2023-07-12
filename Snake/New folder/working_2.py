import pygame
import random

pygame.init()
screen_width = 500

window = pygame.display.set_mode((screen_width,screen_width))
speed = 25

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

food_width = 25
snake_width = 25

font = pygame.font.SysFont('comicsans', 30, True)
tails = []
#start
turns  = []

tail_passed = []
#tail_passed_y =[]

p=0

food_x = random.randrange(0,screen_width,food_width)
food_y = random.randrange(0,screen_width,food_width)
color = blue
previous_color = red
def random_color():
    global color
    while True:
        x = random.randint(0,255)
        y = random.randint(0,255)
        z = random.randint(0,255)
        color = (x,y,z)
        if color != (1,1,1):break
        
def food():
    #x = random.randint(0,500)
    #y = random.randint(0,500)
    pygame.draw.rect(window,color,(food_x,food_y,food_width,food_width))

def collision():
    global food_x,food_y,color,previous_color
    previous_color = color
    random_color()
    food_x = random.randrange(0,screen_width,food_width)
    food_y = random.randrange(0,screen_width,food_width)
    food()
    last = len(tails)-1
    print("Collided")
    head_x = tails[last].x
    head_y = tails[last].y
    tail_side = tails[last].side
    print(last)
    print(sn.x,"head",head_x,sn.y,"head",head_y,"face",tail_side)
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
    print(last)
    print(tails)
        
    print('break')
    #print(tails[last].turns[last][0])
    '''
    #print(tails[last].turns[last][1])
    if len(tails[last].turns) != 0:
        print("1")
        if not((tails[last].turns[last][0],tails[last].turns[last][1]) == (sn.x,sn.y)):
            tails[last].turns.append((sn.x,sn.y,f))
            print("3")
    elif len(tails[last].turns) == 0 :
        print("2")
        if tails[last-1] is not tails[0] or tails[last is not tails[0]]:
            tails[last].turns = tails[last-1].turns
       '''
def valid(f):
    while True:# tails[f] is not snake_head:
        if tails[f] is not snake_head:
            return (tails[f].x,tails[f].y)
            break
        else:
            continue
    
class cube():
    def __init__(self,tail_facing,head_pos_x,head_pos_y):
        self.side = tail_facing
        self.x = head_pos_x
        self.y = head_pos_y
        #self.turns = []
        #self.turns_y = []
        #self.turn_face = [] tails[0].turns[last][0]
    def draw():
        #global tside
        for tail in tails:
            if not(tails[0] is tail):
                for w in range(len(turns)):
                    if (tail.x,tail.y) == (turns[w][0],turns[w][1]):# in tail.turns and tail.y in tail.turns_y:# and not(tail.x in tail.passed_x) and not(tail.passed_y):
                                #g = tail.turns_x.index(tail.x)
                                #print(g)
                                print("turn")
                                #print(tail.turn_face)
                                if turns[w][2] == 1:
                                    #print("u")
                                    tail.side = "down"
                                    #tail.turns.pop(w)
                                    #tail.turns_y.pop(g)
                                    #tail.turn_face.pop(g)
                                elif turns[w][2] == 2:
                                    #print("d")
                                    tail.side = "up"
                                    #tail.turns.pop(w)
                                    #tail.turns_y.pop(g)
                                    #tail.turn_face.pop(g)
                                elif turns[w][2] == 3:
                                    tail.side = "left"
                                    #print("r")
                                    #tail.turns.pop(w)
                                    #tail.turns_y.pop(g)
                                    #tail.turn_face.pop(g)
                                elif turns[w][2] == 4:
                                    tail.side = "right"
                                    #print("l")
                                    #tail.turns.pop(w)
                                    #tail.turns_y.pop(g)
                                    #tail.turn_face.pop(g)
                                else:
                                    print("error")
                                last = len(tails)-1
                                if tails[last] is tail: #or tails[last] is snake_head:
                                    turns.pop(w)
                                    print("pop")
                                    
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
                if tail.x > screen_width : tail.x = tail.x - screen_width
                if tail.y < 0 : tail.y = tail.y + screen_width
                if tail.y > screen_width : tail.y = tail.y - screen_width
                        
                pygame.draw.rect(window,previous_color,(tail.x,tail.y,snake_width-1,snake_width-1))
                pygame.draw.rect(window,color,(tail.x,tail.y,snake_width,snake_width),1)
            
class snake():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def move(self):
        e = list(map(valid,range(1,len(tails))))
        #print(e)
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
        if (sn.x,sn.y) in e:
            print("You fucked yourself.")
            pygame.time.delay(1000000000)
            
        if sn.x < 0 :               sn.x += screen_width
        if sn.x > screen_width :    sn.x -= screen_width
        if sn.y < 0 :               sn.y += screen_width
        if sn.y > screen_width :    sn.y -= screen_width
        #food()
sn = snake(250,250)
flag = True

tail_side = "left"
tails.append(cube(tail_side,sn.x,sn.y))
snake_head = tails[0]

left,up,down = False,False,False
right = True
#food(_x,_y)
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
        #for t in tails:
            #if t is not snake_head:
        if len(tails)>1:turns.append((sn.x,sn.y,2))
            #t.turns_y.append(sn.y)
                
            #t.turns_x.append(sn.x)
            #t.turn_face.append(2)
    elif keys[pygame.K_UP] and not(down) and not(up):
        left = False
        right = False
        up = True
        down = False
        tails[0].side = "down"
        #tail_side = "down"
        #for t in tails:
            #if t is not snake_head:
        if len(tails)>1:turns.append((sn.x,sn.y,1))
            #t.turns_x.append(sn.x)
            #t.turn_face.append(1)

    elif keys[pygame.K_LEFT] and not(right) and not(left):
        left = True
        right = False
        up = False
        down = False
        tails[0].side = "right"
        #tail_side = "right"
        #for t in tails:
            #if t is not snake_head:
        if len(tails)>1:turns.append((sn.x,sn.y,4))
            #t.turns_y.append(sn.y)
            #t.turns_x.append(sn.x)
            #t.turn_face.append(4)
            
    elif keys[pygame.K_RIGHT] and not(left) and not(right):
        left = False
        right = True
        up = False
        down = False
        tails[0].side = "left"
        #tail_side = "left"
        #for t in tails:
            #if t is not snake_head:
        if len(tails)>1:turns.append((sn.x,sn.y,3))
            #t.turns_y.append(sn.y)
            #t.turns_x.append(sn.x)
            #t.turn_face.append(3)

    #print(sn.x,sn.y)
    if sn.y <= food_y + food_width and sn.y >= food_y and sn.x <= food_x + food_width and sn.x >= food_x:
            collision()
    #if keys[pygame.K_SPACE]:
     #   collision()
        
 
            
    #last_x = len(turns_x)-1
    #last_f = len(turn_face)-1
    #if last_x>0:
     #   print(turns_x[last_x])
    #if last_f>0:
     #   print(turn_face[last_f])
    #print(len(tails))
    
    window.fill((0,0,0))
    food()
    
    print(len(turns))
    #if len(turns)!=0:print(turns[0])
    print(len(tails))
    cube.draw()
    sn.move()
    text = font.render("Score "+str(len(tails)), 1,(255,255,255))
    window.blit(text, (550,0))
    pygame.draw.rect(window,green,(sn.x,sn.y,snake_width,snake_width))
    pygame.display.update()
  
