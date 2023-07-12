import pygame

pygame.init()
window = pygame.display.set_mode((500,500))
speed = 1

x = 0
y = 0

class cube():
    def __init__(self,tail,pos_x,pos_y):
        self.tail = tail
        
        #face = tail_facing
    def add(self):
        if self.tail == "right":
            pygame.draw.rect(window,(255,0,0),(sn.x+25,sn.y,25,25))
        elif self.tail == "left":
            pygame.draw.rect(window,(255,0,0),(sn.x-25,sn.y,25,25))
        elif self.tail == "up":
            pygame.draw.rect(window,(255,0,0),(sn.x,sn.y-25,25,25))
        elif self.tail == "down":
            pygame.draw.rect(window,(255,0,0),(sn.x+25,sn.y+25,25,25))
    def follow(self):
        pass
        
        

class snake():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def move(self):
        if right:
            sn.x += speed
        elif left:
            sn.x -= speed
        elif up:
            sn.y -= speed
        elif down:
            sn.y +=speed
        else:
            print("error")

sn = snake(0,0)
flag = True

left,up,down = False,False,False
right = True

tail = "left"

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
        tail = "up"
        print("down")
    elif keys[pygame.K_UP] and not(down):
        print("up")
        left = False
        right = False
        up = True
        down = False
        tail = "down"
    elif keys[pygame.K_LEFT] and not(right):
        left = True
        print("left")
        right = False
        up = False
        down = False
        tail = "right"
    elif keys[pygame.K_RIGHT] and not(left):
        left = False
        print("right")
        right = True
        up = False
        down = False
        tail = "left"
    sn.move()
    window.fill((0,0,0))
    x = cube(tail,sn.x,sn.y)
    x.add()
    pygame.draw.rect(window,(0,255,0),(sn.x,sn.y,25,25))
    pygame.display.update()
  
