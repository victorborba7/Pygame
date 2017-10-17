import pygame
import time
import math
import random


pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
bright_red = (200,0,0)
green = (0,255,0)
bright_green = (0,200,0)
blue = (0,0,255)

screen_width = 800
screen_height = 600


game_Display = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Asteroids')
clock = pygame.time.Clock()




def objects(thingx, thingy, radius):
    pygame.draw.circle(game_Display, (0,0,0),[thingx, thingy], radius)


def text_objects(text,font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((screen_width/2),(screen_height/2))
    screen.blit(TextSurf, TextRect)

    pygame.display.update()
    
    time.sleep(2)
    
    game_intro()


def button(msg, x, y, w, h, ic, ac, action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(game_Display, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
            
        else:
            pygame.draw.rect(game_Display, ic, (x, y, w, h))
        
    smallText = pygame.font.Font('freesansbold.ttf',20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w/2)), (y + (h/2)))
    game_Display.blit(textSurf, textRect)

def quitgame():
    pygame.quit()
    quit()


def game_intro():

    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
            
        game_Display.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects('Asteroids', largeText)
        TextRect.center = ((screen_width/2),(screen_height/2))
        game_Display.blit(TextSurf, TextRect)

        button('Play', 125, 450, 100, 50, green, bright_green, game_loop)
        button('Tutorial', 575, 450, 100, 50, red, bright_red, quitgame)

    
        pygame.display.update()
        clock.tick(15)


def game_loop():
    x = (screen_width/2)
    y = (screen_height/2)
    left = 0
    right = 0
    accelerator = 0
    rotation = 0
    ac_y = 0
    ac_x = 0
    
    thing_starty = - 100
    thing_speed = 5
    object_radius = 35
    shot_radius = 5
    thing_startx = random.randrange(0, screen_width - object_radius)
    
    space = 0
    speed_x = 0
    speed_y = 0
    st = 0
    shot_startx = 0
    shot_starty = 0
    bullets = []


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    right = True

                    
                if event.key == pygame.K_LEFT:
                    left = True
                            

                if event.key == pygame.K_UP:
                    accelerator = True

                if event.key == pygame.K_SPACE:
                    shot_starty = y - 40
                    shot_startx = x - 30
                    bullets.append([bullet, bulletRec,shot_startx, shot_starty])
                    if rotation >= 0 and rotation <= 90:
                        speed_x = math.sin(rotation*math.pi/180) * 15
                        speed_y = math.cos(rotation*math.pi/180) * 15
                    elif rotation >= 90 and rotation <= 180:
                        speed_x = math.sin(rotation*math.pi/180) * 15
                        speed_y = math.cos(rotation*math.pi/180) * 15
                    elif rotation >= 180 and rotation <= 270:
                        speed_x = math.sin(rotation*math.pi/180) * 15
                        speed_y = math.cos(rotation*math.pi/180) * 15
                    elif rotation >= 270 and rotation <= 360:
                        speed_x = math.sin(rotation*math.pi/180) * 15
                        speed_y = math.cos(rotation*math.pi/180) * 15
                    print(bullets)



            if event.type == pygame.KEYUP:
                if left and event.key == pygame.K_LEFT:
                    left = False
                    
                if right and event.key == pygame.K_RIGHT:
                    right = False
                
                if event.key == pygame.K_UP:
                    accelerator = False

                if event.key == pygame.K_SPACE:
                    space = False
                    

        if left:
            rotation += 5
            
        elif right:    
            rotation -= 5
            
        if accelerator:
            if rotation >= 0 and rotation <= 90:
                ac_x = math.sin(rotation*math.pi/180) * 3
                ac_y = math.cos(rotation*math.pi/180) * 3
            elif rotation >= 90 and rotation <= 180:
                ac_x = math.sin(rotation*math.pi/180) * 3
                ac_y = math.cos(rotation*math.pi/180) * 3
            elif rotation >= 180 and rotation <= 270:
                ac_x = math.sin(rotation*math.pi/180) * 3
                ac_y = math.cos(rotation*math.pi/180) * 3
            elif rotation >= 270 and rotation <= 360:
                ac_x = math.sin(rotation*math.pi/180) * 3
                ac_y = math.cos(rotation*math.pi/180) * 3
        else:
            if rotation >= 0 and rotation <= 90:
                ac_x = math.sin(rotation*math.pi/180) / 2
                ac_y = math.cos(rotation*math.pi/180) / 2
            elif rotation >= 90 and rotation <= 180:
                ac_x = math.sin(rotation*math.pi/180) / 2
                ac_y = math.cos(rotation*math.pi/180) / 2
            elif rotation >= 180 and rotation <= 270:
                ac_x = math.sin(rotation*math.pi/180) / 2
                ac_y = math.cos(rotation*math.pi/180) / 2
            elif rotation >= 270 and rotation <= 360:
                ac_x = math.sin(rotation*math.pi/180) / 2
                ac_y = math.cos(rotation*math.pi/180) / 2


        

        
        if x < -38:
            x = 800
        elif x > 838:
            x = 0
        elif y < -19:
            y = 619
        elif y > 619:
            y = -19
            

        if rotation >= 360:
            rotation = 0
        elif rotation < 0:
            rotation = 360
        y -= ac_y
        x -= ac_x


        
        shot_starty -= speed_y
        shot_startx -= speed_x


        game_Display.fill((255,255,255))

        bullet = pygame.image.load('Imagens/Bullet.png')
        bulletRec = bullet.get_rect()
        bulletRec.center = (shot_startx + 15, shot_starty + 20)

        if len(bullets) > 0:
            for b in bullets:
                game_Display.blit(bullet, bulletRec)
        else:
            game_Display.blit(bullet, bulletRec)

        if (shot_startx > 850 or shot_startx < -50) or (shot_starty > 650 or shot_starty < -50):
            bullets.remove[0]

        
        naveImg = pygame.image.load('Imagens/naveReserva.png')
        naveImg = pygame.transform.rotate(naveImg,rotation)
        naveImgRec = naveImg.get_rect()
        naveImgRec.center = (x-15,y-20)

        
        if thing_starty > screen_height:
            thing_starty = 0 - (object_radius*2)
            thing_startx = random.randrange(0,screen_width - object_radius)
            
        game_Display.blit(naveImg,naveImgRec)
        

        pygame.display.update()
        clock.tick(60)

game_intro()
