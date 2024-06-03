#ul 7
import pygame
import random
pygame.init()
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
lgreen = [153, 255, 153]
lblue = [153, 204, 255]
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Hiir")
screen.fill(lblue)
clock = pygame.time.Clock()
gameover = False
circles = []
max_circles = 10
circle_radius = 10
score = 0
font = pygame.font.SysFont(None, 36)
win_score = 30
while not gameover:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click = pygame.mouse.get_pos()
            for circle in circles:
                cx, cy = circle["pos"]
                if (click[0] - cx) ** 2 + (click[1] - cy) ** 2 <= circle["radius"] ** 2:
                    circles.remove(circle)
                    score += 1
                    break
    if len(circles) < max_circles:
        x = random.randint(circle_radius, screenX - circle_radius)
        y = random.randint(circle_radius, screenY - circle_radius)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = [r, g, b]
        circles.append({"pos": (x, y), "color": color, "radius": circle_radius})
    for circle in circles:
        circle["radius"] += 1
    screen.fill(lblue)
    for circle in circles:
        pygame.draw.circle(screen, circle["color"], circle["pos"], circle["radius"])
    score_text = font.render(f'Score: {score}', True, blue)
    screen.blit(score_text, [10, 10])
    if score >= win_score:
        win_text = font.render('You Win!', True, green)
        screen.blit(win_text, [screenX // 2 - 50, screenY // 2 - 20])
        pygame.display.flip()
        pygame.time.delay(3000)
        gameover = True
    pygame.display.flip()
pygame.quit()




##ul 6


#import pygame
#pygame.init()
##pygame.mixer.init()
#red = [255, 0, 0]
#blue = [135, 206, 250]
#black = [0, 0, 0]
#white = [255, 255, 255]
#width, height = 600, 600
#screen = pygame.display.set_mode((width, height))
#pygame.display.set_caption("PingPong Game")
##pygame.mixer.music.load('bgbgbg.mp3')
##pygame.mixer.music.play(-1) 
#paddle_width, paddle_height = 100, 10
#paddle_x = (width - paddle_width) // 2
#paddle_y = height - 30
#paddle_speed = 5
#ball_x, ball_y = width // 2, height // 2
#ball_speed_x, ball_speed_y = 3, 3
#ball_radius = 10
#clock = pygame.time.Clock()
#gameover = False
#while not gameover:
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            gameover = True
#    keys = pygame.key.get_pressed()
#    if keys[pygame.K_LEFT]:
#        paddle_x -= paddle_speed
#    if keys[pygame.K_RIGHT]:
#        paddle_x += paddle_speed
#    if paddle_x < 0:
#        paddle_x = 0
#    if paddle_x + paddle_width > width:
#        paddle_x = width - paddle_width
#    ball_x += ball_speed_x
#    ball_y += ball_speed_y
#    if ball_x - ball_radius < 0 or ball_x + ball_radius > width:
#        ball_speed_x = -ball_speed_x
#    if ball_y - ball_radius < 0:
#        ball_speed_y = -ball_speed_y
#    if paddle_y < ball_y + ball_radius < paddle_y + paddle_height:
#        if paddle_x < ball_x < paddle_x + paddle_width:
#            ball_speed_y = -ball_speed_y
#    if ball_y + ball_radius > height:
#        gameover = True
#    screen.fill(blue)
#    pygame.draw.rect(screen, black, [paddle_x, paddle_y, paddle_width, paddle_height])
#    pygame.draw.circle(screen, red, [ball_x, ball_y], ball_radius)
#    pygame.display.flip()
#    clock.tick(60)

#pygame.quit()