'''
Game
24.08.2021
'''

# O'yin uchun PYGAME ni chaqiramiz...
import pygame
from pygame import mixer
import time
from config.colors import*
from config.object_moving import*
from config.random_num_place import rand_list
from backend.generator import r1, r2, mm1, mm2

# Oyna ochish
pygame.init()
clock = pygame.time.Clock()
fps = 60

# Oyna o'lchami
size = [500, 500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Game')

# 3 ta kerakli obyektlar
area1 = pygame.Rect(15, 20, 250, 200) # 1-Quti
area2 = pygame.Rect(15, 240, 250, 200) # 2-Quti
button = pygame.Rect(310, 430, 160, 40) # Tugma

# Jami yuklarni joylash
c_data = r1+r2

# Ikonkalarni chaqirish
img1 = pygame.image.load(f'images/nums/{c_data[0]}.png')
img1.convert()
rect1 = img1.get_rect()
rect1.center = rand_list[0]

img2 = pygame.image.load(f'images/nums/{c_data[1]}.png')
img2.convert()
rect2 = img2.get_rect()
rect2.center = rand_list[1]

img3 = pygame.image.load(f'images/nums/{c_data[2]}.png')
img3.convert()
rect3 = img3.get_rect()
rect3.center = rand_list[2]

img4 = pygame.image.load(f'images/nums/{c_data[3]}.png')
img4.convert()
rect4 = img4.get_rect()
rect4.center = rand_list[3]

img5 = pygame.image.load(f'images/nums/{c_data[4]}.png')
img5.convert()
rect5 = img5.get_rect()
rect5.center = rand_list[4]

img6 = pygame.image.load(f'images/nums/{c_data[5]}.png')
img6.convert()
rect6 = img6.get_rect()
rect6.center = rand_list[5]

img7 = pygame.image.load(f'images/nums/{c_data[6]}.png')
img7.convert()
rect7 = img7.get_rect()
rect7.center = rand_list[6]

img8 = pygame.image.load(f'images/nums/{c_data[7]}.png')
img8.convert()
rect8 = img8.get_rect()
rect8.center = rand_list[7]

img9 = pygame.image.load(f'images/nums/{c_data[8]}.png')
img9.convert()
rect9 = img9.get_rect()
rect9.center = rand_list[8]

img10 = pygame.image.load(f'images/nums/{c_data[9]}.png')
img10.convert()
rect10 = img10.get_rect()
rect10.center = rand_list[9]

c_rects = [rect1, rect2, rect3, rect4, rect5, rect6, rect7, rect8, rect9, rect10]
bg = pygame.image.load('images/wood-bg.png')

font = pygame.font.Font('freesansbold.ttf', 25)
btn_text = font.render('Tayyor', True, BLACK)
btn_textRect = btn_text.get_rect()
btn_textRect.center = (390, 450)

area1_text = font.render(f'Jami: {mm1}', True, BLACK)
area1_textRect = area1_text.get_rect()
area1_textRect.center = (70, 35)

area2_text = font.render(f'Jami: {mm2}', True, BLACK)
area2_textRect = area2_text.get_rect()
area2_textRect.center = (70, 255)

font2 = pygame.font.Font('freesansbold.ttf', 60)
win = font2.render('You Win!!!', True, GREEN)
win_textRect = win.get_rect()
win_textRect.center = (size[0]//2, size[1]//2)

lose = font2.render('Game Over:(', True, RED)
lose_textRect = lose.get_rect()
lose_textRect.center = (size[0]//2, size[1]//2)

# Sound effect
mixer.music.load("audio/effects/btn-click.wav")
mixer.music.set_volume(1)
play_audio = 1

game_over = None
# Cheksiz faol oyna
run = True
while run:
    screen.fill(WHITE)
    screen.blit(bg, (0, 0))
    
    for event in pygame.event.get():
        #print(r1, r2)
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            # Tayyor tugmasi bosilganda...
            if button.collidepoint(mouse_pos):
                r1 = []
                r2 = []
                # Yuklar qizil mayd
                for c in range(len(c_rects)):
                    cr = list(c_rects[c])
                    cc = c_data[c]
                    if cr[0] >= list(area1)[0] and cr[1] >= list(area1)[1] and cr[0] < list(area1)[0]+list(area1)[2]-cr[2] and cr[1] < list(area1)[1]+list(area1)[3]-cr[3]:
                        r1.append(cc)
                    elif list(area2)[0] and cr[1] >= list(area2)[1] and cr[0] < list(area2)[0]+list(area2)[2]-cr[2] and cr[1] < list(area2)[1]+list(area2)[3]-cr[3]:
                        r2.append(cc)
                     
                rect_locate = {"area1": r1, "area2": r2}
                r1_t = 0; r2_t = 0
                for t in rect_locate["area1"]:
                    r1_t+=t
                for tt in rect_locate["area2"]:
                    r2_t+=tt
                if r1_t == mm1 and r2_t == mm2:
                    game_over = False
                else:
                    game_over = True

            # Sonlar (yuklar bosilganda)
            if rect1.collidepoint(event.pos):
                mixer.music.play()
                m = True
            if rect2.collidepoint(event.pos):
                mixer.music.play()
                m1 = True
            if rect3.collidepoint(event.pos):
                mixer.music.play()
                m2 = True
            if rect4.collidepoint(event.pos):
                mixer.music.play()
                m3 = True
            if rect5.collidepoint(event.pos):
                mixer.music.play()
                m4 = True
            if rect6.collidepoint(event.pos):
                mixer.music.play()
                m5 = True
            if rect7.collidepoint(event.pos):
                mixer.music.play()
                m6 = True
            if rect8.collidepoint(event.pos):
                mixer.music.play()
                m7 = True
            if rect9.collidepoint(event.pos):
                mixer.music.play()
                m8 = True
            if rect10.collidepoint(event.pos):
                mixer.music.play()
                m9 = True
        elif event.type == pygame.MOUSEBUTTONUP:
            # Sichqoncha qo'yvorilganda harakatni to'xtatish
            m = False
            m1 = False
            m2 = False
            m3 = False
            m4 = False
            m5 = False
            m6 = False
            m7 = False
            m8 = False
            m9 = False

        # Sichqoncha bilan yuklarni tortib siljitish
        elif event.type == pygame.MOUSEMOTION and m:
            rect1.move_ip(event.rel)
        elif event.type == pygame.MOUSEMOTION and m1:
            rect2.move_ip(event.rel)
        elif event.type == pygame.MOUSEMOTION and m2:
            rect3.move_ip(event.rel)
        elif event.type == pygame.MOUSEMOTION and m3:
            rect4.move_ip(event.rel)
        elif event.type == pygame.MOUSEMOTION and m4:
            rect5.move_ip(event.rel)
        elif event.type == pygame.MOUSEMOTION and m5:
            rect6.move_ip(event.rel)
        elif event.type == pygame.MOUSEMOTION and m6:
            rect7.move_ip(event.rel)
        elif event.type == pygame.MOUSEMOTION and m7:
            rect8.move_ip(event.rel)
        elif event.type == pygame.MOUSEMOTION and m8:
            rect9.move_ip(event.rel)
        elif event.type == pygame.MOUSEMOTION and m9:
            rect10.move_ip(event.rel)

    # Obyektlarni yaratish 
    pygame.draw.rect(screen, RED, area1)
    pygame.draw.rect(screen, RED, area2)
    screen.blit(area1_text, area1_textRect)
    screen.blit(area2_text, area2_textRect)

    screen.blit(img1, rect1)
    pygame.draw.rect(screen, BLUE, rect1, 5)
    
    screen.blit(img2, rect2)
    pygame.draw.rect(screen, BLUE, rect2, 5)

    screen.blit(img3, rect3)
    pygame.draw.rect(screen, BLUE, rect3, 5)
    
    screen.blit(img4, rect4)
    pygame.draw.rect(screen, BLUE, rect4, 5)

    screen.blit(img5, rect5)
    pygame.draw.rect(screen, BLUE, rect5, 5)
    
    screen.blit(img6, rect6)
    pygame.draw.rect(screen, BLUE, rect6, 5)

    screen.blit(img7, rect7)
    pygame.draw.rect(screen, BLUE, rect7, 5)
    
    screen.blit(img8, rect8)
    pygame.draw.rect(screen, BLUE, rect8, 5)

    screen.blit(img9, rect9)
    pygame.draw.rect(screen, BLUE, rect9, 5)
    
    screen.blit(img10, rect10)
    pygame.draw.rect(screen, BLUE, rect10, 5)
    pygame.draw.rect(screen, BTN_COLOR, button)
    screen.blit(btn_text, btn_textRect)

    # Yutish/Yutqizish sharti
    if(game_over == None):
        pass
    elif(not game_over):
        screen.fill(AERO)
        screen.blit(win, win_textRect)
        while play_audio==1:
            mixer.music.load("audio/effects/win.wav")
            mixer.music.set_volume(1)
            mixer.music.play()
            play_audio = 0
    elif(game_over):
        screen.fill(AERO)
        screen.blit(lose, lose_textRect)
        while play_audio==1:
            mixer.music.load("audio/effects/game-over.wav")
            mixer.music.set_volume(1)
            mixer.music.play()
            play_audio = 0
            
    pygame.display.update()
    clock.tick(fps)

# O'yin tugadi
pygame.quit()
exit()