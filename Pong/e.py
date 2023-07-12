import pygame
import random

pygame.init()

win_x = 1000
win_y = 600

window = pygame.display.set_mode((win_x,win_y))

solids = []
speed = 1

grey = (200,200,200)
num_of_circles = 30

def rand_pos(win):
    global win_x,win_y
    if win == win_x:
        return random.randint(0,win_x)
    elif win == win_y:
        return random.randint(0,win_y)
    
def rand_speed(x,y):
    y = random.randint(x,y)
    return y
def rand_color():
    while True:
        x = random.randint(0,255)
        y = random.randint(0,255)
        z = random.randint(0,255)
        if (x,y,z) != (1,1,1):
            break
    return(x,y,z)
class solid:
    def __init__(self):
        self.rect = pygame.Rect(rand_pos(win_x),rand_pos(win_y),20,20)
        self.speed = rand_speed(5,10)/5
        self.sp_x = 1
        self.sp_y = 1
        self.color = rand_color()

def draw():
    global solids
    for r in solids:
        if r.rect.top <= 0:
            r.sp_y *= -1
        if r.rect.left <=0:
            r.sp_x *= -1
        if r.rect.bottom >= win_y:
            r.sp_y *= -1
        if r.rect.right >= win_x:
            r.sp_x *= -1

    for r in solids:
        r.rect.x += r.speed * r.sp_x
        r.rect.y += r.speed * r.sp_y
    
    for f in solids:
        pygame.draw.ellipse(window,f.color,f.rect)
        
    

def maker():
    global num_of_circles,solids
    for p in range(1,num_of_circles+1):
        p = solid()
        solids.append(p)

maker()

while True:
    #print(solids[0].rect.x,solids[0].rect.y)
    window.fill((1,1,1))
    draw()
    pygame.display.update()
