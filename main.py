#imports
import pygame
from pathlib import Path
import random
import math
from resources import resizer
from resources import EnemyClass
from resources import PlayerClass
from resources import ScreenClass
from resources import BulletClass
from pygame import mixer
pygame.init()

#setting ICON
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('resources/images/Spaceship2.png')
pygame.display.set_icon(icon)

#setting screen
screen_obj = ScreenClass.Screen()
screen_obj.screen_resize()
screen_background = pygame.image.load('resources/images/background_resized.png')
screen = pygame.display.set_mode((screen_obj.screen_width, screen_obj.screen_height))

#setting background music
mixer.music.load('resources/Sounds/background.wav')
mixer.music.play(-1)

#global variables for controlling the state
score_value = 0
health_value = 100
life = 2
playerX_change = 0
playerY_change = 0
fire_ball_counter = 0
out_of_screen_flag = False
inside_the_game = True
bullet_array = []
fireball_list = []
bullet_flag = False
bullet_flag2 =  False
counter = 0
enemylist = []

#function for displaying
def show_score():
    font = pygame.font.Font('resources/fonts/ARCADECLASSIC.TTF', 24)
    score = font.render("Score: "+ str(score_value),True, (255,255,255))
    screen.blit(score,(5,5))
def show_bullets():
    font2 = pygame.font.Font('resources/fonts/ARCADECLASSIC.TTF',20)
    bullet = font2.render("Bullets: "+ str(3-counter),True, (255,255,255))
    screen.blit(bullet,(5,30))
def show_health_value():
    font3 = pygame.font.Font('resources/fonts/ARCADECLASSIC.TTF',22)
    lifer = font3.render("LIFE: "+str(life),True,(255,255,255))
    screen.blit(lifer,(690,5))
def show_lives():
    font4 = pygame.font.Font('resources/fonts/ARCADECLASSIC.TTF',20)
    health = font4.render("HEALTH: "+str(health_value),True,(255,255,255))
    screen.blit(health,(690,30))

def playerFun(player,x,y):
    screen.blit(player,(x,y))

def enemyFun(enemy,x,y):
    screen.blit(enemy,(x,y))
def bulletFun(bullet,x,y):
    screen.blit(bullet,(x,y))

def enemyBulletCollison(xe,ye,xb,yb):
    distance = math.sqrt(math.pow((xe-xb),2)+math.pow((ye-yb),2))
    if distance <= 35:
        return True
    else:
        return False
def gameover(playerY,enemyY):
    if abs(playerY-enemyY)<=50:
        return True
    else:
        return False
def game_over_display():
    font1 = pygame.font.Font('resources/fonts/ARCADECLASSIC.TTF', 60)
    go = font1.render("GAME OVER",True, (255,255,255))
    screen.blit(go,(250,250))


#creating player and enemies

player1 = PlayerClass.Player()
player1.player_resize()
player1.add_player()
player1_instance = pygame.image.load('resources/images/player_resized.png') 

for i in range(0,4):
    enemy = EnemyClass.Enemy()
    enemy.enemy_resize()
    enemy.add_enemy()
    enemy.set_instance(pygame.image.load('resources/images/enemy_resized.png'))
    enemy2 = enemy
    del enemy
    enemylist.append(enemy2)

#game logic

while(inside_the_game):
    fire_ball_counter+=1
    screen.fill((0,0,0))
    screen.blit(screen_background,(0,0))
    #displaying enemy
    for enemy1 in enemylist[:]:
        enemy1.change_position()
        enemyFun(enemy1.instance,enemy1.enemyX,enemy1.enemyY)
    #handling click events
    for event in pygame.event.get(): #pygame.event.get() == brings all the events
        if event.type == pygame.QUIT:
            inside_the_game = False
    #player movement in x-axis and setting boundaries:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            elif event.key == pygame.K_RIGHT:
                playerX_change = 5
            #bullets creation
            if event.key == pygame.K_SPACE:
                if counter<3:
                    counter+=1
                    bullet1 = BulletClass.Bullet()
                    if bullet_flag == False:
                        bullet1.bullet_resize()
                    bullet1.set_instance(pygame.image.load('resources/images/bullet_resized.png'))
                    bullet1.add_bullet(player1.playerX,bullet1.bulletY)
                    bullet_sound = mixer.Sound('resources/Sounds/laser.wav')
                    bullet_sound.play()
                    bulletFun(bullet1.instance,bullet1.bulletX,bullet1.bulletY)
                    bullet2 = bullet1
                    del bullet1
                    bullet_array.append(bullet2)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    #bullet handling
    for bullets in bullet_array[:]:
        
        if bullets.state == "fire":
            #bullet_flag2 = True
            bullets.fire_bullet()
            bulletFun(bullets.instance,bullets.bulletX,bullets.bulletY)
            for enemy1 in enemylist[:]:
                if enemyBulletCollison(enemy1.enemyX,enemy1.enemyY,bullets.bulletX,bullets.bulletY) == True:
                    collision_sound = mixer.Sound('resources/Sounds/explosion.wav')
                    collision_sound.play()
                    score_value+=50
                    bullet_array.remove(bullets)
                    enemy1.add_enemy()
                    counter-=1
            if bullets.bulletY<=0:
                del bullets
                bullet_array.pop(0)
                counter-=1
    for enemy in enemylist:
        if out_of_screen_flag == True:
            enemy.enemyY = 2000
            game_over_display()
        if gameover(player1.playerY,enemy.enemyY) == True:
            out_of_screen_flag = True
    if fire_ball_counter % 50 == 0:
        index = random.randint(0,len(enemylist)-1)
        fireball = EnemyClass.enemyBullet()
        fireball.resize()
        fireball.set_instance(pygame.image.load('resources/images/fireball_resized.png'))
        fireball.add_bullet(enemylist[index].enemyX,enemylist[index].enemyY)
        bulletFun(fireball.instance,fireball.X,fireball.Y)
        fireball2 = fireball
        del fireball
        fireball_list.append(fireball2)
    for fireballs in fireball_list[:]:
        if fireballs.state == "fire":
            fireballs.fire_bullet()
            bulletFun(fireballs.instance,fireballs.X,fireballs.Y)
            if enemyBulletCollison(player1.playerX,player1.playerY,fireballs.X,fireballs.Y) == True:
                fireball_list.remove(fireballs)
                health_value-=10
                if health_value == 0:
                    life-=1
                    health_value = 100
                    if life==0:
                        out_of_screen_flag = True
                if fireballs.Y >=600:
                    fireballs.pop(0)
    if out_of_screen_flag == True:
        for enemy in enemylist:
            enemy.enemyY = 2000
            game_over_display()
    player1.change_position(playerX_change)
    #movement for enemy
    playerFun(player1_instance,player1.playerX,player1.playerY)
    show_score()
    show_bullets()
    show_health_value()
    show_lives()
    pygame.display.update()