import pygame

pygame.init()
Width, Height = 600, 600

win = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Simple Game")

x, y = 300, 570
radius = 30
vel = [6, 10, 10]
global circle_x
global circle_y
circle_x, circle_y = 29, 570
moving_right = False

def move_left():
    global circle_x
    if circle_x >= 33:
        circle_x -= vel[2]
        print(circle_x)

def move_right():
    global circle_x
    if circle_x <= 30:
        moving_right = True
        while moving_right == True:
            circle_x += vel[2]
            if circle_x >= 570:
                moving_right = False
            print(circle_x)


game = True
jump = False
while game == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            game = False
    pygame.time.delay(40)
    win.fill((255, 0, 0))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and x+50 < 600:
        x += vel[0]
    if keys[pygame.K_LEFT] and x > 0:
        x -= vel[0]
    if jump is  False and keys[pygame.K_UP]:
        jump = True

    if jump is True:
        y -= vel[1] * 4
        vel[1] -= 1
        if vel[1] <- 10:
            jump = False
            vel[1] = 10
    move_left()
    move_right()
        
    pygame.draw.rect(win, (60,90,200), (x, y, 50, 25))
    pygame.draw.circle(win, (0,0,0), (circle_x, circle_y), radius)
    pygame.display.update()