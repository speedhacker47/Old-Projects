import pygame
import random

pygame.init()
screen_size = 400

win = pygame.display.set_mode((screen_size,screen_size))

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
cyan = (79, 190, 180)
grey = (200,200,200)

food_width = 25
snake_width = 25

sn_x = 50
sn_y = 50

food_x = random.randrange(0,screen_size,food_width)
food_y = random.randrange(0,screen_size,food_width)

# A STAR ALGORITHM

def end_dist(start,end):
    (x1, y1) = start
    (x2, y2) = end
    return abs(x1 - x2) + abs(y1 - y2)

def path():
    global val,child,extra
    child = []
    current = (sn_x,sn_y)
    h = []
    val = []
    extra = []
    p = 0
    #valid.append(current)
    while True:
        if len(child) == 0:
            current = (sn_x,sn_y)
        else:
            current = child[-1]
        # LOOKING FOR PATH
        sn = (sn_x,sn_y)
        food = (food_x,food_y)
        left = (current[0]-snake_width,current[1])
        right = (current[0]+snake_width,current[1])
        up = (current[0],current[1]-snake_width)
        down = (current[0],current[1]+snake_width)
        current_av = [left,right,up,down]
        for f in current_av:
          if f not in ob and f not in child:
              h = end_dist(f,food)
              extra.append((f[0],f[1],h))
              stuck = False
          else:
              stuck = True
        if stuck:
            child.pop(len(child)-1)
            print('runned')
            continue
                  
        extra = sorted(extra,key=lambda x:x[2])
        #print(extra)
        m = extra.pop(0)
        child.append(m)
        #print("child",child)
        p += 1
        if p == 1000 or current == food:
            break

def path_find():
    global path
    path = []
    _x = sn_x
    _y = sn_y

    while not (_x,_y) == (food_x,food_y):
        while not _x == food_x:
            if _x < food_x:
                _x += snake_width
            if _x > food_x:
                _x -= snake_width
            path.append([_x,_y])
        while not _y == food_y:
            if _y < food_y:
                _y += snake_width
            if _y > food_y:
                _y -= snake_width
            path.append([_x,_y])
    
def re_food_pos():
    global food_x,food_y
    food_x = random.randrange(0,screen_size,snake_width)
    food_y = random.randrange(0,screen_size,snake_width)

def create_obs():
    global ob
    ob = []
    o = 0
    while o < 70:
        x = random.randrange(0,screen_size,snake_width)
        y = random.randrange(0,screen_size,snake_width)
        if not(x,y) == (sn_x,sn_y) and not (x,y) == (food_x,food_y) and (x,y) not in ob:
            ob.append((x,y))
            o += 1
    
def draw():
    global ob_pos
# DRAWING FUNCTION
# PATHS
    for g in child:
        pygame.draw.rect(win,(cyan),(g[0],g[1],snake_width,snake_width))
    for g in extra:
        if g not in child and g is not (food_x,food_y):
            pygame.draw.rect(win,blue,(g[0],g[1],snake_width,snake_width))

# SNAKE HEAD AND FOOD
    pygame.draw.rect(win,green,(sn_x,sn_y,snake_width,snake_width))
    pygame.draw.rect(win,red,(food_x,food_y,snake_width,snake_width))

# OBSTACLE
    for h in ob:
        pygame.draw.rect(win,grey,(h[0],h[1],snake_width,snake_width))

create_obs()
path()
while True:
     win.fill((0,0,0))
     if (sn_x,sn_y) == (food_x,food_y):
         re_food_pos()
     #path_find()
     #print(val)
     #print(child)
     draw()
     pygame.display.update()
