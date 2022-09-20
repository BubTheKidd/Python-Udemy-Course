# Importing and initializing Pygame
import sys, pygame
pygame.init()


# Setting up the scene and the player object
size = width, height = 600, 480
speed = [1, 1]
black = 0, 0, 0
screen = pygame.display.set_mode(size)
ball = pygame.image.load("pygame\intro_ball.gif")
ballrect = ball.get_rect()


# Loop that keeps the ball moving until user stops it
while 1:
    # If the user decides to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()


    # The ball's movement logic
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]


    # 'Animates' the window
    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()