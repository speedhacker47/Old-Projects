import pygame

pygame.init()

window = pygame.display.set_mode((720,400))

grey = (200,200,200)
black = (1,1,1)
white = (255,255,255)
blue = (0,0,255)
green = (0,255,0)
red = (255,0,0)

speed = 4

speed_of_ball = 3

op_speed = speed_of_ball - 0.02

player_score = 0
op_score = 0

player = pygame.Rect(10,10,10,50)
enemy = pygame.Rect(700,10,10,50)
ball = pygame.Rect(360,200,15,15)
#new = pygame.Rect(200,200,20,20)
font = pygame.font.SysFont('comicsans', 30, True)

ball_speed_x = ball_speed_y = speed_of_ball
speeder = list(range(1,200,3))
def restart(side):
    side =1
    ball.x = 360
    ball.y = 200
    if side==0:
        ball_speed_x = 1
    elif side == 1:
        ball_speed_x = -1
    #pygame.time.delay(1000)

def control():
    global speed,speed_of_ball,ball_speed_x,ball_speed_y,op_speed
    if player_score in speeder:
        speed += 0.3
        speed_of_ball += 0.3
        op_speed = speed_of_ball - 0.02
        ball_speed_x = ball_speed_y = speed_of_ball
        speeder.pop(0)
        print(speed_of_ball)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player.y > 0:
        player.y -= speed
    elif keys[pygame.K_DOWN] and player.y < 350:
        player.y += speed

    if enemy.y >= ball.y and enemy.y > 0:# and ball.x > 200:
        enemy.y -= op_speed
    if enemy.y <= ball.y and enemy.y < 350:# and ball.x > 200:
        enemy.y += op_speed

def ball_move():
    global ball_speed_x,ball_speed_y,player_score,op_score

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    player_side_check = ball.left <= 0 
    op_side_check = ball.right >= 720

    if ball.bottom >= 400 or ball.top <= 0 :
        ball_speed_y *= -1
    if player_side_check or op_side_check or ball.colliderect(player) or ball.colliderect(enemy):
        ball_speed_x *= -1
    if player_side_check:
        op_score += 1
        restart(0)

    if op_side_check:
        player_score += 1
        restart(1)

    if player_score>op_score:
        color_op = green
        color = red
    elif player_score<op_score:
        color_op = red
        color = green

    else:
        color_op = color = white
    
    text = font.render(str(player_score), 10,color_op)
    text_2 = font.render(str(op_score), 10,color)

    window.blit(text,(340,0))
    window.blit(text_2,(370,0))
    
def draw():
    pygame.draw.rect(window,grey,player)
    pygame.draw.rect(window,grey,enemy)
    pygame.draw.ellipse(window,grey,ball)
    #print(player.left)
    #print(enemy.right)
            
while True:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.quit:
            pygame.quit()
            sys.exit()
        
    window.fill(black)
    pygame.draw.aaline(window,grey,(360,0),(360,720))
    control()
    ball_move()
    draw()
    pygame.display.update()
