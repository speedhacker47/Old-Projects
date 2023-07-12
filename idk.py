import pygame

pygame.init()

window = pygame.display.set_mode((720,400))

grey = (200,200,200)
black = (1,1,1)

player = pygame.Rect(20,20,20,20)
gravity = 2
speed = 3
jump = 6

ground = False

def draw():
    global ground
    pygame.draw.rect(window,grey,player)
    if player.bottom < 400:
        player.y += gravity
        if player.bottom < 400- jump+1:
            ground = False
    #else:
     #   ground = True
    
def control():
    global ground
    print(ground)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and ground:
        player.x += speed
    elif keys[pygame.K_LEFT] and ground:
        player.x -= speed
    
    if ground and keys[pygame.K_SPACE]:
        player.y -= jump
        if player.y < 400-jump:
            ground = False
    

while True:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event == pygame.quit:
            pygame.quit()

    window.fill(black)
    draw()
    control()
    pygame.display.update()
