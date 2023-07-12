import pygame

pygame.init()
window = pygame.display.set_mode((500,500))
speed = 1

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

tails = []


class cube():
    def __init__(self,tail_facing,head_pos_x,head_pos_y):
        self.side = tail_facing
        self.x = head_pos_x
        self.y = head_pos_y 
    def draw():
        for tail in tails:            
            if right:
                tail.x += speed
            elif left:
                tail.x -= speed
            elif up:
                tail.y -= speed
            elif down:
                tail.y +=speed
            pygame.draw.rect(window,red,(tail.x,tail.y,25,25))
        
    
class snake():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def move(self):
        if right:
            sn.x += speed
        if left:
            sn.x -= speed
        if up:
            sn.y -= speed
        if down:
            sn.y +=speed
sn = snake(0,0)
flag = True

tail_side = "left"
tails.append(cube("right",sn.x,sn.y))

left,up,down = False,False,False
right = True



pos = 20
while flag:

    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.quit:
            flag = False
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN] and not(up):
        left = False
        right = False
        up = False
        down = True
        tail_side = "up"
    elif keys[pygame.K_UP] and not(down):
        left = False
        right = False
        up = True
        down = False
        tail_side = "down"
    elif keys[pygame.K_LEFT] and not(right):
        left = True
        right = False
        up = False
        down = False
        tail_side = "right"
    elif keys[pygame.K_RIGHT] and not(left):
        left = False
        right = True
        up = False
        down = False
        tail_side = "left"
    if keys[pygame.K_SPACE]:
        last = len(tails)-1
        pos += 0
        head_x = tails[last].x
        head_y = tails[last].y
        if tail_side == "right":
            tails.append(cube("right",head_y+25,head_y))
        elif tail_side == "down":
            tails.append(cube("down",head_x,head_y+25))
        elif tail_side == "up":
            tails.append(cube("up",head_x,head_y-25))
        elif tail_side == "left":
            tails.append(cube("left",head_x-25,head_y))
 
            
        
    sn.move()
    
    window.fill((0,0,0))
    cube.draw()
    pygame.draw.rect(window,(0,255,0),(sn.x,sn.y,25,25))
    pygame.display.update()
  
