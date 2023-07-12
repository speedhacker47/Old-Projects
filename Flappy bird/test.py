import pygame

pygame.init()

screen_height = 500
screen_width = 700

bird_size = 45
gravity = 4
jump_speed = 15

black = (1,1,1)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
white = (255,255,255)

jump = False

window = pygame.display.set_mode((screen_height,screen_width))
bg = pygame.image.load('bg.jpg')

class player:
    def __init__(self,pos_x,pos_y):
        self.x = pos_x
        self.y = pos_y

    def jump(self):
        self.y = self.y - jump_speed

    def draw(self):
        pygame.draw.rect(window,red,(self.x,self.y,bird_size,bird_size))
    def jump(self):
        keys = pygame.key.get_pressed()
        print(keys[pygame.K_UP])
        if jump and bird.y < screen_height:
            print("jump")
            self.y -= jump_speed
        elif self.y < screen_width : self.y += gravity
        else:pass
       
bird = player(150,250)

while True:
    print(bird.x,bird.y)
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                jump = True
            else:
                jump = False
        else:
            jump = False
    #window.blit(background,(0,0))
    window.blit(bg,(0,0))
    bird.jump()
    bird.draw()
    pygame.display.update()

