import pygame

pygame.init()
window = pygame.display.set_mode((500,500))
speed = 1

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

tails = []
#start

tail_passed_x = []
tail_passed_y =[]

p=0

class cube():
    def __init__(self,tail_facing,head_pos_x,head_pos_y):
        self.side = tail_facing
        self.x = head_pos_x
        self.y = head_pos_y
        self.turns_x = []
        self.turns_y = []
        self.turn_face = []
    def draw():
        #global tside
        for tail in tails:            
            if tail.x in tail.turns_x and tail.y in tail.turns_y:# and not(tail.x in tail.passed_x) and not(tail.passed_y):
                        g = tail.turns_x.index(tail.x)
                        print(g)
                        print(tail.turn_face)
                        if tail.turn_face[g] == 1:
                            print("u")
                            tail.side = "down"
                            tail.turns_x.pop(g)
                            tail.turns_y.pop(g)
                            tail.turn_face.pop(g)
                        elif tail.turn_face[g] == 2:
                            print("d")
                            tail.side = "up"
                            tail.turns_x.pop(g)
                            tail.turns_y.pop(g)
                            tail.turn_face.pop(g)
                        elif tail.turn_face[g] == 3:
                            tail.side = "left"
                            print("r")
                            tail.turns_x.pop(g)
                            tail.turns_y.pop(g)
                            tail.turn_face.pop(g)
                        elif tail.turn_face[g] == 4:
                            tail.side = "right"
                            print("r")
                            tail.turns_x.pop(g)
                            tail.turns_y.pop(g)
                            tail.turn_face.pop(g)
                        else:
                            print("other")
                    
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
        if left:
            sn.x -= speed
        if up:
            sn.y -= speed
        if down:
            sn.y +=speed
sn = snake(250,250)
flag = True

tail_side = "left"
tails.append(cube(tail_side,sn.x,sn.y))

left,up,down = False,False,False
right = True

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
        #tail_side = "up"
        for t in tails:
            t.turns_y.append(sn.y)
            t.turns_x.append(sn.x)
            t.turn_face.append(2)
    elif keys[pygame.K_UP] and not(down):
        left = False
        right = False
        up = True
        down = False
        #tail_side = "down"
        for t in tails:
            t.turns_y.append(sn.y)
            t.turns_x.append(sn.x)
            t.turn_face.append(1)

    elif keys[pygame.K_LEFT] and not(right):
        left = True
        right = False
        up = False
        down = False
        #tail_side = "right"
        for t in tails:
            t.turns_y.append(sn.y)
            t.turns_x.append(sn.x)
            t.turn_face.append(4)
            
    elif keys[pygame.K_RIGHT] and not(left):
        left = False
        right = True
        up = False
        down = False
        #tail_side = "left"
        for t in tails:
            t.turns_y.append(sn.y)
            t.turns_x.append(sn.x)
            t.turn_face.append(3)

    if keys[pygame.K_SPACE]:
        last = len(tails)-1
        #print(last)
        head_x = tails[last].x
        head_y = tails[last].y
        tail_side = tails[last].side
        if tail_side == "right":
            tails.append(cube("right",head_y+25,head_y))
        elif tail_side == "down":
            tails.append(cube("down",head_x,head_y+25))
        elif tail_side == "up":
            tails.append(cube("up",head_x,head_y-25))
        elif tail_side == "left":
            tails.append(cube("left",head_x-25,head_y))
 
            
    #last_x = len(turns_x)-1
    #last_f = len(turn_face)-1
    #if last_x>0:
     #   print(turns_x[last_x])
    #if last_f>0:
     #   print(turn_face[last_f])
    sn.move()
    window.fill((0,0,0))
    cube.draw()
    pygame.draw.rect(window,(0,255,0),(sn.x,sn.y,25,25))
    pygame.display.update()
  
