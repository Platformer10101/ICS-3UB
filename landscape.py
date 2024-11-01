import pygame
import random

pygame.init()

WIDTH = 1280
HEIGHT = 720
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

face_x = 0
face_y = 0
speed_x = 10
speed_y = 10
colour1 = 0
colour2 = 0
colour3 = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    face_x += speed_x
    face_y -= speed_y

    screen.fill((0, 0, 0))  # always the first drawing command
    for i in range(1,21):
        starposx = random.randrange(0,1281)
        starposy = random.randrange(0,721)
        pygame.draw.circle(screen, (255,255,255), (starposx,starposy), 5)

    pygame.draw.ellipse(screen, (0,255,0), (160,640,1000,200))
    pygame.draw.rect(screen, (232,220,202), (450,250,400,400))
    pygame.draw.polygon(screen, (176,102,96),((650,75), (450,250), (850,250)))
    pygame.draw.rect(screen, (139,69,19), ((600,500,100,150)))
    pygame.draw.rect(screen, (0,0,128), ((500,300,100,100)))
    pygame.draw.rect(screen, (0,0,128), ((700,300,100,100)))
    
    pygame.draw.ellipse(screen, (255, 255, 255), (face_x+600, face_y+320,100,100))
    pygame.draw.rect(screen, (255,255,255), (face_x+600,face_y+370,100,85))
    pygame.draw.polygon(screen, (colour1,colour2,colour3), ((face_x+635,face_y+340),(face_x+625,face_y+355),(face_x+645,face_y+355)), 0)
    pygame.draw.polygon(screen, (colour1,colour2,colour3), ((face_x+665,face_y+340),(face_x+655,face_y+355),(face_x+675,face_y+355)), 0)
    pygame.draw.polygon(screen, (colour1,colour2,colour3), ((face_x+650,face_y+385),(face_x+640,face_y+370),(face_x+660,face_y+370)), 0)
    pygame.draw.polygon(screen, (255,255,255), ((face_x+650,face_y+470),(face_x+640,face_y+455),(face_x+660,face_y+455)), 0)
    pygame.draw.polygon(screen, (255,255,255), ((face_x+670,face_y+470),(face_x+660,face_y+455),(face_x+680,face_y+455)), 0)
    pygame.draw.polygon(screen, (255,255,255), ((face_x+630,face_y+470),(face_x+620,face_y+455),(face_x+640,face_y+455)), 0)
    pygame.draw.polygon(screen, (255,255,255), ((face_x+689,face_y+470),(face_x+679,face_y+455),(face_x+699,face_y+455)), 0)
    pygame.draw.polygon(screen, (255,255,255), ((face_x+610,face_y+470),(face_x+600,face_y+455),(face_x+620,face_y+455)), 0)
    #pygame.draw.polygon(screen, (255,255,255), ((face_x+695,face_y+470),(face_x+685,face_y+455),(face_x+705,face_y+455)), 0)
    #pygame.draw.polygon(screen, (255,255,255), ((face_x+605,face_y+470),(face_x+595,face_y+455),(face_x+615,face_y+455)), 0)
    
    if face_x >= 580 or face_x <= -600:
        colour1 = random.randrange(0,226)
        colour2 = random.randrange(0,226)
        colour3 = random.randrange(0,226)
        #speed_x = random.randrange(1,21,5)
        #speed_y = random.randrange(1,21,5)
        speed_x *= -1
        speed_y *= 1
    elif face_y >= 250 or face_y <= -320:
        colour1 = random.randrange(0,226)
        colour2 = random.randrange(0,226)
        colour3 = random.randrange(0,226)
        #speed_x = random.randrange(1,21,5)
        #speed_y = random.randrange(1,21,5)
        speed_x *= 1
        speed_y *= -1
    
    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------

pygame.quit()