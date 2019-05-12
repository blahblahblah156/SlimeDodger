import pygame
import sys
import random
import time
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
pygame.mixer.init()
pygame.font.init()


class button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,display_window,outline=None):
        if outline:
            pygame.draw.rect(display_window, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(display_window, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.Font(None, 40)
            text = font.render(self.text, 1, (0,0,0))
            display_window.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False

                
def redrawWindow():
    global greenButton, pinkButton, home_img
    display_window.blit(home_img,(0,0))
    greenButton.draw(display_window,(0,0,0))
    pinkButton.draw(display_window,(0,0,0))


    
def redrawWindow1():
    global blueButton, instructions
    display_window.blit(instructions,(0,0))
    blueButton.draw(display_window,(0,0,0))

def redrawWindow3():
    global yellowButton, orangeButton
    display_window.blit(endscene,(0,0))
    orangeButton.draw(display_window,(0,0,0))
    yellowButton.draw(display_window,(0,0,0))


def main():
    global display_window, user, enemy, boss, slime, check, x_mark, laser, lives_5, lives_4, lives_3, lives_2, lives_1, dead, star
    global clock, clock1, enemy_explosion_clock, instructions, explosion, home_img, level_bg, math, enemy2, enemy3, enemy4, laser2, laser3, laser4
    global slime2, slime3, game_over, enemy_shoot_clock, enemy2_shoot_clock, enemy3_shoot_clock, boss_shoot_clock, boss2_shoot_clock
    global level1, level2, level3, level4, level5, level6, level7, count_3, count_2, count_1, count_go, bossslime, bossslime2, endscene
    
    screenHeight = 600
    screenWidth = 600
    display_window = pygame.display.set_mode((screenWidth, screenHeight))
    pygame.display.set_caption('SlimeDodger')

    load_screen = pygame.image.load('load.png')
    display_window.blit(load_screen, (0,0))
    pygame.draw.rect(display_window, (255, 0, 0), (100, 500, 400, 30))
    pygame.display.update()

    user = pygame.image.load('rocket.png')
    enemy = pygame.image.load('ufo.png')
    enemy2 = pygame.image.load('ufo2.png')
    enemy3 = pygame.image.load('ufo3.png')
    boss = pygame.image.load('boss.png')
    slime = pygame.image.load('slime.png')
    slime2 = pygame.image.load('slime2.png')
    slime3 = pygame.image.load('slime3.png')
    bossslime = pygame.image.load('bossslime.png')
    bossslime2 = pygame.image.load('bossslime2.png')
    check = pygame.image.load('checkmark.png')
    pygame.draw.rect(display_window, (25, 255, 25), (100, 500, 80, 30))
    pygame.time.delay(500)
    pygame.display.update()
    
    laser = laser2 = laser3 = laser4 = pygame.image.load('laser.png')
    lives_5 = pygame.image.load('lives_5.png')
    lives_4 = pygame.image.load('lives_4.png')
    lives_3 = pygame.image.load('lives_3.png')
    x_mark = pygame.image.load('x_mark.png')
    count_1 = pygame.image.load('count_1.png')
    count_2 = pygame.image.load('count_2.png')
    count_3 = pygame.image.load('count_3.png')
    count_go = pygame.image.load('count_go.png')
    pygame.draw.rect(display_window, (25, 255, 25), (100, 500, 160, 30))
    pygame.time.delay(500)
    pygame.display.update()
    
    lives_2 = pygame.image.load('lives_2.png')
    lives_1 = pygame.image.load('lives_1.png')
    game_over = pygame.image.load('game_over.jpg')
    star = pygame.image.load('star.png')
    instructions = pygame.image.load('instructions.png')
    endscene = pygame.image.load('endscene.png')
    pygame.draw.rect(display_window, (25, 255, 25), (100, 500, 240, 30))
    pygame.time.delay(500)
    pygame.display.update()
    
    explosion = pygame.image.load('explosion.png')
    home_img = pygame.image.load('home.png')
    level_bg = pygame.image.load('level.png')
    pygame.draw.rect(display_window, (25, 255, 25), (100, 500, 320, 30))
    pygame.time.delay(500)
    pygame.display.update()
    
    home_img = pygame.image.load('home.png')
    level_bg = pygame.image.load('level.png')
    math = pygame.image.load('math.png')
    level1 = pygame.image.load('level1.png')
    level2 = pygame.image.load('level2.png')
    level3 = pygame.image.load('level3.png')
    level4 = pygame.image.load('level4.png')
    level5 = pygame.image.load('level5.png')
    level6 = pygame.image.load('level6.png')
    level7 = pygame.image.load('level7.png')
    pygame.draw.rect(display_window, (25, 255, 25), (100, 500, 400, 30))
    pygame.time.delay(500)
    pygame.display.update()
    
    pygame.time.delay(500)
    clock = pygame.time.Clock()
    clock1 = pygame.time.Clock()
    enemy_explosion_clock = pygame.time.Clock()
    enemy_shoot_clock = pygame.time.Clock()
    enemy2_shoot_clock = pygame.time.Clock()
    enemy3_shoot_clock = pygame.time.Clock()
    boss_shoot_clock = pygame.time.Clock()
    boss2_shoot_clock = pygame.time.Clock()
    
    home()



def home():
    global instructions, blueButton, pinkButton, greenButton, display_window, home_img, lives, hit, level_num, speed, enemy_speed, kill_count, enemy_dir, enemyhp, enemy2hp, enemy3hp
    global userx, usery, enemyx, enemy2x, enemy3x, enemy_resx, enemyy, enemy2y, enemy3y, enemyresy, laserx, lasery, slimex, slimey, enemy_shoot_time, enemy_move_c, bosshp
    global slime2x, slime3x, bosslimex, enemyx, slime2, enemy2, enemy3, slime3, bossslimex, bossslimey, bossslime, enemy_move_2, enemy_move_3, boss_move, enemy2_dir, enemy3_dir, boss_dir
    global enemy2_shoot_time, enemy3_shoot_time, boss_shoot_time, slime2y, slime3y, enemyalive, enemy2alive, enemy3alive, bossalive, bossx, bossy, slimespeed, laserspeed
    global bossslime2x, bossslime2y, boss_speed, boss2_shoot_time
    display_window.blit(home_img, (0,0))
    pygame.display.update()
    
    lives = 5
    run = True
    inst = 0
    hit = False
    greenButton = button((0,255,0),25,450,250,100,'Play')
    pinkButton = button((255,0,255),325,450,250,100,'Instructions')
    blueButton = button((0,0,255),25,500,200,80,'Back')

    userx = random.randint(10, 542)
    usery = 450
    enemyx = random.randint(110, 442)
    enemy2x = random.randint(110, 442)
    enemy3x = random.randint(110, 442)
    enemy_resx = random.randint(110, 442)
    bossx = random.randint(110, 337)
    enemyy = enemy2y = enemy3y = bossy = enemy_resy = 40
    laserx = userx + 22
    lasery = usery + 35
    slimex = enemyx + 30
    slimey = enemyy + 35
    slime2x = enemy2x + 30
    slime2y = enemy2x + 35
    slime3x = enemy3x + 30
    slime3y = enemy3y + 35
    bossslimex = bossx + 50
    bossslimey = bossy + 35
    bossslime2x = bossx + 130
    bossslime2y = bossy + 35
    speed = 3
    enemy_speed = 1
    boss_speed = 0.5
    enemy_shoot_time = enemy2_shoot_time = enemy3_shoot_time = boss_shoot_time = boss2_shoot_time = 0
    kill_count = 0
    enemy_move_c = enemy_move_2 = enemy_move_3 = boss_move= 0
    enemy_dir = enemy2_dir = enemy3_dir = boss_dir= 1
    enemyhp = 2
    enemy2hp = 2
    enemy3hp = 2
    bosshp = 15
    enemyalive = True
    enemy2alive = True
    enemy3alive = True
    bossalive = True
    slimespeed = 2
    laserspeed = 6
    
    while run == True:
        pygame.mixer.music.load('home_music.mp3')
        pygame.mixer.music.play(-1)
        level_num = 0
        if inst == 0:
            redrawWindow()
        pygame.display.update()
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                run = False
                pygame.quit(); sys.exit();
            if event.type == pygame.MOUSEBUTTONDOWN:
                if greenButton.isOver(pos) and inst == 0:
                    ############################################################hello weird
                    level_num = 1
                    end_scene()
                elif pinkButton.isOver(pos):
                    inst = 1
                    redrawWindow1()
                    pygame.display.update()
                elif blueButton.isOver(pos):
                    display_window.blit(home_img,(0,0))
                    inst = 0
                else:
                    pass
    
def countdown():
    global level_num, level_bg, level1, level2, level3, level4, level5, level6, level7, count_1, count_2, count_3, count_go, display_window

    display_window.blit(level_bg,(0,0))
    if level_num == 1:
        display_window.blit(level1,(200,50))
    elif level_num == 2:
        display_window.blit(level2,(200,50))
    elif level_num == 3:
        display_window.blit(level3,(200,50))
    elif level_num == 4:
        display_window.blit(level4,(200,50))
    elif level_num == 5:
        display_window.blit(level5,(200,50))
    elif level_num == 6:
        display_window.blit(level6,(200,50))
    elif level_num == 7:
        display_window.blit(level7,(200,50))
    pygame.display.update()
    pygame.time.delay(500)
    
    display_window.blit(level_bg,(0,0))
    if level_num == 1:
        display_window.blit(level1,(200,50))
    elif level_num == 2:
        display_window.blit(level2,(200,50))
    elif level_num == 3:
        display_window.blit(level3,(200,50))
    elif level_num == 4:
        display_window.blit(level4,(200,50))
    elif level_num == 5:
        display_window.blit(level5,(200,50))
    elif level_num == 6:
        display_window.blit(level6,(200,50))
    elif level_num == 7:
        display_window.blit(level7,(200,50))
    display_window.blit(count_3, (250,350))
    pygame.display.update()
    pygame.time.delay(1000)
    
    display_window.blit(level_bg,(0,0))
    if level_num == 1:
        display_window.blit(level1,(200,50))
    elif level_num == 2:
        display_window.blit(level2,(200,50))
    elif level_num == 3:
        display_window.blit(level3,(200,50))
    elif level_num == 4:
        display_window.blit(level4,(200,50))
    elif level_num == 5:
        display_window.blit(level5,(200,50))
    elif level_num == 6:
        display_window.blit(level6,(200,50))
    elif level_num == 7:
        display_window.blit(level7,(200,50))
    display_window.blit(count_2, (250,350))
    pygame.display.update()
    pygame.time.delay(1000)

    display_window.blit(level_bg,(0,0))
    if level_num == 1:
        display_window.blit(level1,(200,50))
    elif level_num == 2:
        display_window.blit(level2,(200,50))
    elif level_num == 3:
        display_window.blit(level3,(200,50))
    elif level_num == 4:
        display_window.blit(level4,(200,50))
    elif level_num == 5:
        display_window.blit(level5,(200,50))
    elif level_num == 6:
        display_window.blit(level6,(200,50))
    elif level_num == 7:
        display_window.blit(level7,(200,50))
    display_window.blit(count_1, (250,350))
    pygame.display.update()
    pygame.time.delay(1000)

    display_window.blit(level_bg,(0,0))
    if level_num == 1:
        display_window.blit(level1,(200,50))
    elif level_num == 2:
        display_window.blit(level2,(200,50))
    elif level_num == 3:
        display_window.blit(level3,(200,50))
    elif level_num == 4:
        display_window.blit(level4,(200,50))
    elif level_num == 5:
        display_window.blit(level5,(200,50))
    elif level_num == 6:
        display_window.blit(level6,(200,50))
    elif level_num == 7:
        display_window.blit(level7,(200,50))
    display_window.blit(count_go, (225,350))
    pygame.display.update()
    pygame.time.delay(1000)
    


def left():
    global speed, laserx, level_num, slime, slimex, slimey, enemy, enemyx, enemyy, laser, laserx, lasery, enemy2, enemy2x, enemy2y, display_window
    global user, userx, usery, lives, lives_5, lives_4, lives_3, lives_2, lives_1, level_bg, slime2x, slime2y, slime2, enemyalive, enemy2alive, enemy3alive, bossalive
    global bossslime, bossslimex, bossslimey, bossslime2, bossslime2x, bossslime2y, bossx, bossy, boss, slime3, slime3x, slime3y
    
    if userx - speed < 10:
        pass
    else:
        if laserx == userx + 22 and lasery == usery + 35:
            laserx -= 3
        userx -= 3

        if lasery != usery + 35:
            lasery -= 1
        if slimey != enemyy + 35:
            slimey += 1
        if slime2y != enemy2y + 35:
            slime2y += 1
        if slime3y != enemy3y + 35:
            slime3y += 1
        if bossslimey != bossy + 35:
            bossslimey += 1
        if bossslime2y != bossy + 35:
            bossslime2y += 1

    
    if level_num == 1:
        display_window.blit(level_bg,(0,0))
        if lives == 5:
            display_window.blit(lives_5,(440,10))
        if lives == 4:
            display_window.blit(lives_4,(470,10))
        if lives == 3:
            display_window.blit(lives_3,(500,10))
        if lives == 2:
            display_window.blit(lives_2,(530,10))
        if lives == 1:
            display_window.blit(lives_1,(560,10))
        display_window.blit(slime, (slimex, slimey))
        display_window.blit(enemy, (enemyx, enemyy))
        display_window.blit(laser, (laserx, lasery))
        display_window.blit(user, (userx, usery))
        pygame.display.update()
    elif level_num == 2:
        display_window.blit(level_bg,(0,0))
        if lives == 5:
            display_window.blit(lives_5,(440,10))
        if lives == 4:
            display_window.blit(lives_4,(470,10))
        if lives == 3:
            display_window.blit(lives_3,(500,10))
        if lives == 2:
            display_window.blit(lives_2,(530,10))
        if lives == 1:
            display_window.blit(lives_1,(560,10))
        if enemyalive == True:
            display_window.blit(slime, (slimex, slimey))
            display_window.blit(enemy, (enemyx, enemyy))
        if enemy2alive == True:
            display_window.blit(slime2, (slime2x, slime2y))
            display_window.blit(enemy2, (enemy2x, enemy2y))
        display_window.blit(laser, (laserx, lasery))
        display_window.blit(user, (userx, usery))
        pygame.display.update()
    elif level_num == 3:
        display_window.blit(level_bg,(0,0))
        if lives == 5:
            display_window.blit(lives_5,(440,10))
        if lives == 4:
            display_window.blit(lives_4,(470,10))
        if lives == 3:
            display_window.blit(lives_3,(500,10))
        if lives == 2:
            display_window.blit(lives_2,(530,10))
        if lives == 1:
            display_window.blit(lives_1,(560,10))
        if enemyalive == True:
            display_window.blit(slime, (slimex, slimey))
            display_window.blit(enemy, (enemyx, enemyy))
        if enemy2alive == True:
            display_window.blit(slime2, (slime2x, slime2y))
            display_window.blit(enemy2, (enemy2x, enemy2y))
        if enemy3alive == True:
            display_window.blit(slime3, (slime3x, slime3y))
            display_window.blit(enemy3, (enemy3x, enemy3y))
        display_window.blit(laser, (laserx, lasery))
        display_window.blit(user, (userx, usery))
        pygame.display.update()
    elif level_num == 4:
        display_window.blit(level_bg,(0,0))
        if lives == 5:
            display_window.blit(lives_5,(440,10))
        if lives == 4:
            display_window.blit(lives_4,(470,10))
        if lives == 3:
            display_window.blit(lives_3,(500,10))
        if lives == 2:
            display_window.blit(lives_2,(530,10))
        if lives == 1:
            display_window.blit(lives_1,(560,10))
        if bossalive == True:
            display_window.blit(bossslime, (bossslimex, bossslimey))
            display_window.blit(bossslime2, (bossslime2x, bossslime2y))
            display_window.blit(boss, (bossx, bossy))
        display_window.blit(laser, (laserx, lasery))
        display_window.blit(user, (userx, usery))
        pygame.display.update()
    elif level_num == 5:
        display_window.blit(level_bg,(0,0))
        if lives == 5:
            display_window.blit(lives_5,(440,10))
        if lives == 4:
            display_window.blit(lives_4,(470,10))
        if lives == 3:
            display_window.blit(lives_3,(500,10))
        if lives == 2:
            display_window.blit(lives_2,(530,10))
        if lives == 1:
            display_window.blit(lives_1,(560,10))
        if enemyalive == True:
            display_window.blit(slime, (slimex, slimey))
            display_window.blit(enemy, (enemyx, enemyy))
        if bossalive == True:
            display_window.blit(bossslime, (bossslimex, bossslimey))
            display_window.blit(bossslime2, (bossslime2x, bossslime2y))
            display_window.blit(boss, (bossx, bossy))
        display_window.blit(laser, (laserx, lasery))
        display_window.blit(user, (userx, usery))
        pygame.display.update()
    elif level_num == 6:
        display_window.blit(level_bg,(0,0))
        if lives == 5:
            display_window.blit(lives_5,(440,10))
        if lives == 4:
            display_window.blit(lives_4,(470,10))
        if lives == 3:
            display_window.blit(lives_3,(500,10))
        if lives == 2:
            display_window.blit(lives_2,(530,10))
        if lives == 1:
            display_window.blit(lives_1,(560,10))
        if enemyalive == True:
            display_window.blit(slime, (slimex, slimey))
            display_window.blit(enemy, (enemyx, enemyy))
        if enemy2alive == True:
            display_window.blit(slime2, (slime2x, slime2y))
            display_window.blit(enemy2, (enemy2x, enemy2y))
        if bossalive == True:
            display_window.blit(bossslime, (bossslimex, bossslimey))
            display_window.blit(bossslime2, (bossslime2x, bossslime2y))
            display_window.blit(boss, (bossx, bossy))
        display_window.blit(laser, (laserx, lasery))
        display_window.blit(user, (userx, usery))
        pygame.display.update()
    elif level_num == 7:
        display_window.blit(level_bg,(0,0))
        if lives == 5:
            display_window.blit(lives_5,(440,10))
        if lives == 4:
            display_window.blit(lives_4,(470,10))
        if lives == 3:
            display_window.blit(lives_3,(500,10))
        if lives == 2:
            display_window.blit(lives_2,(530,10))
        if lives == 1:
            display_window.blit(lives_1,(560,10))
        if enemyalive == True:
            display_window.blit(slime, (slimex, slimey))
            display_window.blit(enemy, (enemyx, enemyy))
        if enemy2alive == True:
            display_window.blit(slime2, (slime2x, slime2y))
            display_window.blit(enemy2, (enemy2x, enemy2y))
        if enemy3alive == True:
            display_window.blit(slime3, (slime3x, slime3y))
            display_window.blit(enemy3, (enemy3x, enemy3y))
        if bossalive == True:
            display_window.blit(bossslime, (bossslimex, bossslimey))
            display_window.blit(bossslime2, (bossslime2x, bossslime2y))
            display_window.blit(boss, (bossx, bossy))
        display_window.blit(laser, (laserx, lasery))
        display_window.blit(user, (userx, usery))
        pygame.display.update()
    
def right():
    global speed, laserx, level_num, slime, slimex, slimey, enemy, enemyx, enemyy, laser, laserx, lasery, enemy2, enemy2x, enemy2y, display_window
    global user, userx, usery, lives, lives_5, lives_4, lives_3, lives_2, lives_1, level_bg, slime2x, slime2y, slime2, enemyalive, enemy2alive, enemy3alive, bossalive
    global bossslime, bossslimex, bossslimey, bossslime2, bossslime2x, bossslime2y, bossx, bossy, boss, slime3, slime3x, slime3y
    
    if userx + speed > 542:
        pass
    else:
        if laserx == userx + 22 and lasery == usery + 35:
            laserx += 3
        userx += 3

        if lasery != usery + 35:
            lasery -= 1
        if slimey != enemyy + 35:
            slimey += 1
        if slime2y != enemy2y + 35:
            slime2y += 1
        if slime3y != enemy3y + 35:
            slime3y += 1
        if bossslimey != bossy + 35:
            bossslimey += 1
        if bossslime2y != bossy + 35:
            bossslime2y += 1

            
    if level_num == 1:
        display_window.blit(level_bg,(0,0))
        if lives == 5:
            display_window.blit(lives_5,(440,10))
        if lives == 4:
            display_window.blit(lives_4,(470,10))
        if lives == 3:
            display_window.blit(lives_3,(500,10))
        if lives == 2:
            display_window.blit(lives_2,(530,10))
        if lives == 1:
            display_window.blit(lives_1,(560,10))
        display_window.blit(slime, (slimex, slimey))
        display_window.blit(enemy, (enemyx, enemyy))
        display_window.blit(laser, (laserx, lasery))
        display_window.blit(user, (userx, usery))
        pygame.display.update()
    elif level_num == 2:
        display_window.blit(level_bg,(0,0))
        if lives == 5:
            display_window.blit(lives_5,(440,10))
        if lives == 4:
            display_window.blit(lives_4,(470,10))
        if lives == 3:
            display_window.blit(lives_3,(500,10))
        if lives == 2:
            display_window.blit(lives_2,(530,10))
        if lives == 1:
            display_window.blit(lives_1,(560,10))
        if enemyalive == True:
            display_window.blit(slime, (slimex, slimey))
            display_window.blit(enemy, (enemyx, enemyy))
        if enemy2alive == True:
            display_window.blit(slime2, (slime2x, slime2y))
            display_window.blit(enemy2, (enemy2x, enemy2y))
        display_window.blit(laser, (laserx, lasery))
        display_window.blit(user, (userx, usery))
        pygame.display.update()
    elif level_num == 3:
        display_window.blit(level_bg,(0,0))
        if lives == 5:
            display_window.blit(lives_5,(440,10))
        if lives == 4:
            display_window.blit(lives_4,(470,10))
        if lives == 3:
            display_window.blit(lives_3,(500,10))
        if lives == 2:
            display_window.blit(lives_2,(530,10))
        if lives == 1:
            display_window.blit(lives_1,(560,10))
        if enemyalive == True:
            display_window.blit(slime, (slimex, slimey))
            display_window.blit(enemy, (enemyx, enemyy))
        if enemy2alive == True:
            display_window.blit(slime2, (slime2x, slime2y))
            display_window.blit(enemy2, (enemy2x, enemy2y))
        if enemy3alive == True:
            display_window.blit(slime3, (slime3x, slime3y))
            display_window.blit(enemy3, (enemy3x, enemy3y))
        display_window.blit(laser, (laserx, lasery))
        display_window.blit(user, (userx, usery))
        pygame.display.update()
    elif level_num == 4:
        display_window.blit(level_bg,(0,0))
        if lives == 5:
            display_window.blit(lives_5,(440,10))
        if lives == 4:
            display_window.blit(lives_4,(470,10))
        if lives == 3:
            display_window.blit(lives_3,(500,10))
        if lives == 2:
            display_window.blit(lives_2,(530,10))
        if lives == 1:
            display_window.blit(lives_1,(560,10))
        if bossalive == True:
            display_window.blit(bossslime, (bossslimex, bossslimey))
            display_window.blit(bossslime2, (bossslime2x, bossslime2y))
            display_window.blit(boss, (bossx, bossy))
        display_window.blit(laser, (laserx, lasery))
        display_window.blit(user, (userx, usery))
        pygame.display.update()
    elif level_num == 5:
        display_window.blit(level_bg,(0,0))
        if lives == 5:
            display_window.blit(lives_5,(440,10))
        if lives == 4:
            display_window.blit(lives_4,(470,10))
        if lives == 3:
            display_window.blit(lives_3,(500,10))
        if lives == 2:
            display_window.blit(lives_2,(530,10))
        if lives == 1:
            display_window.blit(lives_1,(560,10))
        if enemyalive == True:
            display_window.blit(slime, (slimex, slimey))
            display_window.blit(enemy, (enemyx, enemyy))
        if bossalive == True:
            display_window.blit(bossslime, (bossslimex, bossslimey))
            display_window.blit(bossslime2, (bossslime2x, bossslime2y))
            display_window.blit(boss, (bossx, bossy))
        display_window.blit(laser, (laserx, lasery))
        display_window.blit(user, (userx, usery))
        pygame.display.update()
    elif level_num == 6:
        display_window.blit(level_bg,(0,0))
        if lives == 5:
            display_window.blit(lives_5,(440,10))
        if lives == 4:
            display_window.blit(lives_4,(470,10))
        if lives == 3:
            display_window.blit(lives_3,(500,10))
        if lives == 2:
            display_window.blit(lives_2,(530,10))
        if lives == 1:
            display_window.blit(lives_1,(560,10))
        if enemyalive == True:
            display_window.blit(slime, (slimex, slimey))
            display_window.blit(enemy, (enemyx, enemyy))
        if enemy2alive == True:
            display_window.blit(slime2, (slime2x, slime2y))
            display_window.blit(enemy2, (enemy2x, enemy2y))
        if bossalive == True:
            display_window.blit(bossslime, (bossslimex, bossslimey))
            display_window.blit(bossslime2, (bossslime2x, bossslime2y))
            display_window.blit(boss, (bossx, bossy))
        display_window.blit(laser, (laserx, lasery))
        display_window.blit(user, (userx, usery))
        pygame.display.update()
    elif level_num == 7:
        display_window.blit(level_bg,(0,0))
        if lives == 5:
            display_window.blit(lives_5,(440,10))
        if lives == 4:
            display_window.blit(lives_4,(470,10))
        if lives == 3:
            display_window.blit(lives_3,(500,10))
        if lives == 2:
            display_window.blit(lives_2,(530,10))
        if lives == 1:
            display_window.blit(lives_1,(560,10))
        if enemyalive == True:
            display_window.blit(slime, (slimex, slimey))
            display_window.blit(enemy, (enemyx, enemyy))
        if enemy2alive == True:
            display_window.blit(slime2, (slime2x, slime2y))
            display_window.blit(enemy2, (enemy2x, enemy2y))
        if enemy3alive == True:
            display_window.blit(slime3, (slime3x, slime3y))
            display_window.blit(enemy3, (enemy3x, enemy3y))
        if bossalive == True:
            display_window.blit(bossslime, (bossslimex, bossslimey))
            display_window.blit(bossslime2, (bossslime2x, bossslime2y))
            display_window.blit(boss, (bossx, bossy))
        display_window.blit(laser, (laserx, lasery))
        display_window.blit(user, (userx, usery))
        pygame.display.update()


    
def shoot():
    global speed, laserx, level_num, slime, slimex, slimey, enemy, enemyx, enemyy, laser, laserx, lasery, enemy2, enemy2x, enemy2y, display_window
    global user, userx, usery, lives, lives_5, lives_4, lives_3, lives_2, lives_1, level_bg, slime2x, slime2y, slime2, enemyalive, enemy2alive, enemy3alive, bossalive
    global bossslime, bossslimex, bossslimey, bossslime2, bossslime2x, bossslime2y, bossx, bossy, boss
    
    if lasery == usery + 35:
        lasery -= 1

        if level_num == 1:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            display_window.blit(slime, (slimex, slimey))
            display_window.blit(enemy, (enemyx, enemyy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
        elif level_num == 2:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
        elif level_num == 3:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if enemy3alive == True:
                display_window.blit(slime3, (slime3x, slime3y))
                display_window.blit(enemy3, (enemy3x, enemy3y))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
        elif level_num == 4:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
        elif level_num == 5:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
        elif level_num == 6:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
        elif level_num == 7:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if enemy3alive == True:
                display_window.blit(slime3, (slime3x, slime3y))
                display_window.blit(enemy3, (enemy3x, enemy3y))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()



def enemy_movement():
    global speed, laserx, level_num, slime, slimex, slimey, enemy, enemyx, enemyy, laser, laserx, lasery, slime2x, slime2y, slime2, enemy_move_2, enemy_move_3, boss_move, display_window
    global user, userx, usery, lives, lives_5, lives_4, lives_3, lives_2, lives_1, level_bg, enemy_move_c, enemy_dir, enemy2, enemy2x, enemy2y, enemy2_dir, enemy3_dir, boss_dir
    global enemyalive, enemy2alive, enemy3alive, bossalive, enemy3, enemy3x, enemy3y, bossx, boss, bossy, bossslimex, bossslimey, bossslime, slime3, slime3x, slime3y
    global bossslime2, bossslime2x, bossslime2y
    #enemy*************************************
    if enemy_move_c == 0 and enemyalive == True:
        enemy_dir = random.randint(1,2)
        
    if enemy_dir == 1 and enemyx <= 447:
        enemyx += enemy_speed
        if slimey == enemyy + 35:
            slimex += enemy_speed
        enemy_move_c += 1
        if enemy_move_c >= 60:
            enemy_move_c = 0
            
    elif enemy_dir == 2 and enemyx >= 10:
        enemyx -= enemy_speed
        if slimey == enemyy + 35:
            slimex -= enemy_speed
        enemy_move_c += 1
        if enemy_move_c >= 60:
            enemy_move_c = 0
            
    else:
        enemy_move_c += 1
        if enemy_dir == 1:
            enemy_dir = 2
        else:
            enemy_dir = 1
            
    if enemy_move_c >= 60:
        enemy_move_c = 0

    #enemy2********************************************
    if level_num >= 2 and enemy2alive == True:
        if enemy_move_2 == 0:
            enemy2_dir = random.randint(1,2)
            
        if enemy2_dir == 1 and enemy2x <= 447:
            enemy2x += enemy_speed
            if slime2y == enemy2y + 35:
                slime2x += enemy_speed
            enemy_move_2 += 1
            if enemy_move_2 >= 60:
                enemy_move_2 = 0
                
        elif enemy2_dir == 2 and enemy2x >= 10:
            enemy2x -= enemy_speed
            if slime2y == enemy2y + 35:
                slime2x -= enemy_speed
            enemy_move_2 += 1
            if enemy_move_2 >= 60:
                enemy_move_2 = 0
                
        else:
            enemy_move_2 += 1
            if enemy2_dir == 1:
                enemy2_dir = 2
            else:
                enemy2_dir = 1
                
        if enemy_move_2 >= 60:
            enemy_move_2 = 0

    #enemy3********************************************
    if level_num >= 3 and enemy3alive == True:
        if enemy_move_3 == 0:
            enemy3_dir = random.randint(1,2)
            
        if enemy3_dir == 1 and enemy3x <= 447:
            enemy3x += enemy_speed
            if slime3y == enemy3y + 35:
                slime3x += enemy_speed
            enemy_move_3 += 1
            if enemy_move_3 >= 60:
                enemy_move_3 = 0
                
        elif enemy3_dir == 2 and enemy3x >= 10:
            enemy3x -= enemy_speed
            if slime3y == enemy3y + 35:
                slime3x -= enemy_speed
            enemy_move_3 += 1
            if enemy_move_3 >= 60:
                enemy_move_3 = 0
                
        else:
            enemy_move_3 += 1
            if enemy3_dir == 1:
                enemy3_dir = 2
            else:
                enemy3_dir = 1
                
        if enemy_move_3 >= 60:
            enemy_move_3 = 0
            
    #boss********************************************
    if level_num >= 4 and bossalive == True:
        if boss_move == 0:
            boss_dir = random.randint(1,2)
            
        if boss_dir == 1 and bossx <= 342:
            bossx += enemy_speed
            if bossslimey == bossslimey + 35:
                bossslimex += enemy_speed
            if bossslime2y == bossslime2y + 35:
                bossslime2x += enemy_speed
            boss_move += 1
            if boss_move >= 60:
                boss_move = 0
                
        elif boss_dir == 2 and bossx >= 10:
            bossx -= enemy_speed
            if bossslimey == bossslimey + 35:
                bossslimex -= enemy_speed
            if bossslime2y == bossslime2y + 35:
                bossslime2x -= enemy_speed
            boss_move += 1
            if boss_move >= 60:
                boss_move = 0
                
        else:
            boss_move += 1
            if boss_dir == 1:
                boss_dir = 2
            else:
                boss_dir = 1
                
        if boss_move >= 60:
            boss_move = 0

    if level_num == 1:    
        display_window.blit(level_bg,(0,0))
        if lives == 5:
            display_window.blit(lives_5,(440,10))
        if lives == 4:
            display_window.blit(lives_4,(470,10))
        if lives == 3:
            display_window.blit(lives_3,(500,10))
        if lives == 2:
            display_window.blit(lives_2,(530,10))
        if lives == 1:
            display_window.blit(lives_1,(560,10))
        display_window.blit(slime, (slimex, slimey))
        display_window.blit(enemy, (enemyx, enemyy))
        display_window.blit(laser, (laserx, lasery))
        display_window.blit(user, (userx, usery))
        pygame.display.update()
    elif level_num == 2:
        display_window.blit(level_bg,(0,0))
        if lives == 5:
            display_window.blit(lives_5,(440,10))
        if lives == 4:
            display_window.blit(lives_4,(470,10))
        if lives == 3:
            display_window.blit(lives_3,(500,10))
        if lives == 2:
            display_window.blit(lives_2,(530,10))
        if lives == 1:
            display_window.blit(lives_1,(560,10))
        if enemyalive == True:
            display_window.blit(slime, (slimex, slimey))
            display_window.blit(enemy, (enemyx, enemyy))
        if enemy2alive == True:
            display_window.blit(slime2, (slime2x, slime2y))
            display_window.blit(enemy2, (enemy2x, enemy2y))
        display_window.blit(laser, (laserx, lasery))
        display_window.blit(user, (userx, usery))
        pygame.display.update()
    elif level_num == 3:
        display_window.blit(level_bg,(0,0))
        if lives == 5:
            display_window.blit(lives_5,(440,10))
        if lives == 4:
            display_window.blit(lives_4,(470,10))
        if lives == 3:
            display_window.blit(lives_3,(500,10))
        if lives == 2:
            display_window.blit(lives_2,(530,10))
        if lives == 1:
            display_window.blit(lives_1,(560,10))
        if enemyalive == True:
            display_window.blit(slime, (slimex, slimey))
            display_window.blit(enemy, (enemyx, enemyy))
        if enemy2alive == True:
            display_window.blit(slime2, (slime2x, slime2y))
            display_window.blit(enemy2, (enemy2x, enemy2y))
        if enemy3alive == True:
            display_window.blit(slime3, (slime3x, slime3y))
            display_window.blit(enemy3, (enemy3x, enemy3y))
        display_window.blit(laser, (laserx, lasery))
        display_window.blit(user, (userx, usery))
        pygame.display.update()
    elif level_num == 4:
        display_window.blit(level_bg,(0,0))
        if lives == 5:
            display_window.blit(lives_5,(440,10))
        if lives == 4:
            display_window.blit(lives_4,(470,10))
        if lives == 3:
            display_window.blit(lives_3,(500,10))
        if lives == 2:
            display_window.blit(lives_2,(530,10))
        if lives == 1:
            display_window.blit(lives_1,(560,10))
        if bossalive == True:
            display_window.blit(bossslime, (bossslimex, bossslimey))
            display_window.blit(bossslime2, (bossslime2x, bossslime2y))
            display_window.blit(boss, (bossx, bossy))
        display_window.blit(laser, (laserx, lasery))
        display_window.blit(user, (userx, usery))
        pygame.display.update()
    elif level_num == 5:
        display_window.blit(level_bg,(0,0))
        if lives == 5:
            display_window.blit(lives_5,(440,10))
        if lives == 4:
            display_window.blit(lives_4,(470,10))
        if lives == 3:
            display_window.blit(lives_3,(500,10))
        if lives == 2:
            display_window.blit(lives_2,(530,10))
        if lives == 1:
            display_window.blit(lives_1,(560,10))
        if enemyalive == True:
            display_window.blit(slime, (slimex, slimey))
            display_window.blit(enemy, (enemyx, enemyy))
        if bossalive == True:
            display_window.blit(bossslime, (bossslimex, bossslimey))
            display_window.blit(bossslime2, (bossslime2x, bossslime2y))
            display_window.blit(boss, (bossx, bossy))
        display_window.blit(laser, (laserx, lasery))
        display_window.blit(user, (userx, usery))
        pygame.display.update()
    elif level_num == 6:
        display_window.blit(level_bg,(0,0))
        if lives == 5:
            display_window.blit(lives_5,(440,10))
        if lives == 4:
            display_window.blit(lives_4,(470,10))
        if lives == 3:
            display_window.blit(lives_3,(500,10))
        if lives == 2:
            display_window.blit(lives_2,(530,10))
        if lives == 1:
            display_window.blit(lives_1,(560,10))
        if enemyalive == True:
            display_window.blit(slime, (slimex, slimey))
            display_window.blit(enemy, (enemyx, enemyy))
        if enemy2alive == True:
            display_window.blit(slime2, (slime2x, slime2y))
            display_window.blit(enemy2, (enemy2x, enemy2y))
        if bossalive == True:
            display_window.blit(bossslime, (bossslimex, bossslimey))
            display_window.blit(bossslime2, (bossslime2x, bossslime2y))
            display_window.blit(boss, (bossx, bossy))
        display_window.blit(laser, (laserx, lasery))
        display_window.blit(user, (userx, usery))
        pygame.display.update()
    elif level_num == 7:
        display_window.blit(level_bg,(0,0))
        if lives == 5:
            display_window.blit(lives_5,(440,10))
        if lives == 4:
            display_window.blit(lives_4,(470,10))
        if lives == 3:
            display_window.blit(lives_3,(500,10))
        if lives == 2:
            display_window.blit(lives_2,(530,10))
        if lives == 1:
            display_window.blit(lives_1,(560,10))
        if enemyalive == True:
            display_window.blit(slime, (slimex, slimey))
            display_window.blit(enemy, (enemyx, enemyy))
        if enemy2alive == True:
            display_window.blit(slime2, (slime2x, slime2y))
            display_window.blit(enemy2, (enemy2x, enemy2y))
        if enemy3alive == True:
            display_window.blit(slime3, (slime3x, slime3y))
            display_window.blit(enemy3, (enemy3x, enemy3y))
        if bossalive == True:
            display_window.blit(bossslime, (bossslimex, bossslimey))
            display_window.blit(bossslime2, (bossslime2x, bossslime2y))
            display_window.blit(boss, (bossx, bossy))
        display_window.blit(laser, (laserx, lasery))
        display_window.blit(user, (userx, usery))
        pygame.display.update()
    
        
    


def enemy_shoot():
    global speed, laserx, level_num, slime, slimex, slimey, enemy, enemyx, enemyy, laser, laserx, lasery, enemy2, enemy2x, enemy2y, enemy, boss_shoot_time, boss_shoot_clock
    global user, userx, usery, lives, lives_5, lives_4, lives_3, lives_2, lives_1, level_bg, slime2x, slime2y, slime2, enemy_shoot_clock, enemy_shoot_time
    global enemy2_shoot_clock, enemy2_shoot_time, enemyalive, enemy2alive, enemy3alive, bossalive, display_window, enemy3_shoot_time, enemy3_shoot_clock
    global slime3x, slime3y, slime3, bossslime, bossslimex, bossslimey, bossslime2, bossslime2x, bossslime2y, boss2_shoot_time, boss2_shoot_clock
    
    if slimey == enemyy + 35 and enemyalive == True:
        enemy_shoot_clock.tick(60)
        enemy_shoot_time += enemy_shoot_clock.get_rawtime()
        save = enemy_shoot_time
        
        if enemy_shoot_time >= 1250:
            slimey += 1
            enemy_shoot_time = 0
    if level_num >= 2:
        if slime2y == enemy2y + 35 and enemy2alive == True:
            enemy2_shoot_clock.tick(60)
            enemy2_shoot_time += enemy2_shoot_clock.get_rawtime()
            save2 = enemy2_shoot_time
            
            if enemy2_shoot_time >= 1250:
                slime2y += 1
                enemy2_shoot_time = 0
    if level_num >= 3:
        if slime3y == enemy3y + 35 and enemy3alive == True:
            enemy3_shoot_clock.tick(60)
            enemy3_shoot_time += enemy3_shoot_clock.get_rawtime()
            save3 = enemy3_shoot_time
            
            if enemy3_shoot_time >= 1250:
                slime3y += 1
                enemy3_shoot_time = 0
    if level_num >= 4:
        if bossslimey == bossy + 35 and bossalive == True:
            boss_shoot_clock.tick(60)
            boss_shoot_time += boss_shoot_clock.get_rawtime()
            bosssave = boss_shoot_time
            
            if boss_shoot_time >= 1250:
                bossslimey += 1
                boss_shoot_time = 0
        if bossslime2y == bossy + 35 and bossalive == True:
            boss2_shoot_clock.tick(60)
            boss2_shoot_time += boss2_shoot_clock.get_rawtime()
            bosss2ave = boss2_shoot_time
            
            if boss2_shoot_time >= 1250:
                bossslime2y += 1
                boss2_shoot_time = 0
    


def laser_enemy_collision():
    global speed, laserx, level_num, slime, slimex, slimey, enemy, enemyx, enemyy, laser, laserx, lasery, kill_count, enemy2, enemy2x, enemy2y
    global user, userx, usery, lives, lives_5, lives_4, lives_3, lives_2, lives_1, level_bg, enemy_explosion_clock, enemyhp, enemy2hp, enemy3hp, bosshp
    global enemyalive, enemy2alive, enemy3alive, bossalive, slime2, slime2x, slime2y, slime3, slime3x, slime3y, display_window, enemy3, enemy3x, enemy3y
    global bossx, bossy, boss, bossslime, bossslimex, bossslimey, bossslime2, bossslime2x, bossslime2y

    #ENEMY DETECTION#################################################
    if laserx > enemyx and laserx < enemyx + 123 and lasery > enemyy and lasery < enemyy + 100:
        enemyhp -= 1
        if enemyhp == 0:
            kill_count += 1
            enemyx = 999
            enemyy = 999
            enemyalive = False
        laserx = userx + 22
        lasery = usery + 35
        
        if level_num == 1:
            display_window.blit(level_bg, (0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            display_window.blit(explosion,(enemyx,enemyy))
            pygame.display.update()
        elif level_num == 2:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            display_window.blit(explosion,(enemyx,enemyy))
            pygame.display.update()
        elif level_num == 3:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if enemy3alive == True:
                display_window.blit(slime3, (slime3x, slime3y))
                display_window.blit(enemy3, (enemy3x, enemy3y))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            display_window.blit(explosion,(enemyx,enemyy))
            pygame.display.update()
        elif level_num == 5:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(user, (userx, usery))
            display_window.blit(explosion,(enemyx,enemyy))
            pygame.display.update()
        elif level_num == 6:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(user, (userx, usery))
            display_window.blit(explosion,(enemyx,enemyy))
            pygame.display.update()
        elif level_num == 7:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if enemy3alive == True:
                display_window.blit(slime3, (slime3x, slime3y))
                display_window.blit(enemy3, (enemy3x, enemy3y))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(user, (userx, usery))
            display_window.blit(explosion,(enemyx,enemyy))
            pygame.display.update()
        
        enemy_explosion = 0
        
        while enemy_explosion < 500:
            enemy_explosion = enemy_explosion + enemy_explosion_clock.get_rawtime()
            enemy_explosion_clock.tick(60)
            
        if level_num == 1:
            display_window.blit(level_bg, (0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
        elif level_num == 2:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
        elif level_num == 3:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if enemy3alive == True:
                display_window.blit(slime3, (slime3x, slime3y))
                display_window.blit(enemy3, (enemy3x, enemy3y))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
        elif level_num == 5:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
        elif level_num == 6:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
        elif level_num == 7:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if enemy3alive == True:
                display_window.blit(slime3, (slime3x, slime3y))
                display_window.blit(enemy3, (enemy3x, enemy3y))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()


    #ENEMY 2 DETECTION############################################        
    if laserx > enemy2x and laserx < enemy2x + 123 and lasery > enemy2y and lasery < enemy2y + 100 and level_num >= 2:
        enemy2hp -= 1
        if enemy2hp == 0:
            kill_count += 1
            enemy2x = 999
            enemy2y = 999
            enemy2alive = False
        laserx = userx + 22
        lasery = usery + 35
        
        if level_num == 2:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            display_window.blit(explosion,(enemy2x,enemy2y))
            pygame.display.update()
        elif level_num == 3:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy3alive == True:
                display_window.blit(slime3, (slime3x, slime3y))
                display_window.blit(enemy3, (enemy3x, enemy3y))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            display_window.blit(explosion,(enemy2x,enemy2y))
            pygame.display.update()
        elif level_num == 6:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            display_window.blit(explosion,(enemy2x,enemy2y))
            pygame.display.update()
        elif level_num == 7:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy3alive == True:
                display_window.blit(slime3, (slime3x, slime3y))
                display_window.blit(enemy3, (enemy3x, enemy3y))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            display_window.blit(explosion,(enemy2x,enemy2y))
            pygame.display.update()
        
        enemy_explosion = 0
        
        while enemy_explosion < 500:
            enemy_explosion = enemy_explosion + enemy_explosion_clock.get_rawtime()
            enemy_explosion_clock.tick(60)
            
        if level_num == 2:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
        elif level_num == 3:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy3alive == True:
                display_window.blit(slime3, (slime3x, slime3y))
                display_window.blit(enemy3, (enemy3x, enemy3y))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
        elif level_num == 6:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
        elif level_num == 7:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy3alive == True:
                display_window.blit(slime3, (slime3x, slime3y))
                display_window.blit(enemy3, (enemy3x, enemy3y))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()

    #ENEMY 3 DETECTION####################################
    if laserx > enemy3x and laserx < enemy3x + 123 and lasery > enemy3y and lasery < enemy3y + 100 and level_num >= 2:
        enemy3hp -= 1
        if enemy3hp == 0:
            kill_count += 1
            enemy3x = 999
            enemy3y = 999
            enemy3alive = False
        laserx = userx + 22
        lasery = usery + 35
        
        if level_num == 3:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            display_window.blit(explosion,(enemy3x,enemy3y))
            pygame.display.update()
        if level_num == 7:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            display_window.blit(explosion,(enemy3x,enemy3y))
            pygame.display.update()
        
        enemy_explosion = 0
        
        while enemy_explosion < 500:
            enemy_explosion = enemy_explosion + enemy_explosion_clock.get_rawtime()
            enemy_explosion_clock.tick(60)
            
        if level_num == 3:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
        if level_num == 7:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()

    #BOSS DETECTION####################################
    if laserx > bossx and laserx < bossx + 232 and lasery > bossy and lasery < bossy + 160 and level_num >= 2:
        bosshp -= 1
        if bosshp == 0:
            kill_count += 1
            bossx = 999
            bossy = 999
            bossalive = False
        laserx = userx + 22
        lasery = usery + 35
        
        if level_num == 4:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            display_window.blit(explosion,(bossx+60,bossy))
            pygame.display.update()
        elif level_num == 5:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            display_window.blit(explosion,(bossx+60,bossy))
            pygame.display.update()
        elif level_num == 6:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            display_window.blit(explosion,(bossx+60,bossy))
            pygame.display.update()
        elif level_num == 7:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if enemy3alive == True:
                display_window.blit(slime3, (slime3x, slime3y))
                display_window.blit(enemy3, (enemy3x, enemy3y))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            display_window.blit(explosion,(bossx+60,bossy))
            pygame.display.update()
        
        enemy_explosion = 0
        
        while enemy_explosion < 500:
            enemy_explosion = enemy_explosion + enemy_explosion_clock.get_rawtime()
            enemy_explosion_clock.tick(60)
            
        if level_num == 4:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            display_window.blit(bossslime, (bossslimex, bossslimey))
            display_window.blit(bossslime2, (bossslime2x, bossslime2y))
            display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
        elif level_num == 5:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
        elif level_num == 6:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
        elif level_num == 7:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if enemy3alive == True:
                display_window.blit(slime3, (slime3x, slime3y))
                display_window.blit(enemy3, (enemy3x, enemy3y))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()

        
    if level_num == 1 and kill_count == 1:
        display_window.blit(level_bg,(0,0))
        level_num = 2
        math_prob()
        reset_var()
        print('Level 1 cleared!')
        display_window.blit(star, (0, 0))
        pygame.display.update()
        pygame.time.delay(1500)
        level_2()
    if level_num == 2 and kill_count == 2:
        display_window.blit(level_bg,(0,0))
        level_num = 3
        math_prob()
        reset_var()
        print('Level 2 cleared!')
        display_window.blit(star, (0, 0))
        pygame.display.update()
        pygame.time.delay(1500)
        level_3()
    if level_num == 3 and kill_count == 3:
        display_window.blit(level_bg,(0,0))
        level_num = 4
        math_prob()
        reset_var()
        print('Level 3 cleared!')
        display_window.blit(star, (0, 0))
        pygame.display.update()
        pygame.time.delay(1500)
        level_4()
    if level_num == 4 and kill_count == 1:
        display_window.blit(level_bg,(0,0))
        level_num = 5
        math_prob()
        reset_var()
        print('Level 4 cleared!')
        display_window.blit(star, (0, 0))
        pygame.display.update()
        pygame.time.delay(1500)
        level_5()
    if level_num == 5 and kill_count == 2:
        display_window.blit(level_bg,(0,0))
        level_num = 6
        math_prob()
        reset_var()
        print('Level 5 cleared!')
        display_window.blit(star, (0, 0))
        pygame.display.update()
        pygame.time.delay(1500)
        level_6()
    if level_num == 6 and kill_count == 3:
        display_window.blit(level_bg,(0,0))
        level_num = 7
        math_prob()
        reset_var()
        print('Level 6 cleared!')
        display_window.blit(star, (0, 0))
        pygame.display.update()
        pygame.time.delay(1500)
        level_7()
    if level_num == 7 and kill_count == 4:
        display_window.blit(level_bg,(0,0))
        math_prob()
        reset_var()
        level_num = 1
        print('Level 7 cleared!')
        display_window.blit(star, (0, 0))
        pygame.display.update()
        pygame.time.delay(1500)
        end_scene()


def slime_user_collision():
    global speed, laserx, level_num, slime, slimex, slimey, enemy, enemyx, enemyy, laser, laserx, lasery, enemy2, enemy2x, enemy2y
    global user, userx, usery, lives, lives_5, lives_4, lives_3, lives_2, lives_1, level_bg, slime2x, slime2y, slime2
    global enemyalive, enemy2alive, enemy3alive, bossalive, display_window, slime3, slime3x, slime3y, enemy3, enemy3x, enemy3y, boss, bossx, bossy
    global bossslime, bossslimex, bossslimey, bossslime2, bossslime2x, bossslime2y

    #SLIME DETECTION#########################################3
    if slimex > userx - 40 and slimex < userx + 48 and slimey > usery - 40 and slimey < usery + 100 and enemyalive == True and (level_num <= 3 or level_num >= 5):
        lives -= 1
        slimey = enemyy + 35
        slimex = enemyx + 30
        if level_num == 1:
            display_window.blit(level_bg, (0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            display_window.blit(slime, (enemyx + 30, enemyy + 35))
            slimex = enemyx + 30
            slimey = enemyx + 35
            display_window.blit(enemy, (enemyx, enemyy))
            display_window.blit(explosion, (userx - 25, usery))
            pygame.display.update()
        elif level_num == 2:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                slimex = enemyx + 30
                slimey = enemyx + 35
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            display_window.blit(explosion, (userx - 25, usery))
            pygame.display.update()
        elif level_num == 3:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                slimex = enemyx + 30
                slimey = enemyx + 35
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if enemy3alive == True:
                display_window.blit(slime3, (slime3x, slime3y))
                display_window.blit(enemy3, (enemy3x, enemy3y))
            display_window.blit(explosion, (userx - 25, usery))
            pygame.display.update()
        elif level_num == 5:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                slimex = enemyx + 30
                slimey = enemyx + 35
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(explosion, (userx - 25, usery))
            pygame.display.update()
        elif level_num == 6:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                slimex = enemyx + 30
                slimey = enemyx + 35
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(explosion, (userx - 25, usery))
            pygame.display.update()
        elif level_num == 7:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                slimex = enemyx + 30
                slimey = enemyx + 35
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if enemy3alive == True:
                display_window.blit(slime3, (slime3x, slime3y))
                display_window.blit(enemy3, (enemy3x, enemy3y))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(explosion, (userx - 25, usery))
            pygame.display.update()
        pygame.time.delay(250)
        ###############################################
        if level_num == 1:
            display_window.blit(level_bg, (0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            display_window.blit(slime, (enemyx + 30, enemyy + 35))
            slimex = enemyx + 30
            slimey = enemyx + 35
            display_window.blit(enemy, (enemyx, enemyy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
            math_prob()
            pygame.display.update()
        elif level_num == 2:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                slimex = enemyx + 30
                slimey = enemyx + 35
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
            math_prob()
            pygame.display.update()
        elif level_num == 3:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                slimex = enemyx + 30
                slimey = enemyx + 35
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if enemy3alive == True:
                display_window.blit(slime3, (slime3x, slime3y))
                display_window.blit(enemy3, (enemy3x, enemy3y))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
            math_prob()
            pygame.display.update()
        elif level_num == 5:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                slimex = enemyx + 30
                slimey = enemyx + 35
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
            math_prob()
            pygame.display.update()
        elif level_num == 6:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                slimex = enemyx + 30
                slimey = enemyx + 35
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
            math_prob()
            pygame.display.update()
        elif level_num == 7:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                slimex = enemyx + 30
                slimey = enemyx + 35
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if enemy3alive == True:
                display_window.blit(slime3, (slime3x, slime3y))
                display_window.blit(enemy3, (enemy3x, enemy3y))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
            math_prob()
            pygame.display.update()

    #SLIME 2 DETECTION###################################################33
    if slime2x > userx - 40 and slime2x < userx + 48 and slime2y > usery - 40 and slime2y < usery + 100 and enemy2alive == True and (level_num == 2 or level_num == 3 or level_num >= 6):
        lives -= 1
        slime2y = enemy2y + 35
        slime2x = enemy2x + 30

        if level_num == 2:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                slime2x = enemy2x + 30
                slime2y = enemy2y + 35
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            display_window.blit(explosion, (userx - 25, usery))
            pygame.display.update()
        elif level_num == 3:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                slime2x = enemy2x + 30
                slime2y = enemy2y + 35
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if enemy3alive == True:
                display_window.blit(slime3, (slime3x, slime3y))
                display_window.blit(enemy3, (enemy3x, enemy3y))
            display_window.blit(explosion, (userx - 25, usery))
            pygame.display.update()
        elif level_num == 6:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                slime2x = enemy2x + 30
                slime2y = enemy2y + 35
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(explosion, (userx - 25, usery))
            pygame.display.update()
        elif level_num == 7:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                slime2x = enemy2x + 30
                slime2y = enemy2y + 35
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if enemy3alive == True:
                display_window.blit(slime3, (slime3x, slime3y))
                display_window.blit(enemy3, (enemy3x, enemy3y))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(explosion, (userx - 25, usery))
            pygame.display.update()
        pygame.time.delay(250)
        #############################################
        if level_num == 2:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                slime2x = enemy2x + 30
                slime2y = enemy2y + 35
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
            math_prob()
            pygame.display.update()
        elif level_num == 3:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                slime2x = enemy2x + 30
                slime2y = enemy2y + 35
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if enemy3alive == True:
                display_window.blit(slime3, (slime3x, slime3y))
                display_window.blit(enemy3, (enemy3x, enemy3y))
            display_window.blit(explosion, (userx - 25, usery))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
            math_prob()
            pygame.display.update()
        elif level_num == 6:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                slime2x = enemy2x + 30
                slime2y = enemy2y + 35
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
            math_prob()
            pygame.display.update()
        elif level_num == 7:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                slime2x = enemy2x + 30
                slime2y = enemy2y + 35
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if enemy3alive == True:
                display_window.blit(slime3, (slime3x, slime3y))
                display_window.blit(enemy3, (enemy3x, enemy3y))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(explosion, (userx - 25, usery))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
            math_prob()
            pygame.display.update()
            
    #SLIME 3 DETECTION###################################################33
    if slime3x > userx - 40 and slime3x < userx + 48 and slime3y > usery - 40 and slime3y < usery + 100 and enemy3alive == True and (level_num == 3 or level_num == 7):
        lives -= 1
        slime3y = enemy3y + 35
        slime3x = enemy3x + 30

        if level_num == 3:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if enemy3alive == True:
                slime3x = enemy3x + 30
                slime3y = enemy3y + 35
                display_window.blit(slime3, (slime3x, slime3y))
                display_window.blit(enemy3, (enemy3x, enemy3y))
            display_window.blit(explosion, (userx - 25, usery))
            pygame.display.update()
        elif level_num == 7:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if enemy3alive == True:
                slime3x = enemy3x + 30
                slime3y = enemy3y + 35
                display_window.blit(slime3, (slime3x, slime3y))
                display_window.blit(enemy3, (enemy3x, enemy3y))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(explosion, (userx - 25, usery))
            pygame.display.update()
        pygame.time.delay(250)
        ###########################################################3
        if level_num == 3:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if enemy3alive == True:
                slime3x = enemy3x + 30
                slime3y = enemy3y + 35
                display_window.blit(slime3, (slime3x, slime3y))
                display_window.blit(enemy3, (enemy3x, enemy3y))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
            math_prob()
            pygame.display.update()
        elif level_num == 7:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if enemy3alive == True:
                slime3x = enemy3x + 30
                slime3y = enemy3y + 35
                display_window.blit(slime3, (slime3x, slime3y))
                display_window.blit(enemy3, (enemy3x, enemy3y))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
            math_prob()
            pygame.display.update()

    #BOSS SLIME DETECTION###################################################33
    if bossslimex > userx - 40 and bossslimex < userx + 48 and bossslimey > usery - 40 and bossslimey < usery + 100 and bossalive == True and (level_num >= 4):
        lives -= 1
        bossslimey = bossy + 35
        bossslimex = bossx + 50

        if level_num == 4:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if bossalive == True:
                bossslimex = bossx + 50
                bossslimey = bossy + 35
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(explosion, (userx - 25, usery))
            pygame.display.update()
        elif level_num == 5:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if bossalive == True:
                bossslimex = bossx + 50
                bossslimey = bossy + 35
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(explosion, (userx - 25, usery))
            pygame.display.update()
        elif level_num == 6:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if bossalive == True:
                bossslimex = bossx + 50
                bossslimey = bossy + 35
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(explosion, (userx - 25, usery))
            pygame.display.update()
        elif level_num == 7:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if enemy3alive == True:
                display_window.blit(slime3, (slime3x, slime3y))
                display_window.blit(enemy3, (enemy3x, enemy3y))
            if bossalive == True:
                bossslimex = bossx + 50
                bossslimey = bossy + 35
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(explosion, (userx - 25, usery))
            pygame.display.update()
        pygame.time.delay(250)
        ###########################################################3
        if level_num == 4:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if bossalive == True:
                bossslimex = bossx + 50
                bossslimey = bossy + 35
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
            math_prob()
            pygame.display.update()
        elif level_num == 5:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if bossalive == True:
                bossslimex = bossx + 50
                bossslimey = bossy + 35
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
            math_prob()
            pygame.display.update()
        elif level_num == 6:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if bossalive == True:
                bossslimex = bossx + 50
                bossslimey = bossy + 35
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
            math_prob()
            pygame.display.update()
        elif level_num == 7:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if enemy3alive == True:
                display_window.blit(slime3, (slime3x, slime3y))
                display_window.blit(enemy3, (enemy3x, enemy3y))
            if bossalive == True:
                bossslimex = bossx + 50
                bossslimey = bossy + 35
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
            math_prob()
            pygame.display.update()

    #BOSS SLIME 2 DETECTION###################################################33
    if bossslime2x > userx - 40 and bossslime2x < userx + 48 and bossslime2y > usery - 40 and bossslime2y < usery + 100 and (level_num >= 4):
        lives -= 1
        bossslime2y = bossy + 35
        bossslime2x = bossx + 30

        if level_num == 4:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if bossalive == True:
                bossslime2x = bossx + 130
                bossslime2y = bossy + 35
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(explosion, (userx - 25, usery))
            pygame.display.update()
        elif level_num == 5:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if bossalive == True:
                bossslime2x = bossx + 130
                bossslime2y = bossy + 35
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(explosion, (userx - 25, usery))
            pygame.display.update()
        elif level_num == 6:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if bossalive == True:
                bossslime2x = bossx + 130
                bossslime2y = bossy + 35
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(explosion, (userx - 25, usery))
            pygame.display.update()
        elif level_num == 7:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if enemy3alive == True:
                display_window.blit(slime3, (slime3x, slime3y))
                display_window.blit(enemy3, (enemy3x, enemy3y))
            if bossalive == True:
                bossslime2x = bossx + 130
                bossslime2y = bossy + 35
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(explosion, (userx - 25, usery))
            pygame.display.update()
        pygame.time.delay(250)
        ###########################################################3
        if level_num == 4:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if bossalive == True:
                bossslime2x = bossx + 130
                bossslime2y = bossy + 35
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
            math_prob()
            pygame.display.update()
        elif level_num == 5:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if bossalive == True:
                bossslime2x = bossx + 130
                bossslime2y = bossy + 35
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
            math_prob()
            pygame.display.update()
        elif level_num == 6:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if bossalive == True:
                bossslime2x = bossx + 130
                bossslime2y = bossy + 35
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
            math_prob()
            pygame.display.update()
        elif level_num == 7:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if enemy3alive == True:
                display_window.blit(slime3, (slime3x, slime3y))
                display_window.blit(enemy3, (enemy3x, enemy3y))
            if bossalive == True:
                bossslime2x = bossx + 130
                bossslime2y = bossy + 35
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
            math_prob()
            pygame.display.update()

def reset_var():
    global display_window, lives, hit, level_num, speed, enemy_speed, kill_count, enemy_dir, enemyhp, enemy2hp, enemy3hp, slimespeed, laserspeed
    global userx, usery, enemyx, enemy2x, enemy3x, enemy_resx, enemyy, enemy2y, enemy3y, enemyresy, laserx, lasery, slimex, slimey, enemy_shoot_time, enemy_move_c, bosshp
    global slime2x, slime3x, bossslimex, enemyx, slime2, enemy2, enemy3, slime3, bossslimex, bossslimey, bossslime, enemy_move_2, enemy_move_3, boss_move, enemy2_dir, enemy3_dir, boss_dir
    global enemy2_shoot_time, enemy3_shoot_time, boss_shoot_time, slime2y, slime3y, enemyalive, enemy2alive, enemy3alive, bossalive, bossx, bossy, bossslime2, bossslime2x, bossslime2y
    global boss_speed, bossy, bossx, boss
    
    userx = random.randint(10, 542)
    usery = 450
    enemyx = random.randint(110, 442)
    enemy2x = random.randint(110, 442)
    enemy3x = random.randint(110, 442)
    enemy_resx = random.randint(110, 442)
    bossx = random.randint(110, 337)
    enemyy = enemy2y = enemy3y = bossy = 40
    laserx = userx + 22
    lasery = usery + 35
    slimex = enemyx + 30
    slimey = enemyy + 35
    slime2x = enemy2x + 30
    slime2y = enemy2x + 35
    slime3x = enemy3x + 30
    slime3y = enemy3y + 35
    bossslimex = bossx + 50
    bossslimey = bossy + 35
    bossslime2x = bossx + 130
    bossslime2y = bossy + 35
    speed = 3
    enemy_speed = 1
    boss_speed = 0.5
    if level_num == 2:
        enemy_speed = 1.5
    enemy_shoot_time = enemy2_shoot_time = enemy3_shoot_time = boss_shoot_time = 0
    kill_count = 0
    enemy_move_c = enemy_move_2 = enemy_move_3 = boss_move= 0
    enemy_dir = enemy2_dir = enemy3_dir = boss_dir= 1
    enemyhp = 2
    enemy2hp = 2
    enemy3hp = 2
    bosshp = 15
    enemyalive = True
    enemy2alive = True
    enemy3alive = True
    bossalive = True
    slimespeed = 2
    if level_num == 2:
        slimespeed += 1
    if level_num == 3 or level_num == 4 or level_num == 5 or level_num == 6 or level_num == 7:
        slimespeed += 2
    if level_num == 6 or level_num == 7:
        slimespeed += 1
    laserspeed = 6
    if level_num == 2:
        laserspeed += 1
    if level_num == 3 or level_num == 4 or level_num == 5 or level_num == 6 or level_num == 7:
        laserspeed += 3
    if level_num == 6 or level_num == 7:
        laserspeed += 2

def continue_loop():
    global speed, laserx, level_num, slime, slimex, slimey, enemy, enemyx, enemyy, laser, laserx, lasery, slime2, slime2x, slime2y, slime3, slime3x, slime3y, enemy2, enemy2x, enemy2y
    global user, userx, usery, lives, lives_5, lives_4, lives_3, lives_2, lives_1, level_bg, enemyalive, enemy2alive, enemy3alive, bossalive, enemy3, enemy3x, enemy3y, display_window
    global slimespeed, laserspeed, boss, bossx, bossy, bossslime, bossslimex, bossslimey, bossslime2, bossslime2x, bossslime2y
    
    if lasery != usery + 35:
        lasery -= laserspeed
        if level_num == 1:
            display_window.blit(level_bg, (0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            display_window.blit(slime, (slimex, slimey))
            display_window.blit(enemy, (enemyx, enemyy))
            pygame.display.update()
        elif level_num == 2:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
        elif level_num == 3:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if enemy3alive == True:
                display_window.blit(slime3, (slime3x, slime3y))
                display_window.blit(enemy3, (enemy3x, enemy3y))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
        elif level_num == 4:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
        elif level_num == 5:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
        elif level_num == 6:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
        elif level_num == 7:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if enemy3alive == True:
                display_window.blit(slime3, (slime3x, slime3y))
                display_window.blit(enemy3, (enemy3x, enemy3y))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()

    if slimey != enemyy + 35:
        slimey += slimespeed
        if level_num == 1:
            display_window.blit(level_bg, (0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            display_window.blit(slime, (slimex, slimey))
            display_window.blit(enemy, (enemyx, enemyy))
            pygame.display.update()
        elif level_num == 2:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
        elif level_num == 3:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if enemy3alive == True:
                display_window.blit(slime3, (slime3x, slime3y))
                display_window.blit(enemy3, (enemy3x, enemy3y))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
        elif level_num == 5:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
        elif level_num == 6:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
        elif level_num == 7:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if enemy3alive == True:
                display_window.blit(slime3, (slime3x, slime3y))
                display_window.blit(enemy3, (enemy3x, enemy3y))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
            
    if slime2y != enemy2y + 35 and level_num >= 2:
        slime2y += slimespeed
        if level_num == 2:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
        elif level_num == 3:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if enemy3alive == True:
                display_window.blit(slime3, (slime3x, slime3y))
                display_window.blit(enemy3, (enemy3x, enemy3y))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
        elif level_num == 6:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
        elif level_num == 7:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if enemy3alive == True:
                display_window.blit(slime3, (slime3x, slime3y))
                display_window.blit(enemy3, (enemy3x, enemy3y))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()

    if slime3y != enemy3y + 35 and level_num >= 3:
        slime3y += slimespeed
        if level_num == 3:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if enemy3alive == True:
                display_window.blit(slime3, (slime3x, slime3y))
                display_window.blit(enemy3, (enemy3x, enemy3y))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
        elif level_num == 7:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if enemy3alive == True:
                display_window.blit(slime3, (slime3x, slime3y))
                display_window.blit(enemy3, (enemy3x, enemy3y))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()

    if bossslimey != bossy + 35 and level_num >= 4:
        bossslimey += slimespeed
        if level_num == 4:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
        elif level_num == 5:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
        elif level_num == 6:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
        elif level_num == 7:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if enemy3alive == True:
                display_window.blit(slime3, (slime3x, slime3y))
                display_window.blit(enemy3, (enemy3x, enemy3y))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
            
    if bossslime2y != bossy + 35 and level_num >= 4:
        bossslime2y += slimespeed
        if level_num == 4:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
        elif level_num == 5:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
        elif level_num == 6:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
        elif level_num == 7:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if enemy3alive == True:
                display_window.blit(slime3, (slime3x, slime3y))
                display_window.blit(enemy3, (enemy3x, enemy3y))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
            
    if lasery <= -50:
        lasery = usery + 35
        laserx = userx + 22
        if level_num == 1:
            display_window.blit(level_bg, (0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            display_window.blit(slime, (slimex, slimey))
            display_window.blit(enemy, (enemyx, enemyy))
            pygame.display.update()
        elif level_num == 2:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
        elif level_num == 3:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if enemy3alive == True:
                display_window.blit(slime3, (slime3x, slime3y))
                display_window.blit(enemy3, (enemy3x, enemy3y))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
        elif level_num == 4:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
        elif level_num == 5:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
        elif level_num == 6:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
        elif level_num == 7:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if enemy3alive == True:
                display_window.blit(slime3, (slime3x, slime3y))
                display_window.blit(enemy3, (enemy3x, enemy3y))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()

    if slimey >= 650:
        slimey = enemyy + 35
        slimex = enemyx + 30
        if level_num == 1:
            display_window.blit(level_bg, (0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            display_window.blit(slime, (slimex, slimey))
            display_window.blit(enemy, (enemyx, enemyy))
            pygame.display.update()
        elif level_num == 2:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
        elif level_num == 3:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if enemy3alive == True:
                display_window.blit(slime3, (slime3x, slime3y))
                display_window.blit(enemy3, (enemy3x, enemy3y))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
        elif level_num == 5:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
        elif level_num == 6:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
        elif level_num == 7:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if enemy3alive == True:
                display_window.blit(slime3, (slime3x, slime3y))
                display_window.blit(enemy3, (enemy3x, enemy3y))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()

    if slime2y >= 650 and level_num >= 2:
        slime2y = enemy2y + 35
        slime2x = enemy2x + 30
        if level_num == 2:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
        elif level_num == 3:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if enemy3alive == True:
                display_window.blit(slime3, (slime3x, slime3y))
                display_window.blit(enemy3, (enemy3x, enemy3y))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
        elif level_num == 6:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
        elif level_num == 7:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if enemy3alive == True:
                display_window.blit(slime3, (slime3x, slime3y))
                display_window.blit(enemy3, (enemy3x, enemy3y))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()

    if slime3y >= 650 and level_num >= 3:
        slime3y = enemy3y + 35
        slime3x = enemy3x + 30
        if level_num == 3:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if enemy3alive == True:
                display_window.blit(slime3, (slime3x, slime3y))
                display_window.blit(enemy3, (enemy3x, enemy3y))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
        elif level_num == 7:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if enemy3alive == True:
                display_window.blit(slime3, (slime3x, slime3y))
                display_window.blit(enemy3, (enemy3x, enemy3y))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()

    if bossslimey >= 650 and level_num >= 4:
        bossslimey = bossy + 35
        bossslimex = bossx + 50
        if level_num == 4:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
        elif level_num == 5:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
        elif level_num == 6:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
        elif level_num == 7:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if enemy3alive == True:
                display_window.blit(slime3, (slime3x, slime3y))
                display_window.blit(enemy3, (enemy3x, enemy3y))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
            
    if bossslime2y >= 650 and level_num >= 4:
        bossslime2y = bossy + 35
        bossslime2x = bossx + 130
        if level_num == 4:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
        elif level_num == 5:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
        elif level_num == 6:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()
        elif level_num == 7:
            display_window.blit(level_bg,(0,0))
            if lives == 5:
                display_window.blit(lives_5,(440,10))
            if lives == 4:
                display_window.blit(lives_4,(470,10))
            if lives == 3:
                display_window.blit(lives_3,(500,10))
            if lives == 2:
                display_window.blit(lives_2,(530,10))
            if lives == 1:
                display_window.blit(lives_1,(560,10))
            if enemyalive == True:
                display_window.blit(slime, (slimex, slimey))
                display_window.blit(enemy, (enemyx, enemyy))
            if enemy2alive == True:
                display_window.blit(slime2, (slime2x, slime2y))
                display_window.blit(enemy2, (enemy2x, enemy2y))
            if enemy3alive == True:
                display_window.blit(slime3, (slime3x, slime3y))
                display_window.blit(enemy3, (enemy3x, enemy3y))
            if bossalive == True:
                display_window.blit(bossslime, (bossslimex, bossslimey))
                display_window.blit(bossslime2, (bossslime2x, bossslime2y))
                display_window.blit(boss, (bossx, bossy))
            display_window.blit(laser, (laserx, lasery))
            display_window.blit(user, (userx, usery))
            pygame.display.update()


def level_1():
    global lives, hit, level_num, clock, clock1, enemy_explosion_clock, level_bg, user, enemy, explosion, speed, bossx, bossy, bossslimex, bossslimey, display_window
    global laser, math, lives_5, lives_4, lives_3, lives_2, lives_1, slime, game_over, enemy_speed, kill_count, slime2, slime2x, slime2y, slime3, slime3x, slime3y
    global userx, usery, enemyx, enemy2x, enemy3x, enemy4x, enemy_resx, enemyresy, laserx, lasery, slimex, slimey, enemyalive, enemy2alive, enemy3alive, bossalive
    global bossslime2, bossslime2x, bossslime2y

    reset_var()
    enemy2x = enemy3x = bossx = 999
    enemy2y = enemy3y = bossy = 999
    slime2x = slime3x = bossslimex = bossslime2x = 1029
    slime2y = slime3y = bossslimey = bossslime2y = 1034
    pygame.display.update()

    countdown()
    
    display_window.blit(level_bg, (0,0))
    if lives == 5:
        display_window.blit(lives_5,(440,10))
    if lives == 4:
        display_window.blit(lives_4,(470,10))
    if lives == 3:
        display_window.blit(lives_3,(500,10))
    if lives == 2:
        display_window.blit(lives_2,(530,10))
    if lives == 1:
        display_window.blit(lives_1,(560,10))
    slimex = enemyx + 30
    slimey = enemyy + 35
    display_window.blit(slime, (slimex, slimey))
    display_window.blit(enemy, (enemyx, enemyy))
    display_window.blit(laser, (laserx, lasery))
    display_window.blit(user, (userx, usery))
    pygame.display.update()

    while level_num == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit(); sys.exit();

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_SPACE]:
            shoot()
        
        if keys[pygame.K_LEFT]:
            left()
            
        if keys[pygame.K_RIGHT]:
            right()

        enemy_movement()
        enemy_shoot()
        continue_loop()
        slime_user_collision()
        laser_enemy_collision()
        
def level_2():
    global lives, hit, level_num, clock, clock1, enemy_explosion_clock, level_bg, user, enemy, explosion, speed, bossx, bossy, bossslimex, bossslimey, display_window
    global laser, math, lives_5, lives_4, lives_3, lives_2, lives_1, slime, game_over, enemy_speed, kill_count, slime2, slime2x, slime2y, slime3, slime3x, slime3y
    global userx, usery, enemyx, enemy2x, enemy3x, enemy4x, enemy_resx, enemyresy, laserx, lasery, slimex, slimey, enemyalive, enemy2alive, enemy3alive, bossalive
    global bossslime2, bossslime2x, bossslime2y

    reset_var()
    enemy3x = bossx = 999
    enemy3y = bossy = 999
    slime3x = bossslimex = bossslime2x = 1029
    slime3y = bossslimey = bossslime2y = 1034
    pygame.display.update()

    countdown()
    
    display_window.blit(level_bg, (0,0))
    if lives == 5:
        display_window.blit(lives_5,(440,10))
    if lives == 4:
        display_window.blit(lives_4,(470,10))
    if lives == 3:
        display_window.blit(lives_3,(500,10))
    if lives == 2:
        display_window.blit(lives_2,(530,10))
    if lives == 1:
        display_window.blit(lives_1,(560,10))
    slimex = enemyx + 30
    slimey = enemyy + 35
    display_window.blit(slime, (slimex, slimey))
    display_window.blit(enemy, (enemyx, enemyy))
    slime2x = enemy2x + 30
    slime2y = enemy2y + 35
    display_window.blit(slime2, (slime2x, slime2y))
    display_window.blit(enemy2, (enemy2x, enemy2y))
    display_window.blit(laser, (laserx, lasery))
    display_window.blit(user, (userx, usery))
    pygame.display.update()

    while level_num == 2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit(); sys.exit();

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_SPACE]:
            shoot()
        
        if keys[pygame.K_LEFT]:
            left()
            
        if keys[pygame.K_RIGHT]:
            right()

        enemy_movement()
        enemy_shoot()
        continue_loop()
        slime_user_collision()
        laser_enemy_collision()



def level_3():
    global lives, hit, level_num, clock, clock1, enemy_explosion_clock, level_bg, user, enemy, explosion, speed, bossx, bossy, bossslimex, bossslimey, display_window
    global laser, math, lives_5, lives_4, lives_3, lives_2, lives_1, slime, game_over, enemy_speed, kill_count, slime2, slime2x, slime2y, slime3, slime3x, slime3y
    global userx, usery, enemyx, enemy2x, enemy3x, enemy4x, enemy_resx, enemyresy, laserx, lasery, slimex, slimey, enemyalive, enemy2alive, enemy3alive, bossalive
    global bossslime2, bossslime2x, bossslime2y

    reset_var()
    bossx = 999
    bossy = 999
    bossslimex = bossslime2x = 1029
    bossslimey = bossslime2y = 1034
    pygame.display.update()

    countdown()
    
    display_window.blit(level_bg, (0,0))
    if lives == 5:
        display_window.blit(lives_5,(440,10))
    if lives == 4:
        display_window.blit(lives_4,(470,10))
    if lives == 3:
        display_window.blit(lives_3,(500,10))
    if lives == 2:
        display_window.blit(lives_2,(530,10))
    if lives == 1:
        display_window.blit(lives_1,(560,10))
    slimex = enemyx + 30
    slimey = enemyy + 35
    display_window.blit(slime, (slimex, slimey))
    display_window.blit(enemy, (enemyx, enemyy))
    slime2x = enemy2x + 30
    slime2y = enemy2y + 35
    display_window.blit(slime2, (slime2x, slime2y))
    display_window.blit(enemy2, (enemy2x, enemy2y))
    slime3x = enemy3x + 30
    slime3y = enemy3y + 35
    display_window.blit(slime3, (slime3x, slime3y))
    display_window.blit(enemy3, (enemy3x, enemy3y))
    display_window.blit(laser, (laserx, lasery))
    display_window.blit(user, (userx, usery))
    pygame.display.update()

    while level_num == 3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit(); sys.exit();

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_SPACE]:
            shoot()
        
        if keys[pygame.K_LEFT]:
            left()
            
        if keys[pygame.K_RIGHT]:
            right()

        enemy_movement()
        enemy_shoot()
        continue_loop()
        slime_user_collision()
        laser_enemy_collision()



def level_4():
    global lives, hit, level_num, clock, clock1, enemy_explosion_clock, level_bg, user, enemy, explosion, speed, bossx, bossy, bossslimex, bossslimey, display_window
    global laser, math, lives_5, lives_4, lives_3, lives_2, lives_1, slime, game_over, enemy_speed, kill_count, slime2, slime2x, slime2y, slime3, slime3x, slime3y
    global userx, usery, enemyx, enemy2x, enemy3x, enemy4x, enemy_resx, enemyresy, laserx, lasery, slimex, slimey, enemyalive, enemy2alive, enemy3alive, bossalive
    global bossslime2, bossslime2x, bossslime2y

    reset_var()
    enemyx = enemy2x = enemy3x = 999
    enemyy = enemy2y = enemy3y = 999
    slimex = slime2x = slime3x = 1029
    slimey = slime2y = slime3y = 1034
    pygame.display.update()

    countdown()
    
    display_window.blit(level_bg, (0,0))
    if lives == 5:
        display_window.blit(lives_5,(440,10))
    if lives == 4:
        display_window.blit(lives_4,(470,10))
    if lives == 3:
        display_window.blit(lives_3,(500,10))
    if lives == 2:
        display_window.blit(lives_2,(530,10))
    if lives == 1:
        display_window.blit(lives_1,(560,10))
    bossslimex = bossx + 50
    bossslimey = bossy + 35
    bossslime2x = bossx + 130
    bossslime2y = bossy + 35
    display_window.blit(bossslime, (bossslimex, bossslimey))
    display_window.blit(bossslime2, (bossslime2x, bossslime2y))
    display_window.blit(boss, (bossx, bossy))
    display_window.blit(laser, (laserx, lasery))
    display_window.blit(user, (userx, usery))
    pygame.display.update()

    while level_num == 4:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit(); sys.exit();

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_SPACE]:
            shoot()
        
        if keys[pygame.K_LEFT]:
            left()
            
        if keys[pygame.K_RIGHT]:
            right()

        enemy_movement()
        enemy_shoot()
        continue_loop()
        slime_user_collision()
        laser_enemy_collision()



def level_5():
    global lives, hit, level_num, clock, clock1, enemy_explosion_clock, level_bg, user, enemy, explosion, speed, bossx, bossy, bossslimex, bossslimey, display_window
    global laser, math, lives_5, lives_4, lives_3, lives_2, lives_1, slime, game_over, enemy_speed, kill_count, slime2, slime2x, slime2y, slime3, slime3x, slime3y
    global userx, usery, enemyx, enemy2x, enemy3x, enemy4x, enemy_resx, enemyresy, laserx, lasery, slimex, slimey, enemyalive, enemy2alive, enemy3alive, bossalive
    global bossslime2, bossslime2x, bossslime2y

    reset_var()
    enemy2x = enemy3x = 999
    enemy2y = enemy3y = 999
    slime2x = slime3x = 1029
    slime2y = slime3y = 1034
    pygame.display.update()

    countdown()
    
    display_window.blit(level_bg, (0,0))
    if lives == 5:
        display_window.blit(lives_5,(440,10))
    if lives == 4:
        display_window.blit(lives_4,(470,10))
    if lives == 3:
        display_window.blit(lives_3,(500,10))
    if lives == 2:
        display_window.blit(lives_2,(530,10))
    if lives == 1:
        display_window.blit(lives_1,(560,10))
    slimex = enemyx + 30
    slimey = enemyy + 35
    display_window.blit(slime, (slimex, slimey))
    display_window.blit(enemy, (enemyx, enemyy))
    bossslimex = bossx + 50
    bossslimey = bossy + 35
    bossslime2x = bossx + 130
    bossslime2y = bossy + 35
    display_window.blit(bossslime, (bossslimex, bossslimey))
    display_window.blit(bossslime2, (bossslime2x, bossslime2y))
    display_window.blit(boss, (bossx, bossy))
    display_window.blit(laser, (laserx, lasery))
    display_window.blit(user, (userx, usery))
    pygame.display.update()

    while level_num == 5:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit(); sys.exit();

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_SPACE]:
            shoot()
        
        if keys[pygame.K_LEFT]:
            left()
            
        if keys[pygame.K_RIGHT]:
            right()

        enemy_movement()
        enemy_shoot()
        continue_loop()
        slime_user_collision()
        laser_enemy_collision()



def level_6():
    global lives, hit, level_num, clock, clock1, enemy_explosion_clock, level_bg, user, enemy, explosion, speed, bossx, bossy, bossslimex, bossslimey, display_window
    global laser, math, lives_5, lives_4, lives_3, lives_2, lives_1, slime, game_over, enemy_speed, kill_count, slime2, slime2x, slime2y, slime3, slime3x, slime3y
    global userx, usery, enemyx, enemy2x, enemy3x, enemy4x, enemy_resx, enemyresy, laserx, lasery, slimex, slimey, enemyalive, enemy2alive, enemy3alive, bossalive
    global bossslime2, bossslime2x, bossslime2y

    reset_var()
    enemy3x = 999
    enemy3y = 999
    slime3x = 1029
    slime3y = 1034
    pygame.display.update()

    countdown()
    
    display_window.blit(level_bg, (0,0))
    if lives == 5:
        display_window.blit(lives_5,(440,10))
    if lives == 4:
        display_window.blit(lives_4,(470,10))
    if lives == 3:
        display_window.blit(lives_3,(500,10))
    if lives == 2:
        display_window.blit(lives_2,(530,10))
    if lives == 1:
        display_window.blit(lives_1,(560,10))
    slimex = enemyx + 30
    slimey = enemyy + 35
    display_window.blit(slime, (slimex, slimey))
    display_window.blit(enemy, (enemyx, enemyy))
    slime2x = enemy2x + 30
    slime2y = enemy2y + 35
    display_window.blit(slime2, (slime2x, slime2y))
    display_window.blit(enemy2, (enemy2x, enemy2y))
    bossslimex = bossx + 50
    bossslimey = bossy + 35
    bossslime2x = bossx + 130
    bossslime2y = bossy + 35
    display_window.blit(bossslime, (bossslimex, bossslimey))
    display_window.blit(bossslime2, (bossslime2x, bossslime2y))
    display_window.blit(boss, (bossx, bossy))
    display_window.blit(laser, (laserx, lasery))
    display_window.blit(user, (userx, usery))
    pygame.display.update()

    while level_num == 6:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit(); sys.exit();

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_SPACE]:
            shoot()
        
        if keys[pygame.K_LEFT]:
            left()
            
        if keys[pygame.K_RIGHT]:
            right()

        enemy_movement()
        enemy_shoot()
        continue_loop()
        slime_user_collision()
        laser_enemy_collision()



def level_7():
    global lives, hit, level_num, clock, clock1, enemy_explosion_clock, level_bg, user, enemy, explosion, speed, bossx, bossy, bossslimex, bossslimey, display_window
    global laser, math, lives_5, lives_4, lives_3, lives_2, lives_1, slime, game_over, enemy_speed, kill_count, slime2, slime2x, slime2y, slime3, slime3x, slime3y
    global userx, usery, enemyx, enemy2x, enemy3x, enemy4x, enemy_resx, enemyresy, laserx, lasery, slimex, slimey, enemyalive, enemy2alive, enemy3alive, bossalive
    global bossslime2, bossslime2x, bossslime2y

    reset_var()
    pygame.display.update()

    countdown()
    
    display_window.blit(level_bg, (0,0))
    if lives == 5:
        display_window.blit(lives_5,(440,10))
    if lives == 4:
        display_window.blit(lives_4,(470,10))
    if lives == 3:
        display_window.blit(lives_3,(500,10))
    if lives == 2:
        display_window.blit(lives_2,(530,10))
    if lives == 1:
        display_window.blit(lives_1,(560,10))
    slimex = enemyx + 30
    slimey = enemyy + 35
    display_window.blit(slime, (slimex, slimey))
    display_window.blit(enemy, (enemyx, enemyy))
    slime2x = enemy2x + 30
    slime2y = enemy2y + 35
    display_window.blit(slime2, (slime2x, slime2y))
    display_window.blit(enemy2, (enemy2x, enemy2y))
    slime3x = enemy3x + 30
    slime3y = enemy3y + 35
    display_window.blit(slime3, (slime3x, slime3y))
    display_window.blit(enemy3, (enemy3x, enemy3y))
    bossslimex = bossx + 50
    bossslimey = bossy + 35
    bossslime2x = bossx + 130
    bossslime2y = bossy + 35
    display_window.blit(bossslime, (bossslimex, bossslimey))
    display_window.blit(bossslime2, (bossslime2x, bossslime2y))
    display_window.blit(boss, (bossx, bossy))
    display_window.blit(laser, (laserx, lasery))
    display_window.blit(user, (userx, usery))
    pygame.display.update()

    while level_num == 7:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit(); sys.exit();

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_SPACE]:
            shoot()
        
        if keys[pygame.K_LEFT]:
            left()
            
        if keys[pygame.K_RIGHT]:
            right()

        enemy_movement()
        enemy_shoot()
        continue_loop()
        slime_user_collision()
        laser_enemy_collision()


def end_scene():
    global endscene, yellowButton, orangeButton
    pygame.mixer.music.load('endgame.mp3')
    pygame.mixer.music.play(-1)
    display_window.blit(endscene,(0,0))
    pygame.display.update()
    yellowButton = button((238, 255, 0),100,420,150,80,'Home')
    orangeButton = button((255, 182, 0),350,420,150,80,'Quit')
    bnst = 0
    while True:
        pygame.mixer.music.load('endgame.mp3')
        pygame.mixer.music.play(-1)
        level_num = 0
        if bnst == 0:
            redrawWindow3()
        pygame.display.update()
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                run = False
                pygame.quit(); sys.exit();
            if event.type == pygame.MOUSEBUTTONDOWN:
                if orangeButton.isOver(pos) and bnst == 0:
                    pygame.quit()
                    sys.exit()
                elif yellowButton.isOver(pos):
                    home()

    #add button code
    #add a quit button on the home screen

    
def math_prob():
    global lives, run, level_bg, display_window, level_num, math, check, x_mark
    font = pygame.font.Font(None, 50)
    choose_operator = random.randint(1,2)
    
    if choose_operator == 1:
        operator = '+'
    elif choose_operator == 2:
        operator = "-"
        
    if level_num == 1:
        num1 = num1p = random.randint(0,10)
        num2 = num2p = random.randint(0,10)
    elif level_num == 2:
        num1 = num1p = random.randint(0,50)
        num2 = num2p = random.randint(0,50)
    elif level_num == 3:
        num1 = num1p = random.randint(0,100)
        num2 = num2p = random.randint(0,100)
    elif level_num == 4:
        num1 = num1p = random.randint(0,250)
        num2 = num2p = random.randint(0,250)
    elif level_num == 5:
        num1 = num1p = random.randint(0,500)
        num2 = num2p = random.randint(0,500)
    elif level_num == 6:
        num1 = num1p = random.randint(0,1000)
        num2 = num2p = random.randint(0,1000)
    elif level_num == 7:
        num1 = num1p = random.randint(0,5000)
        num2 = num2p = random.randint(0,4999)
    if num2 > num1:
        num1 = num2p
        num2 = num1p
    
    num1surface = font.render(str(num1), True, (0, 0, 0))
    num2surface = font.render(str(num2), True, (0, 0, 0))
    operatorsurface = font.render(operator, True, (0, 0, 0))
    display_window.blit(math, (100,100))
    display_window.blit(num1surface,(125,270))
    display_window.blit(num2surface,(300,270))
    display_window.blit(operatorsurface,(250,270))
    pygame.display.update()
    input_box = pygame.Rect(200, 350, 95, 40)
    color = pygame.Color('black')
    text = ''
    final_res = ''
    done = False
    b_out = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or final_res != '':
                done = True
                if event.type == pygame.QUIT:
                    pygame.quit(); sys.exit();
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    final_res = text
                    done = True
                else:
                    if event.unicode.isnumeric():
                        if len(text) < 4:
                            if event.unicode == 4:
                                text += 0
                            else:
                                text += event.unicode
        display_window.blit(math, (100,100))
        display_window.blit(num1surface,(125,270))
        display_window.blit(num2surface,(300,270))
        display_window.blit(operatorsurface,(250,270))
        txt_surface = font.render(text, True, color)
        display_window.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(display_window, color, input_box, 2)
        pygame.display.flip()
        
    if final_res.isnumeric() == True:
        pass
    else:
        final_res = 9999
    if str(num1 + num2) == final_res and operator == "+" or str(num1 - num2) == final_res and operator == "-":
        pygame.mixer.music.load('right.mp3')
        pygame.mixer.music.play()
        display_window.blit(check, (300,300))
        pygame.display.update()
        pygame.time.delay(3000)
        pygame.mixer.music.load('home_music.mp3')
        pygame.mixer.music.play(-1)
    elif b_out == True:
        pass
    else:
        pygame.mixer.music.load('wrong.mp3')
        pygame.mixer.music.play()
        display_window.blit(x_mark,(325,260))
        pygame.display.update()
        pygame.time.delay(3000)
        pygame.mixer.music.load('home_music.mp3')
        pygame.mixer.music.play(-1)
        lives = lives - 1
        if lives <= 0:
            display_window.blit(game_over,(50,100))
            print("GAME OVER!")
            pygame.display.update()
            pygame.time.delay(5000)
            home()
    
main()
pygame.quit(); sys.exit();
