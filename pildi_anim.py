import pygame
import random

pygame.init()
#pygame.mixer.init()
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ralli")
red_car = pygame.image.load("pun.png")
yel_car = pygame.image.load("kol.png")
background = pygame.image.load("doroga.png")
scale_factor = 0.5
scale_factor2 = 0.2
red_car = pygame.transform.scale(red_car, (int(red_car.get_width() * scale_factor2), int(red_car.get_height() * scale_factor2)))
yel_car = pygame.transform.scale(yel_car, (int(yel_car.get_width() * scale_factor), int(yel_car.get_height() * scale_factor)))
red_car_speed = 5
yel_car_speed = 5
red_car_x = screen_width // 2 - red_car.get_width() // 2
red_car_y = screen_height - red_car.get_height() - 10
red_car_rect = red_car.get_rect(center=(red_car_x + red_car.get_width() // 2, red_car_y + red_car.get_height() // 2))
yel_cars = []
yel_car_rects = []
for i in range(3):
    yel_car_x = random.randint(0, screen_width - yel_car.get_width())
    yel_car_y = random.randint(-300, -100)
    yel_cars.append([yel_car_x, yel_car_y])
    yel_car_rects.append(yel_car.get_rect(topleft=(yel_car_x, yel_car_y)))
score = 0
font = pygame.font.Font(None, 36)
#pygame.mixer.music.load("music/Barely_Small.mp3")
#pygame.mixer.music.play(-1)  
#pygame.mixer.music.set_volume(0.2) 
#hit_sound = pygame.mixer.Sound("music/Hit.wav")
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and red_car_rect.left > 0:
        red_car_rect.x -= red_car_speed
    if keys[pygame.K_RIGHT] and red_car_rect.right < screen_width:
        red_car_rect.x += red_car_speed
    for i, car in enumerate(yel_cars):
        car[1] += yel_car_speed
        yel_car_rects[i].y = car[1]
        if car[1] > screen_height:
            car[1] = random.randint(-300, -100)
            car[0] = random.randint(0, screen_width - yel_car.get_width())
            yel_car_rects[i].topleft = (car[0], car[1])
            score += 10
            hit_sound.play()
        if red_car_rect.colliderect(yel_car_rects[i]):
            print("game over")
            running = False 
    screen.blit(background, (0, 0))
    screen.blit(red_car, red_car_rect.topleft)
    for car_rect in yel_car_rects:
        screen.blit(yel_car, car_rect.topleft)
    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()




#3.1. osa
#import pygame, sys
#pygame.init()

##värvid
#red = [255, 0, 0]
#green = [0, 255, 0]
#blue = [0, 0, 255]
#pink = [255, 153, 255]
#lGreen = [153, 255, 153]
#lBlue = [153, 204, 255]

##ekraani seaded
#screenX = 640
#screenY = 480
#screen=pygame.display.set_mode([screenX,screenY])
#pygame.display.set_caption("Animeerimine")
#screen.fill(lBlue)

#clock = pygame.time.Clock() #3 lisame kell
#ball = pygame.image.load("pall.png") #graafika laadimine
#posX, posY = 580, 400 #kiirus ja asukoht
#speedX = 1 #2 lisame samm

#gameover = False
#while not gameover:
#    #fps
#    clock.tick(60) #3 paus

#    #mängu sulgemine ristist
#    events = pygame.event.get()
#    for i in pygame.event.get():
#        if i.type == pygame.QUIT:
#            sys.exit()

#    #pildi lisamine ekraanile
#    screen.blit(ball, (posX,posY))
#    posX -= speedX #2 koordinaadi muutmine ehk liigub vasakule
#    #graafika kuvamine ekraanil
#    pygame.display.flip()

#pygame.quit



#pygame.init()

##värvid
#red = [255, 0, 0]
#green = [0, 255, 0]
#blue = [0, 0, 255]
#pink = [255, 153, 255]
#lGreen = [153, 255, 153]
#lBlue = [153, 204, 255]

#screenX = 640 #ekraani seaded
#screenY = 480
#screen=pygame.display.set_mode([screenX,screenY])
#pygame.display.set_caption("Animeerimine_2")
#screen.fill(lBlue)

#clock = pygame.time.Clock()
#ball = pygame.image.load("pall.png") #graafika laadimine
#posX, posY = 0, 0 #kiirus ja asukoht
#speedX, speedY = 3, 4

#gameover = False
#while not gameover:
#    clock.tick(60)
#    #mängu sulgemine ristist
#    events = pygame.event.get()
#    for i in pygame.event.get():
#        if i.type == pygame.QUIT:
#            sys.exit()

#    #pildi lisamine ekraanile
#    screen.blit(ball, (posX,posY))
#    posX += speedX
#    posY += speedY

#    #kui puudub ääri, siis muudab suunda
#    if posX > screenX-ball.get_rect().width or posX < 0:
#        speedX = -speedX

#    if posY > screenY-ball.get_rect().height or posY < 0:
#        speedY = -speedY

#    #graafika kuvamine ekraanil
#    pygame.display.flip()
#    screen.fill(lBlue)

#pygame.quit()



#pygame.init()

#red = [255, 0, 0]
#green = [0, 255, 0]
#blue = [0, 0, 255]
#pink = [255, 153, 255]
#lGreen = [153, 255, 153]
#lBlue = [153, 204, 255]

#screenX = 640
#screenY = 480
#screen=pygame.display.set_mode([screenX,screenY])
#pygame.display.set_caption("Animeerimine")
#screen.fill(lBlue)

#clock = pygame.time.Clock()
#posX, posY = 0, 0 #kiirus ja asukoht
#speedX, speedY = 3, 3
#coords = [] #koordinaatide loomine ja lisamine massiivi

#for i in range(10):
#    posX = random.randint(1,screenX)
#    posY = random.randint(1,screenY)
#    coords.append([posX, posY])

#gameover = False
#while not gameover:
#    clock.tick(120)
#    #mängu sulgemine ristist
#    events = pygame.event.get()
#    for i in pygame.event.get():
#        if i.type == pygame.QUIT:
#            sys.exit()

#    #loendist koordinaadid
#    for i in range(len(coords)):
#        pygame.draw.rect(screen, red, [coords[i][0], coords[i][1], 20, 20])
#        coords[i][1] += 1
#        if coords[i][1] > screenY: #kui jõuab alla, siis muudame ruudu alguspunkti
#            coords[i][1] = random.randint(-40, -10)
#            coords[i][0] = random.randint(0, screenX)

#    pygame.display.flip()
#    screen.fill(lBlue)

#pygame.quit()




