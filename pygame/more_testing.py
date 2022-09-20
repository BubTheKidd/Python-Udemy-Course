import pygame
from pygame.locals import * # Asterisk represents 'all'


pygame.init() # Starts up the game
#------------------Game-------------------<


# Declaring Surface-Related Variables
size = width, height = (800, 800) # Not good in other languages but is fine in this case
road_width = int(width/1.6)
screen = pygame.display.set_mode(size)
roadmark_width = int(width/80)


# Applying Changes To Screen
pygame.display.update()


# Loading Game Images
ball = pygame.image.load("pygame\intro_ball.gif") # Load outside of loop to save resources
ball_location = ball.get_rect()
ball_location.center = width/2 + road_width/4, height*.8
#------<
spidey = pygame.image.load("pygame\Spider-Man-Icon.png") # Load outside of loop to save resources
spidey_location = spidey.get_rect()
spidey_location.center = width/2 - road_width/4, height*.2


# Event/Game Loop
running = True
while running:
    # Animate Other Image
    spidey_location[1] += 1 # [0] = x-coordinate, [1] = y-coordinate
    if spidey_location[1] > height: # Height is measuring from the top down???
        spidey_location[1] = -200 # Setting the location to a much higher position so it seems to loop 


    # Event Listeners
    for event in pygame.event.get(): # Things like 'keys' and 'clicks' are considered events (Like Lua...)
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in [K_a, K_LEFT]: # If key press is within Pygame's library of available keys...
                ball_location = ball_location.move([-int(road_width/2), 0]) # .move([x-coordinate, y-coordinate])
            if event.key in [K_d, K_RIGHT]:
                ball_location = ball_location.move([int(road_width/2), 0])
        

    # Drawing Graphics
    pygame.display.set_caption("Test Game")
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (50, 50, 50), (width/2 - road_width/2, 0, road_width, height))
    pygame.draw.rect(screen, (255, 240, 60), (width/2 - roadmark_width/2, 0, roadmark_width, height))
    pygame.draw.rect(screen, (255, 255, 255), (width/2 - road_width/2 + roadmark_width*2, 0, roadmark_width, height))
    pygame.draw.rect(screen, (255, 255, 255), (width/2 + road_width/2 - roadmark_width*3, 0, roadmark_width, height))
    #pygame.draw.rect(surface, (color), rect)
    # Put the graphics in the while loop so that the picture is constantly updating



    screen.blit(ball, ball_location) # Having to do with "Bit Map Images"
    screen.blit(spidey, spidey_location)
    pygame.display.update()


#------------------Game-------------------<
pygame.quit() # Closes the game